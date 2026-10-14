# Template: Delegation Brief

The six-field brief an orchestrator hands a delegate, and the return shape the delegate sends back. Copy, fill the brackets, paste into the delegate's task, and collect the return. This is how slices move down the ladder while keeping the bar.

```
TASK SLICE
  <one thing, one sentence.>

CRITERIA SLICE  (with thresholds; the delegate is scored on these only)
  - <criterion id and name, threshold>
  - <criterion id and name, threshold, and the command for any
  machine check on that criterion. Run it on your own scratch
  copy before you return; the fenced tree stays off limits.>

RUNG AND EFFORT
  <rung: Haiku 4.5, Sonnet 5, Opus 5.5, or Fable 5.1.
   effort: low, medium, high, or xhigh, set on this call and
   never inherited from the orchestrator's session; Haiku 4.5 takes no
   effort setting, so write "none".>

BUDGET
  <tokens, dollars, or turns. hard limit per attempt; the slice
   stops if hit. defaults: 40K tokens read or mechanical write,
   90K judgment write, 150K hard reasoning.>

INPUTS
  <exact paths or digested content, sized to the rung's context.
   the loop's history stays with the orchestrator.>

RETURN SHAPE
  The work itself, complete. A self-score (1 to 10) for each
  criterion in the slice. The weakest point named. The assumptions
  made. The run-log lines you would have written, one per
  skill applied and per check run. Return all of it in this shape;
  the orchestrator writes the winning version to disk.
```

## How to fill it

- **TASK SLICE:** one bite only. Two parts means two slices.
- **CRITERIA SLICE:** which criteria from the loop's scorecard apply here, by id. Threshold is usually 8. Any criterion with a machine check carries its command; the delegate runs that command on its own scratch copy before returning and never on the fenced tree; the orchestrator reruns it there after the hash check. The slice passes when every criterion clears on the independent judge; the self-score is a calibration signal only, and it does not open the gate.
- **RUNG AND EFFORT:** set on every call, independent of the orchestrator's session. A delegated call with an unset effort takes the orchestrator's session effort instead, which is how the reference build (a measured run that rebuilt this skill's own protocol with the loop, every context priced from its transcript) put every Sonnet 5, Opus 5.5, and Fable 5.1 worker at xhigh while the run log said "default". Use the run logs for this slice type when there is history. With no history: a read slice (find, search, extract into the return, list claims with sources, read logs or test output, check paths) starts on Haiku 4.5 with no effort setting, or Sonnet 5 at low above 200K of input. A write slice (words or code that land in the deliverable) starts on Sonnet 5 or above: mechanical writes (formatting, tables, column additions) at low, judgment writes (drafting, analysis, synthesis) at medium, and hard reasoning (protocol, argument) on Opus 5.5 at high. Raise effort before you raise the rung. These are design defaults, unmeasured, because the reference build held its workers at inherited xhigh throughout. The short ids in `../references/loop-spec.schema.json` are `haiku`, `sonnet`, `opus`, `fable`.
- **BUDGET:** a hard limit per attempt. With no history: 40K tokens for a read slice or a mechanical write, 90K for a judgment write, 150K for a hard-reasoning slice, design defaults sized around the reference build (its agent calls averaged 80K to 90K tokens as the Workflow summaries count them; halved for the smallest slices, raised for hard reasoning). The slice stops at the limit and reports the gap.
- **INPUTS:** exact paths or digested content. Haiku 4.5 has a 200K context; when the inputs plus the work will fill it, digest the inputs or start one rung up. In a multi-round delegation, the brief carries a one-line-per-attempt digest in place of the attempts.
- **RETURN SHAPE:** the work, honest self-scores per criterion, the weakest point named, the assumptions made, the log lines. The orchestrator writes the log lines and the winning work to disk itself. The delegate is fenced: the orchestrator alone writes.

## Example

A real mechanical write: build the ladder table for `references/model-ladder.md`. Its output lands straight in the deliverable, so it starts on Sonnet 5, not Haiku 4.5, at the low effort a mechanical write takes.

```
TASK SLICE
  Build the ladder table: four rows (Haiku 4.5, Sonnet 5, Opus 5.5,
  Fable 5.1) and four columns (model ID, context window, price per
  million tokens in / out, default slice type). Use only the rows
  given in INPUTS.

CRITERIA SLICE
  - C4 model ladder is current and priced: every cell matches INPUTS
    exactly, and the four names are the only model names in the
    table (threshold 9)
  - C8 your style skill did its job: zero em or en dashes, prices formatted
    the same way in every row (threshold 8). Machine check: the
    command your loop's checker runs, for example
    `python3 check_slice.py <scratch copy>` (dashes 0,
    reversals at most 1), run on your own scratch copy before
    you return; the fenced tree stays off limits.

RUNG AND EFFORT
  Sonnet 5, low.

BUDGET
  40K tokens per attempt.

INPUTS
  The four rows, digested from the claude-api skill's model table
  (cached 2026-06-24, first-party API prices per million tokens):
    Haiku 4.5  | claude-haiku-4-5 | 200K | $1 / $5  | mechanical
    Sonnet 5   | claude-sonnet-5  | 1M   | $2 / $10 | judgment
    Opus 5.5   | claude-opus-5-5  | 1M   | $4 / $20 | hard reasoning
    Fable 5.1  | claude-fable-5-1 | 1M   | $10 / $50 | orchestrator and final judge

RETURN SHAPE
  The table (markdown, fenced). Self-scores for C4 and C8. Weakest
  point named. Assumptions. Two run-log lines:
    style skill applied
    check_slice.py: dashes 0, reversals 0
```

## Before handing off

- Six fields named and filled make a brief.
- The slice fits one pass on the rung. A slice that needs two passes is two slices.
- The starting rung came from the run logs, or from the defaults above.
- The inputs plus the work fit the rung's context. When they will overflow it, digest or start one rung up.
- The judge sits on the cheapest rung the advisor rule allows, at effort high set on the call: Haiku 4.5 read work goes to a machine check for every criterion that has one and to Sonnet 5 for the rest (a slice whose criteria are all machine-checked spends no model verdict); Sonnet 5 work to Opus 5.5; Opus 5.5 work to Fable 5.1; Fable 5.1 work to a fresh Fable 5.1 context. It returns the weakest criterion by id so the brief check can compare ids across rungs. A verdict that is missing or malformed is JUDGE_ERROR; it does not count as a failed attempt. Re-run it once in a fresh judge context, and a second JUDGE_ERROR stops the slice at STOPPED_AT_LIMIT with the judge failure named.
- The promotion rule is in force: when the slice fails the judge, retry once on the same rung, one effort step up, with the judge's named weakness pasted in. Haiku 4.5 takes no effort setting, so its retry changes the brief alone, and so does a retry already at xhigh. Promote one rung when the retry also fails; every rung in order, and a slice promoted off Haiku 4.5 starts on Sonnet 5 at low; the promoted rung starts at the effort the failed retry reached, at minimum; run the brief check on the promoted rung after its first failed attempt and before any retry there, comparing criterion ids, with one brief fix per slice and a restart on the original starting rung and effort; cap two promotions per slice; at the cap, the top, or a second brief-fix condition, the orchestrator takes the slice, judged by a fresh Fable 5.1 context, while a pass and budget remain, else the loop exits STOPPED_AT_LIMIT; keep the best failed attempt, so the promoted rung starts from it; log every promotion. A slice type that clears first-attempt twice in a row starts one step lower next time, effort first, then the rung.
