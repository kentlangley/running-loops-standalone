# Delegation and Promotion

A loop that delegates needs four answers before its first hand-off: what a sub-agent receives, what it returns, who grades it, and what happens when its work fails the bar. Without them, every loop that delegates invents the answers on the spot. This reference is where they live.

The evidence behind it:

- A content-drafting run logged "drafters self-score subjects 2-4 points high" and "the fresh-reader judge found the most real defects." The worker's own score was the wrong gate.
- An audit run found that its two adversarial judges "caught 3 factual defects corrected post-gate." The defects were caught by a separate context, after the self-scored gate had opened.
- A tuning campaign (a replay-scored self-improvement loop) found its first judge could be patched by the thing it scored ("a candidate that patched the scoring function scored J = 9 x 10^8 and was marked valid"), watched worker prompts grow to 150K to 300K tokens by round three, and had no rule at all for a failing worker beyond recording the error.

## The six-field brief

A delegate starts cold. It has none of the loop's context, none of the criteria, and no idea what "done" means for its piece. The brief supplies all of it. Six fields, every time:

1. **Task slice.** One thing. A slice with two things is two slices.
2. **Criteria slice.** Which criteria this slice is scored on, by id, with thresholds, and the command for each machine check, so the delegate can run it before returning. The delegate is scored on the part of the loop's bar its slice can affect.
3. **Rung and effort.** Which model, and how hard it thinks, both set on the call itself. A delegate never inherits effort from the orchestrator's session; a call with the field left off takes the session's own effort, which is how a whole run can end up on xhigh while the log says "default." Defaults with no history: a read slice on Haiku 4.5, or Sonnet 5 at low above 200K of input; a mechanical write on Sonnet 5 at low; a judgment write on Sonnet 5 at medium; hard reasoning on Opus 5.5 at high. See `model-ladder.md`.
4. **Budget.** Tokens, dollars, or turns, as a hard limit per attempt. Defaults with no history: 40K tokens for a read slice or a mechanical write, 90K for a judgment write, 150K for hard reasoning, sized around the reference build (a measured run that rebuilt this skill's own protocol with the loop, every context priced from its transcript; the build's three workflows averaged 80K to 90K tokens per agent call as the Workflow completion summaries count them, a measure the summaries do not define; halved for the smallest slices, raised for hard reasoning). The promotion rule's retry runs inside the same limit. A slice with no budget is a runaway waiting to happen.
5. **Inputs.** Exact paths or content, digested to fit the rung's context. The loop's history stays with the orchestrator.
6. **Return shape.** What comes back, in what form.

The copy-paste form is `../templates/delegation-brief.md`. A brief missing a field is a guess with a model attached.

## The return shape

Every delegate returns the same five things:

- **The work.** The whole deliverable. The judge reads the work.
- **A self-score** per criterion in the slice, 1 to 10, honest.
- **The weakest point,** named. This is what a retry brief quotes.
- **Assumptions** made instead of asking.
- **Log lines,** the run-log lines the delegate would have written, one per skill it applied and per check it ran.

The orchestrator writes the log lines itself. Delegates drop logs; that is expected. The orchestrator catching it is required.

## The fence

A delegate returns. The orchestrator alone writes: into the tree the judge reads, into the criteria, into the run log. It writes the winning attempt to disk after the verdict, so a failed attempt never sits where a later reader could mistake it for the shipped version.

This rule was earned twice. The tuning campaign's first build let a candidate patch its own scoring function, and the fix was a quarantined process plus a hash check on the fenced files before every score. The reference build told its Haiku 4.5 delegates to return their work without writing it, and two of them wrote their first attempts into the skill directory anyway. Cheap rungs follow the shape of a task more than its rules. So the guard is mechanical: hash the fenced files before scoring, and treat a mismatch as a failed attempt.

The criteria slice carries the command for each machine check, and the delegate runs it on its own scratch copy, a folder it owns, before it returns. It never runs a check against the fenced tree; the fenced tree is the orchestrator's to touch. The orchestrator reruns every check on the fenced tree after the hash check, and only that rerun counts toward the verdict.

## Where a slice starts

With history, a slice starts on the cheapest rung and effort that have cleared that slice type before, per the run logs. Without history, split first by whether the slice reads or writes:

| Slice type | Examples | Starting rung and effort |
|---|---|---|
| Read | finds, searches, extracts into the return, lists claims with sources, reads logs or test output, checks paths | Haiku 4.5, none (thinking budget, no effort setting); Sonnet 5 at low above 200K of input |
| Mechanical write | formatting, table-building, column additions | Sonnet 5, low |
| Judgment write | drafting, analysis, synthesis, a reference from a spec | Sonnet 5, medium |
| Hard reasoning | protocol design, argument, anything the orchestrator would otherwise do itself | Opus 5.5, high |

The tie-break: a slice that both reads and writes is a write slice when its output lands in the deliverable. Two rules ride along. Haiku 4.5's context is 200K, so a read slice that must take in more than that starts on Sonnet 5 at low, however simple the task. And every rung gets a digest: in a multi-round delegation the orchestrator writes one line per prior attempt and the brief carries those lines in place of the attempts.

These starting efforts are design defaults and unmeasured. The reference build held every worker at an inherited xhigh whatever the slice type, so no run has yet measured Sonnet 5 at low or at medium against real work. Your first runs are the measurement, and the run logs move the defaults once they report.

## Judge separation

The score that opens a gate comes from a context other than the one that did the work. Six rules make that real:

- **Separate context.** The judge is a fresh agent, or a machine check, that reads the work and the criteria slice. The worker's self-score is withheld from the judge; the orchestrator compares the two after the verdict, so the judge cannot anchor on it.
- **The advisor rule, one rung up.** Haiku 4.5 work is judged by Sonnet 5 or above; Sonnet 5 work by Opus 5.5 or above; Opus 5.5 work by Fable 5.1; Fable 5.1 work by a fresh Fable 5.1 context, the one exception at the top. A machine check may judge any rung. The reviewer is at least as capable as the one reviewed, and here that means a rung up.
- **Cheapest rung the advisor rule allows, effort set on the call.** The judge runs on the cheapest rung that clears the advisor rule: Haiku 4.5 read work goes to a machine check for every criterion that has one and to Sonnet 5 for the rest (a slice whose criteria are all machine-checked spends no model verdict); Sonnet 5 work to Opus 5.5; Opus 5.5 work to Fable 5.1. Judge effort is high, set on the call the same as any delegated call. In the reference build every verdict ran on Fable 5.1 regardless of what it was judging; judging the Sonnet 5 attempts on Opus 5.5 would have cut the reword pass from $2.18 to $1.40 per completed slice (over the seven reword slices that shipped; the eighth ran the ladder out) on the same tokens. The gate that prints FINAL stays with a fresh Fable 5.1 context, the one exception.
- **The lean judge brief.** The judge reads the work in full, the criteria slice, and only the reference material each criterion names, leaving out the loop's history and any file no criterion cites. A summary of the work is never the thing judged, and every extra file is paid for again in every verdict.
- **Ranked judges.** A machine check outranks a model judge. A model judge outranks a self-score. On disagreement the stronger judge wins, and a failed machine check fails the slice whatever the model judge said.
- **The undelegated loop too.** A single-context prompt loop may self-score its ITERATING passes. FINAL prints only when a machine check, a fresh context, or the human on an attended run confirms the floor.

Log the self-score beside the independent score every time. A gap above two points on the same criterion means the brief was unclear or the delegate is soft passing. Either way the next brief changes. In the reference build, a Sonnet 5 second-opinion judge scored a criterion 9 where the Fable 5.1 judge found a real contradiction and scored it 7. A judge below the worker's rung misses what a judge above it catches; that is the advisor rule in one data point.

## The promotion rule

When a delegated slice scores below its threshold on the independent judge:

1. **Retry once on the same rung, one effort step up.** Paste the judge's named weakness into the brief and raise effort one step: low to medium, medium to high, high to xhigh, which is the ceiling. Haiku 4.5 has no effort setting, so its retry changes the brief alone, and a retry already at xhigh changes the brief alone too. Most failures are a missing sentence in the brief, and effort comes before a model change; the retry changes both, and the log records both.
2. **Promote one rung** if the retry also fails. Haiku 4.5 to Sonnet 5, Sonnet 5 to Opus 5.5, Opus 5.5 to Fable 5.1. Every rung in order. Skipping a rung is never allowed, for time or for money. The promoted rung starts at the effort the failed retry reached, and never lower: a slice promoted off Haiku 4.5 starts Sonnet 5 at low, since Haiku 4.5 carries no effort setting of its own to carry forward. So a promotion can never quietly hand the next rung an easier setting than the one that just failed.
3. **Run the brief check on the promoted rung** after its first failed attempt and before any retry there. If its weakest criterion id matches the weakest id of the attempt that triggered the promotion (the prior rung's retry), the brief is the fault: rewrite it, restart on the slice's original starting rung and effort (the rung and effort it began on, even when two promotions preceded the check), and log a brief fix. A brief fix resets the retry and promotion counters and is capped at one per slice. Match on the id. The reference build compared the judge's free-text weakness instead, the judge had written its detail into that field, and a slice climbed from Sonnet 5 to Opus 5.5 to Fable 5.1 failing on the same criterion every time while the check slept. The judge's weakest field is an enum of the criteria ids, and the detail lives in its own field.
4. **Cap at two promotions per slice.** At the cap, at the top of the ladder, or on a second brief-fix condition, the orchestrator takes the slice itself, judged by a fresh Fable 5.1 context, provided at least one pass and the slice's budget remain. Otherwise the loop exits STOPPED_AT_LIMIT with the slice named. The loop never fakes a pass because the ladder ran out.

A missing or malformed verdict is its own outcome, **JUDGE_ERROR**, and never counts as a failed attempt: re-run the verdict once in a fresh judge context. A second JUDGE_ERROR stops the slice, and the loop reports STOPPED_AT_LIMIT with the judge failure named, not the worker's.

Two guards sit on the rule:

- **Keep the best attempt.** Every failed attempt is recorded with its work, scores, and cost. The promoted rung starts from the best one. The loop never ships work worse than the best attempt it already holds.
- **Log everything.** Slice, from rung, to rung, weakest criterion, self-score, independent score. A promotion made before a brief check fires stays in the log with its cost, tagged as superseded by the brief fix: it still counts toward the cost per completed slice and no longer counts toward the cap.

The counts are design defaults, chosen for the reasons below and open to revision from run logs: retry once, one effort step up, because every retry in the reference build passed once the weakness was in the brief (at an effort already held at xhigh); the effort step before the rung, as the claude.dev post "What a task costs on Opus 5.5" (Addy Osmani, 2026-09-25) puts it: "Raise effort before you change models"; xhigh as the retry ceiling, because max stays reserved for a single session; every rung in order, so the run log can attribute a fix to one rung and cost per completed slice stays comparable across runs; cap two, because three rungs on one brief is promotion churn by definition; one brief fix, so the cycle is bounded by the rule and by the loop's limit; demote after two clean passes, because one clean pass is luck; budgets per attempt of 40K, 90K, and 150K tokens by slice type, sized around the reference build's 80K-to-90K average per call, halved for the smallest slices and raised for hard reasoning.

## Four worked scenarios

**A dash.** Sonnet 5 at low drafts a template, a mechanical write. The gate's machine check finds one em dash; the delegate's own check missed it because it checked the wrong file. The model judge never runs; the slice fails on C8 with the machine's note. Retry on Sonnet 5, one effort step up to medium, with the note pasted in. Second attempt is clean and the Opus 5.5 judge scores the floor at 8. Outcome: PASS on Sonnet 5 at medium, one retry, no promotion. Cost: two Sonnet 5 calls plus one Opus 5.5 verdict.

**A missing field.** Sonnet 5 at medium drafts a brief template and leaves out the return shape. Judge: C1 at 5, weakest named. Retry on Sonnet 5, one effort step up to high, with the weakness; the return shape appears but lists three of five parts. Judge: C1 at 6. Two failures on the same rung, same criterion, different detail. Promote to Opus 5.5, starting at high, the effort the failed retry reached. Opus 5.5's draft carries all six fields and all five parts; floor 8. Outcome: PASS on Opus 5.5 at high, one promotion logged (S1, Sonnet 5 to Opus 5.5, C1, self 8, independent 6), judged by Fable 5.1.

**A bad brief.** Sonnet 5 at medium writes a ladder reference and never cites the source table. Judge: C5 fails, weakness "no source cited." Retry at high with the weakness; still no citation, because the brief never gave the source. Promote to Opus 5.5 at high (logged). Opus 5.5's first attempt fails C5 with the same weakness. The brief check fires before any Opus 5.5 retry: two rungs, same criterion id, so the brief is the fault (the detail may differ in wording, which is why the check matches on the id). The brief is rewritten to include the source line, the counters reset, and the slice restarts on Sonnet 5 at medium, which passes. Outcome: PASS on Sonnet 5 at medium, one promotion in the log tagged superseded, one brief fix logged, zero promotions against the cap. The Opus 5.5 call was the price of the check, and it is on the bill.

**The cap.** A hard slice starts on Opus 5.5 at high, fails, retries at xhigh, and promotes to Fable 5.1 at xhigh, the effort the failed retry reached (one promotion). Fable 5.1 fails its first attempt with a different weakness, so the brief check does not fire; its retry fails too, and xhigh is already the ceiling. The rung is the top, so the rule stops here. With a pass and budget remaining, the orchestrator takes the slice in its own context, and a fresh Fable 5.1 context judges the result. With neither remaining, the loop exits STOPPED_AT_LIMIT and names the slice. Both outcomes are reported plainly.

## Demotion

The ladder learns downward too. A slice type that clears the bar on first attempt at a rung and effort, twice in a row, starts one step lower next time: effort first, then the rung, so Opus 5.5 at high drops to Opus 5.5 at medium before it drops to Sonnet 5. A slice type that needed a promotion starts on the rung and effort it passed at. Starting rungs and efforts come from the run logs.

The faster way to learn a rung is a **calibration probe**: start one slice one step below its default, effort first, then the rung, judge it exactly like any other slice, and let the promotion rule run. If the lower step clears it, the default moves down for that slice type. If it fails twice and promotes, the run log now holds the cost of finding out, and the default stays. The tuning campaign ran the same move as a `calibrate` step, ranking Haiku, Sonnet, and Opus by cost per improving attempt before freezing its worker. Log a probe as a probe.

## When to keep the worker fixed

Promotion changes the worker. That is fine when each attempt is judged against a fixed bar. It breaks the judge when attempts are compared against each other across history: a replay-scored search tree, a tuning run, an autoresearch run. There, attempt twelve is scored against attempts one to eleven, and a swapped worker means the history stops predicting the future. The tuning campaign's rule stands: freeze the worker for the whole campaign, and test a different rung as a new campaign. Promote between campaigns.

## Two senses of up

**Promotion** moves a slice up the model ladder within a loop. **Graduation** moves a trusted loop up the run methods, from a prompt to `/loop` to `/schedule`. One is about a model. The other is about trust. Keep the words apart so the run log is readable.

## Cost per completed slice

The number that decides a starting rung is cost per completed slice: every attempt, every retry, every promotion, and every judge call, until the slice passed. A Haiku 4.5 slice that took two attempts and a promotion to Sonnet 5 cost more than a Sonnet 5 slice that passed first time, and the judge verdicts often dominate the bill, which is why judges sit on the cheapest rung the advisor rule allows. The run log carries this number and the next run reads it. Worked arithmetic is in `model-ladder.md`.

The reference build priced its own delegation work twice, and the two numbers disagree for a reason worth naming. Its own record summed every transcript line and reached $88.51. A message is written once per content block, so that sum counted each message several times. `scripts/cost_by_class.py` counts each message once. On that count the same run's 61 delegate and judge contexts cost $38.36, of which the judges took $26.89, 70 percent, every verdict on Fable 5.1 back then. The orchestrator's own session cost $26.72, 51 percent of it output, held at xhigh the whole run. The full run, orchestrator and delegates together, cost $65.08.

A fresh delegate or judge context opened at about 68K tokens before its brief, most of it harness, and a Fable 5.1 verdict averaged $0.90, 79 percent cache writes and 15 percent output, against $0.38 for the same tokens re-priced on Opus 5.5; judging the Sonnet 5 attempts on Opus 5.5 would have cut the reword pass from $2.18 to $1.40 per completed slice (over the seven reword slices that shipped; the eighth ran the ladder out). The run log records the effort the transcript shows, the same source `scripts/cost_by_class.py` reads, beside the effort the brief asked for. Carry contexts opened alongside cost per completed slice in every run log; a cheaper rung that opens more contexts can still cost more.

## Running it in a workflow

Independent slices run in parallel, and the promotion rule belongs in the script. The shape:

```
for each slice, in parallel:
  rung, effort = starting rung and effort for the slice kind (read or write); promotions = 0; brief_fixes = 0
  loop:
    attempt 1: agent(model=rung, effort=effort)          -> machine check -> verdict
    if pass: return PASS
    if rung was promoted into and weakest_id == weakest_id of the attempt that triggered the promotion:
        if brief_fixes == 1: return ORCHESTRATOR_TOOK_IT
        rewrite brief; rung, effort = original starting rung and effort; promotions = 0; brief_fixes = 1
        tag the prior promotion superseded; log BRIEF_FIX; continue
    effort = one effort step up (ceiling xhigh; Haiku 4.5 stays at none)
    attempt 2: agent(model=rung, effort=effort), with the named weakness   -> machine check -> verdict
    if pass: return PASS
    if promotions == 2 or rung is the top: return ORCHESTRATOR_TOOK_IT
    rung += 1; effort = max(effort, low), never lower; promotions += 1; log the promotion

verdict = agent(model=cheapest rung the advisor rule allows, effort=high), self-score withheld
if the verdict is missing or malformed: re-run it once; still missing: return JUDGE_ERROR
```

Every `agent()` call in the script carries `model` and `effort`, worker and judge alike. The reference build's scripts left effort off their worker calls, and a Workflow `agent()` call with no `effort` field inherits the orchestrator's session effort; that is how every Sonnet 5, Opus 5.5, and Fable 5.1 worker in the reference build ran at xhigh while the run log said "default." Setting `effort` on every call is what keeps the log and the bill in agreement.

The outcome words are the same everywhere in the skill: PASS, RETRY, PROMOTE, BRIEF_FIX, ORCHESTRATOR_TOOK_IT, and JUDGE_ERROR in the delegation log, and STOPPED_AT_LIMIT as the loop's exit state. `loop-spec.schema.json` carries them as enums. ORCHESTRATOR_TOOK_IT becomes STOPPED_AT_LIMIT at the loop level when no pass or budget remains, and JUDGE_ERROR becomes STOPPED_AT_LIMIT at the loop level too, when its own rerun also fails, with the judge failure named.

Three things the script must get right, all learned the hard way. The judge's verdict schema constrains `weakest` to the criteria ids, so the brief check compares ids. And the criteria slice and the task slice agree on scope: in one rewording slice the task said to leave a copy-paste code block alone while the criteria counted reversals inside it, so every rung failed the same criterion for a reason no rung could fix. That is a brief fault too, and the brief check is the only rule that catches it. And the script treats an empty verdict as JUDGE_ERROR and never as a fail: the reference build's reword script turned an empty verdict into a fail, so a judge that returned nothing could burn a retry or a promotion that belonged to the worker.

Every attempt and every verdict lands in the workflow journal, which is the delegation log. In environments where the Agent tool is blocked (an audit run hit `teammateMode=iterm2` outside iTerm2 and so did the reference build), the Workflow tool is the delegation path and the script above is the whole protocol.
