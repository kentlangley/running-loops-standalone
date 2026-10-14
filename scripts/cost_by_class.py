#!/usr/bin/env python3
# Copyright (c) 2026 Kent Langley (https://kentlangley.com)
# SPDX-License-Identifier: MIT
"""cost_by_class.py: price a loop from its transcripts, by token class, role, rung, and slice.

Reads Claude Code transcripts (JSONL) and reports what the article "What a task costs on
Opus 5.5" says to check in /usage, in loop form: cache share, output against input, and how
many fresh contexts each completed slice opened.

Usage:
    python3 cost_by_class.py --workflows DIR [DIR ...] [--session FILE.jsonl] [--json]
                             [--reprice-judge FROM=TO] [--exclude SLICE ...] [--per-line]

    --workflows  one or more workflow agent folders (each holds agent-*.jsonl beside
                 agent-*.meta.json), for example
                 ~/.claude/projects/<project>/<session>/subagents/workflows/wf_<id>
    --session    the orchestrator's own session transcript, priced on the model it ran on
    --json       print the rows as JSON instead of Markdown tables
    --reprice-judge FROM=TO
                 also price every judge call that followed a worker attempt on rung FROM as if
                 it had run on rung TO (same tokens), per slice and on average; for example
                 sonnet=opus asks what the advisor rule's cheapest judge would have cost
    --exclude    slices to leave out of the re-priced mean (for example one that shipped nothing)
    --per-line   sum every transcript line instead of each message once; this reproduces the
                 overcount described below and exists only to show it

Agent labels follow the convention role:slice@rung (for example do:model-ladder@sonnet or
judge:model-ladder@opus); the role is the text before the colon and the slice is the text
between the colon and the first @ or #.

Counting rule. A transcript writes one line per content block (thinking, text, tool use), and
every line repeats the usage of the whole message, with output_tokens growing as the message
streams. Each message is counted once, keeping the largest value seen for each field. Summing
every line overcounts: a measured build run reported $88.51 for its delegation
calls that way, against $38.36 counted once per message.

Effort is read from the transcript (the "effort" field on assistant records), not from the
brief, so an agent that inherited the orchestrator's session effort shows what it really ran at.

Prices are first-party, per million tokens: input and output from the claude-api model table
(cached 2026-06-24); cache reads for Opus 5.5 ($0.20) from the claude-api skill's Opus 5.5 note,
for Fable 5.1 ($0.25) from the claude.dev post of 2026-09-25, and for Sonnet 5 and Haiku 4.5 at
one tenth of input. Cache writes bill at 1.25x input (five-minute lifetime).
"""

from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import re
import sys

PRICE = {  # input, output, cache read, per million tokens
    "haiku": (1.0, 5.0, 0.10),
    "sonnet": (2.0, 10.0, 0.20),
    "opus": (4.0, 20.0, 0.20),
    "fable": (10.0, 50.0, 0.25),
}
FIELDS = ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")


def rung_of(model: str) -> str:
    """Map a model id or alias (claude-opus-5-5, opus) to its rung name."""
    m = (model or "").lower()
    for rung in PRICE:
        if rung in m:
            return rung
    return "?"


PER_LINE = False  # set by --per-line


def read_transcript(path: str) -> tuple[list[dict], collections.Counter, str]:
    """Return one usage dict per message (largest value per field), the efforts seen, and the
    first timestamp (so attempts on the same slice can be put in order)."""
    by_id: dict[str, dict] = {}
    order: list[str] = []
    efforts: collections.Counter = collections.Counter()
    first_ts = ""
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not first_ts and isinstance(rec.get("timestamp"), str):
                first_ts = rec["timestamp"]
            if rec.get("type") == "assistant" and isinstance(rec.get("effort"), str):
                efforts[rec["effort"]] += 1
            msg = rec.get("message")
            if not (isinstance(msg, dict) and isinstance(msg.get("usage"), dict)):
                continue
            usage = {k: int(msg["usage"].get(k) or 0) for k in FIELDS}
            key = msg.get("id") or f"line{len(order)}"
            if PER_LINE:
                key = f"line{len(order)}"
            if key not in by_id:
                by_id[key] = usage
                order.append(key)
            else:
                by_id[key] = {k: max(by_id[key][k], usage[k]) for k in FIELDS}
    return [by_id[k] for k in order], efforts, first_ts


def price(usages: list[dict], rung: str) -> dict:
    p_in, p_out, p_read = PRICE.get(rung, (0.0, 0.0, 0.0))
    tok = {k: sum(u[k] for u in usages) for k in FIELDS}
    cost = {
        "fresh": tok["input_tokens"] * p_in / 1e6,
        "cache_write": tok["cache_creation_input_tokens"] * p_in * 1.25 / 1e6,
        "cache_read": tok["cache_read_input_tokens"] * p_read / 1e6,
        "output": tok["output_tokens"] * p_out / 1e6,
    }
    first = usages[0] if usages else {k: 0 for k in FIELDS}
    return {
        **tok,
        **{f"usd_{k}": v for k, v in cost.items()},
        "usd": sum(cost.values()),
        "messages": len(usages),
        "opening_context": first["input_tokens"] + first["cache_creation_input_tokens"] + first["cache_read_input_tokens"],
    }


def price_as(row: dict, rung: str) -> float:
    """What a row's tokens would cost on another rung."""
    p_in, p_out, p_read = PRICE[rung]
    return (row["input_tokens"] * p_in + row["cache_creation_input_tokens"] * p_in * 1.25
            + row["cache_read_input_tokens"] * p_read + row["output_tokens"] * p_out) / 1e6


def agent_rows(folders: list[str]) -> list[dict]:
    rows = []
    for folder in folders:
        for meta_path in sorted(glob.glob(os.path.join(os.path.expanduser(folder), "agent-*.meta.json"))):
            meta = json.load(open(meta_path, encoding="utf-8"))
            label = meta.get("description", "")
            role, _, rest = label.partition(":")
            slice_id = re.split(r"[@#]", rest)[0] if rest else "?"
            usages, efforts, first_ts = read_transcript(meta_path.replace(".meta.json", ".jsonl"))
            rung = rung_of(meta.get("model", ""))
            rows.append({
                "run": os.path.basename(os.path.normpath(folder)),
                "label": label,
                "role": role or "?",
                "slice": slice_id,
                "rung": rung,
                "effort_observed": ",".join(sorted(efforts)) or "none recorded",
                "first_timestamp": first_ts,
                **price(usages, rung),
            })
    return rows


def md_table(head: list[str], rows: list[list]) -> str:
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Price a loop's transcripts by token class, role, rung, and slice.")
    ap.add_argument("--workflows", nargs="*", default=[], help="workflow agent folders (agent-*.jsonl + agent-*.meta.json)")
    ap.add_argument("--session", help="the orchestrator's session transcript")
    ap.add_argument("--session-rung", default=None, help="rung for --session if the model cannot be read (default: from the transcript)")
    ap.add_argument("--json", action="store_true", help="print JSON rows instead of Markdown")
    ap.add_argument("--reprice-judge", help="FROM=TO: re-price judge calls that followed a FROM attempt on rung TO")
    ap.add_argument("--exclude", nargs="*", default=[], help="slices to leave out of the re-priced mean")
    ap.add_argument("--per-line", action="store_true", help="sum every line (reproduces the overcount; for the record only)")
    args = ap.parse_args(argv)
    global PER_LINE
    PER_LINE = args.per_line
    if not args.workflows and not args.session:
        ap.error("give --workflows, --session, or both")

    rows = agent_rows(args.workflows)
    session = None
    if args.session:
        usages, efforts, _ = read_transcript(args.session)
        model = args.session_rung
        if not model:
            models = collections.Counter()
            for line in open(args.session, encoding="utf-8", errors="replace"):
                try:
                    msg = json.loads(line).get("message")
                except json.JSONDecodeError:
                    continue
                if isinstance(msg, dict) and msg.get("model"):
                    models[rung_of(msg["model"])] += 1
            model = models.most_common(1)[0][0] if models else "?"
        session = {"label": "orchestrator", "role": "orchestrator", "rung": model,
                   "effort_observed": ",".join(sorted(efforts)) or "none recorded", **price(usages, model)}

    if args.json:
        print(json.dumps({"agents": rows, "session": session}, indent=2))
        return 0

    def pct(part, whole):
        return f"{100 * part / whole:.0f}%" if whole else "0%"

    by_rr = collections.defaultdict(lambda: collections.Counter())
    efforts_rr = collections.defaultdict(set)
    for r in rows:
        k = (r["role"], r["rung"])
        by_rr[k]["calls"] += 1
        efforts_rr[k].add(r["effort_observed"])
        for f in ("usd_cache_write", "usd_cache_read", "usd_output", "usd_fresh", "usd", "opening_context"):
            by_rr[k][f] += r[f]
    table = []
    for (role, rung), c in sorted(by_rr.items(), key=lambda kv: -kv[1]["usd"]):
        table.append([f"{role} / {rung}", c["calls"], "; ".join(sorted(efforts_rr[(role, rung)])),
                      f"${c['usd_cache_write']:.2f} ({pct(c['usd_cache_write'], c['usd'])})",
                      f"${c['usd_cache_read']:.2f}", f"${c['usd_output']:.2f} ({pct(c['usd_output'], c['usd'])})",
                      f"${c['usd']:.2f}", f"{c['opening_context'] / c['calls']:,.0f}"])
    if session:
        table.append(["orchestrator / " + session["rung"], f"{session['messages']} msgs", session["effort_observed"],
                      f"${session['usd_cache_write']:.2f} ({pct(session['usd_cache_write'], session['usd'])})",
                      f"${session['usd_cache_read']:.2f}",
                      f"${session['usd_output']:.2f} ({pct(session['usd_output'], session['usd'])})",
                      f"${session['usd']:.2f}", "n/a"])
    print("## By role and rung\n")
    print(md_table(["Role / rung", "Calls", "Effort (observed)", "Cache writes", "Cache reads", "Output", "Total", "Mean opening context (tokens)"], table))

    by_slice = collections.defaultdict(lambda: collections.Counter())
    for r in rows:
        k = (r["run"], r["slice"])
        by_slice[k]["contexts"] += 1
        by_slice[k][r["role"]] += r["usd"]
        by_slice[k]["usd"] += r["usd"]
    srows = [[run, sl, c["contexts"], f"${c['do']:.2f}", f"${c['judge']:.2f}", f"${c['usd']:.2f}"]
             for (run, sl), c in sorted(by_slice.items())]
    print("\n## By slice (cost per completed slice)\n")
    print(md_table(["Run", "Slice", "Contexts opened", "Worker $", "Judge $", "Cost per completed slice"], srows))

    if args.reprice_judge:
        src, _, dst = args.reprice_judge.partition("=")
        if src not in PRICE or dst not in PRICE:
            ap.error("--reprice-judge takes FROM=TO with rungs haiku, sonnet, opus, fable")
        by_slice_rows = collections.defaultdict(list)
        for r in sorted(rows, key=lambda r: r["first_timestamp"]):
            by_slice_rows[(r["run"], r["slice"])].append(r)
        rrows, as_run_sum, re_sum, n_kept = [], 0.0, 0.0, 0
        for (run, sl), rs in sorted(by_slice_rows.items()):
            last, as_run, repriced, path = None, 0.0, 0.0, []
            for r in rs:
                as_run += r["usd"]
                if r["role"] == "do":
                    last = r["rung"]
                    path.append(r["rung"])
                    repriced += r["usd"]
                else:
                    repriced += price_as(r, dst) if last == src else r["usd"]
            rrows.append([run, sl, " > ".join(path), len(rs), f"${as_run:.2f}", f"${repriced:.2f}"])
            if sl not in args.exclude:
                as_run_sum, re_sum, n_kept = as_run_sum + as_run, re_sum + repriced, n_kept + 1
        print(f"\n## Judges after a {src} attempt re-priced on {dst} (same tokens)\n")
        print(md_table(["Run", "Slice", "Worker path", "Contexts", "As run", "Re-priced"], rrows))
        if n_kept:
            print(f"\nMean per completed slice over {n_kept} slices (excluded: {', '.join(args.exclude) or 'none'}): "
                  f"as run ${as_run_sum / n_kept:.2f}, re-priced ${re_sum / n_kept:.2f}.")
        judges = [r for r in rows if r["role"] == "judge"]
        if judges:
            print(f"Mean verdict as run: ${sum(r['usd'] for r in judges) / len(judges):.2f}; "
                  f"the same verdicts priced on {dst}: ${sum(price_as(r, dst) for r in judges) / len(judges):.2f}.")

    delegation = sum(r["usd"] for r in rows)
    print(f"\nDelegation total: ${delegation:.2f} over {len(rows)} agent contexts.")
    if session:
        print(f"Orchestrator session: ${session['usd']:.2f}. Whole run: ${delegation + session['usd']:.2f}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
