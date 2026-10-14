# Template: Loop Run Log

Log each pass so the run is auditable and the improvement is visible. One row per pass. Keep it honest, the log is only useful if VERIFY was.

## Run header

- **Task:** <one line>
- **Run method:** prompt / /loop / /schedule
- **Amplifiers:** workflow / multi-agent / ultrathink / effort / the ladder / none
- **Session effort:** <the orchestrator's own session effort, high or xhigh, set at the start, changed only between passes, and held for the run on Bedrock, Google Cloud, or a gateway>. Every delegated call carries its own effort, set fresh on that call; a delegate never inherits this line.
- **Ladder:** orchestrator Fable 5.1; starting rungs and effort by slice type, with no history: read slices Haiku 4.5 (no effort setting), or Sonnet 5 at low above 200K of input; write slices Sonnet 5 at low (mechanical) or medium (judgment), Opus 5.5 at high (hard reasoning) (or from the run logs)
- **Limit:** <max passes / budget / wall-clock>
- **Attended:** yes / no
- **Started:** <ISO timestamp>

## Criteria and thresholds

| # | Criterion | Judge | Judge rung | Threshold |
|---|-----------|-------|------------|-----------|
| 1 | | | | 8 |
| 2 | | | | 8 |
| 3 | | | | 8 |

## Pass log

| Pass | PLAN (next step) | Scores (per criterion) | Weakest point named | DECIDE |
|------|------------------|------------------------|---------------------|--------|
| 1 | | | | ITERATING |
| 2 | | | | ITERATING |
| 3 | | | | FINAL |

## Delegation log

| Pass | Slice | Rung | Effort requested | Effort observed | Attempt | Self-score (floor) | Independent score (floor) | Gap | Weakest named | Outcome | Contexts opened | Cost |
|------|-------|------|-------------------|------------------|---------|-------------------|---------------------------|-----|---------------|---------|------------------|------|
| | | | | | | | | | | | | |

**Effort requested** is the effort set on the delegated call, from the brief. **Effort observed** is the effort the transcript actually shows, read back with `scripts/cost_by_class.py`; a gap between the two means a call ran without an explicit effort and inherited the orchestrator's session effort instead, exactly what put every Sonnet 5, Opus 5.5, and Fable 5.1 worker at xhigh in the reference build (a measured run that rebuilt this skill's own protocol with the loop, every context priced from its transcript) while its log said "default". **Contexts opened** counts this attempt's own fresh context plus its judge, since each one pays to open. **Cost** is this attempt's price alone; cost per completed slice, in Exit, sums every attempt, retry, promotion, and judge call for the slice.

**Outcome values:** PASS / RETRY (same rung, one effort step up, weakness pasted in) / PROMOTE (one rung up, at the effort the failed retry reached) / BRIEF_FIX (brief rewritten, restart on the original rung and effort, not a promotion) / ORCHESTRATOR_TOOK_IT (Fable 5.1 took the slice after the cap) / JUDGE_ERROR (verdict missing or malformed, re-run once in a fresh judge context; never counts as a failed attempt). A slice still short when the loop's limit hits is reported in Exit as STOPPED_AT_LIMIT.

**Rung names:** Haiku 4.5, Sonnet 5, Opus 5.5, Fable 5.1. **Effort values:** low, medium, high, xhigh on Sonnet 5 and above, set on every delegated call and never inherited; none on Haiku 4.5, which takes no effort setting.

## Promotions

| Slice | From rung | To rung | Weakest criterion | Self-score | Independent score | Reason | Superseded by brief fix |
|-------|-----------|---------|-------------------|------------|-------------------|--------|-------------------------|
| | | | | | | | no / yes |

A brief fix gets its own row: Slice | criterion id two rungs failed on | rungs that failed | rung restarted on | what the brief got wrong.

## Exit

- **Exit state:** FINAL / STOPPED_AT_LIMIT
- **Final scores:** <per criterion, from the independent judge>
- **Weakest remaining (if stopped at limit):** <criterion, or the judge failure named when a second JUDGE_ERROR stopped the slice>
- **Passes run:** <n>
- **Rungs used:** <any of Haiku 4.5, Sonnet 5, Opus 5.5, Fable 5.1>
- **Promotions made:** <count and one line each>
- **Cost per completed slice:** <per slice, including retries, promotions, and judge calls>
- **Contexts opened:** <count, delegates and judges together, since each one pays to open>
- **Cost by token class:** <from `scripts/cost_by_class.py`, counted once per message rather than once per transcript line>
- **Skills used:** <list, including judges>
- **Assumptions made:** <list, per the no-questions rule, including those returned by delegates>

## After the run

- [ ] The run log names every rung used and every promotion.
- [ ] Output and run log kept in the project folder, where the next run reads them.
