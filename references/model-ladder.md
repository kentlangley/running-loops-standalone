# The Model Ladder

The ladder is a cost decision, not a quality ranking. Fable 5.1 orchestrates and judges the loop, and Haiku 4.5, Sonnet 5, and Opus 5.5 take the slices it delegates.

## The four rungs

| Rung | Model ID | Context | Price (in / out per million tokens) |
|---|---|---|---|
| Haiku 4.5 | `claude-haiku-4-5` | 200K context | $1 / $5 |
| Sonnet 5 | `claude-sonnet-5` | 1M context | $2 / $10 |
| Opus 5.5 | `claude-opus-5-5` | 1M context | $4 / $20 |
| Fable 5.1 | `claude-fable-5-1` | 1M context | $10 / $50 |

Source for IDs, context windows, and prices: the claude-api skill's model table, cached 2026-06-24, first-party API prices per million tokens.

## What each rung is for

A slice starts on the cheapest rung and the lowest effort that have cleared that kind of slice before, per the run logs. With no history, the start point follows what the slice does. A **read slice** finds, searches, extracts into the return, lists claims with sources, reads logs or test output, or checks paths; a mistake there is cheap to spot, so it starts on **Haiku 4.5**, or on **Sonnet 5 at low** once its inputs pass 200K. A **write slice** puts words or code into the deliverable and starts on **Sonnet 5** or above: mechanical writes (formatting, table-building, column additions) on Sonnet 5 at low, judgment writes (drafting, analysis, synthesis) on Sonnet 5 at medium, hard reasoning (protocol design, argument, anything the orchestrator would otherwise do itself) on **Opus 5.5** at high. The tie-break: a slice that both reads and writes counts as a write slice whenever its output lands in the deliverable.

These starting rungs and efforts are design defaults. The reference build (a measured run that rebuilt this skill's own protocol with the loop, every context priced from its transcript) held every worker at an inherited xhigh, so it never measured Sonnet 5 at low or medium against these slice types; your first runs are the measurement.

**Fable 5.1** never takes the first attempt at a slice. It writes the criteria, writes the briefs, judges, decides, and picks up a slice only when the ladder has run out. This is a design default with two reasons: the orchestrator's context is the loop's memory, and its tokens are the dearest on the ladder. A tuning campaign (a replay-scored self-improvement loop) kept its orchestrator off worker work in its role table, on the same grounds.

## Effort before rung

The three upper rungs take an effort setting: low, medium, high, xhigh, and max. Delegated work uses the first four; max stays out of it. Effort is set on every delegated call and is never inherited: a Workflow `agent()` call without `effort` takes the orchestrator's session effort as its own. In the reference build, an `agent()` call with no `effort` field took the session's xhigh, so every Sonnet 5, Opus 5.5, and Fable 5.1 worker ran at xhigh while the run log said "default." Haiku 4.5 takes a thinking budget instead, per the claude-api skill's thinking and effort table, so a Haiku slice runs at its default and the first lever on that rung is the brief.

Raising effort on the same rung is the first lever everywhere else. Climbing to the next rung is the second. When a delegated slice fails its threshold, the promotion rule runs in order. First, retry once on the same rung, one effort step up: low to medium, medium to high, high to xhigh, which is the ceiling, with the judge's named weakness pasted into the brief. Haiku 4.5 has no effort setting, so its retry changes the brief alone. If the retry also fails, promote one rung, every rung in order. The promoted rung starts at the effort the failed retry reached and never lower. Opus 5.5 hard reasoning therefore runs high, then xhigh, then Fable 5.1: the claude.dev post's rule (if Opus 5.5 on xhigh hits the same problem twice, switch), where the next rung up is Fable 5.1, with one xhigh attempt instead of two, because each attempt here costs a fresh context and a verdict. Demotion runs the same order in reverse: a slice type that clears the bar twice in a row steps effort down first, then the rung.

Source for the order: the claude.dev post "What a task costs on Opus 5.5" (Addy Osmani, 2026-09-25): "Raise effort before you change models." "A check can catch the same bug." The post reserves the downgrade to Sonnet or Haiku for lookups and keeps writing code on the higher rung.

Measure the strongest model at low effort before building a cascade. The claude-api skill's effort guidance reports that on the current family, low effort on a newer model often beats high effort on the prior one, and that a cascade forfeits cache reuse across its models.

## Cost per completed slice

The number that decides the starting rung is cost per completed slice, counting every retry and every promotion. Cost per request leaves the retries and promotions off the bill.

Worked example: a Haiku 4.5 slice needs one retry on the same rung, then a promotion to Sonnet 5, before it passes. The initial attempt runs 5,000 input tokens and 1,000 output tokens: (5,000 / 1,000,000 × $1) + (1,000 / 1,000,000 × $5) = $0.01. The retry carries the judge's named weakness pasted into the brief, so it runs slightly larger, at 5,200 input and 1,000 output tokens: $0.0052 + $0.005 = $0.0102. The promoted attempt on Sonnet 5 inherits the retry history as context, so it runs larger again, at 6,000 input and 1,200 output tokens: (6,000 / 1,000,000 × $2) + (1,200 / 1,000,000 × $10) = $0.024. Three attempts sum to $0.0442.

A Sonnet 5 slice that passes on the first attempt carries no retry history, and runs 5,500 input tokens and 1,100 output tokens: (5,500 / 1,000,000 × $2) + (1,100 / 1,000,000 × $10) = $0.022. The Haiku-first path costs roughly double the Sonnet-first path once every attempt is counted. A promoted attempt can carry a different token count than the original attempt, so the sum always uses the run log's actual counts.

The run log carries that arithmetic. The sticker price of the starting rung says nothing about it.

Add the judge calls, because they often dominate. Each attempt above was graded, as in the reference build, by a fresh Fable 5.1 context reading the work plus the criteria. Under the cheapest-judge rule the Haiku 4.5 verdicts go to a machine check or to Sonnet 5 and the Sonnet 5 verdict to Opus 5.5, so both paths come out cheaper than this example shows. Call that 6,000 input and 1,000 output tokens per verdict: (6,000 / 1,000,000 × $10) + (1,000 / 1,000,000 × $50) = $0.11. The Haiku-first path needed three verdicts ($0.33) and the Sonnet-first path one ($0.11). With judges counted, the Haiku-first path costs $0.3742 against $0.132, close to three times. Cheap rungs are cheap only when they pass early, and the judge's rung sets the price of every retry. Counted once per message by `scripts/cost_by_class.py`, the reference build cost $65.08 across its 61 delegate and judge contexts and the orchestrator's own session: judges took $26.89 of the $38.36 delegate-and-judge total (70 percent), because every verdict ran on Fable 5.1, and the orchestrator's session took the remaining $26.72, half of it output at xhigh. Judge on the cheapest rung the advisor rule allows, with a machine check in the brief and in front of every verdict.

## The cost of a fresh context

Every delegate and every judge opens a fresh context, and opening one costs before the slice even starts. In the reference build, that opening ran about 68K tokens before the brief, most of it harness (system prompt, tool schemas, instructions, skill listing), and about 47K for Haiku 4.5. That opening writes to the cache at 1.25 times the input price. A Fable 5.1 verdict on those tokens averaged $0.90, 79 percent of it cache writes and 15 percent output; the same tokens re-priced on Opus 5.5 come to $0.38. Judging the Sonnet 5 attempts on Opus 5.5 where the advisor rule allows it would have cut the reword pass from $2.18 to $1.40 per completed slice (over the seven reword slices that shipped; the eighth ran the ladder out). Fewer failed attempts and cheaper judge rungs move that bill; a lower judge effort barely touches it, since the opening cost is fixed and effort changes only the output share. The run log records contexts opened per completed slice.

## The 200K rule

Haiku 4.5 carries a 200K context window against the other three rungs' 1M. A slice that must read more than 200K tokens is not a Haiku slice, however simple the task looks. Digest the inputs first, or start on Sonnet 5 at low.

## The judge's rung

The judge for a rung's work runs one rung up or higher, or a machine check, per `the-judge.md`. Fable 5.1 work is judged by a fresh Fable 5.1 context, the one exception at the top. Judge on the cheapest rung the advisor rule allows: Haiku 4.5 read work goes to a machine check for every criterion that has one and to Sonnet 5 for the rest (a slice whose criteria are all machine-checked spends no model verdict); Sonnet 5 work goes to Opus 5.5, and Opus 5.5 work to Fable 5.1. Judge effort is high, set on the call. Keep the judge brief lean: the criteria slice, the work in full, and only the reference material each criterion names, since every extra file is paid for again in every verdict.
