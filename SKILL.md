---
name: running-loops-standalone
description: Turn any task into a self-correcting agent loop. PLAN, DO, VERIFY, DECIDE, repeat until a strict, honestly scored bar is met or a set limit is hit. Covers success criteria as an incorruptible judge, the priced model ladder (Fable 5.1 orchestrates; Opus 5.5, Sonnet 5, and Haiku 4.5 take delegated slices, effort set on every call), the six-field delegation brief, judge separation (the score that opens a gate comes from a context other than the one that did the work, on the cheapest rung the advisor rule allows), and the promotion rule (retry once one effort step up, then one rung up, every rung in order, always logged). Use when you want an agent to carry a task to the finish on its own, self-correct and verify its own work, write a definition of done, hand slices of a loop to cheaper models while keeping the bar, price a loop by cost per completed slice, or set a task running attended or unattended with /loop or /schedule until it clears.
license: "CC-BY-4.0 (text and templates) and MIT (scripts/). See LICENSE."
metadata:
  version: "1.0.0"
  author: "Kent Langley"
  author-url: "https://kentlangley.com"
---

# Running Loops (Standalone)

By [Kent Langley](https://kentlangley.com).

## How It Works With Your Other Skills

The loop is a meta-skill. It runs your other skills. On each pass Claude picks whatever skill the task needs from the skills you have installed (or you name it), and this skill supplies the machinery that keeps the agent going until the bar is met. Nothing else needs installing: every protocol, template, default, and script the loop uses ships in this folder.

- **Prompt design.** The loop protocol IS a prompt, and so is the delegation brief. The success criteria, the four moves, and the rules are prompt design. Write the criteria strict or the loop passes soft. Write the brief complete or the delegate guesses.
- **Validation.** The VERIFY step is validation turned into a rule that runs every pass. The judge is the whole game, and the score that opens the gate comes from a separate context.
- **Fan-out.** Amplifiers like workflow and multi-agent fan-out layer on top of a loop. The delegation protocol here is what makes a fan-out safe to trust.
- **The mental shift.** You stop steering every turn and start defining the bar. Using the AI is turn by turn. Running a loop is handing over the turns.
- **Unattended runs.** Once a loop is trusted, put it on a cadence and walk away.
- **Handoffs.** Decide what to loop unattended, what to loop with a human on the exit, and what to keep out of a loop altogether.
- **ExO.** In ExO terms, loops are the operating primitive of the agentic firm (the Three Compounding Loops). A loop whose stopping condition is tied to your skills' checks is how "done" becomes a measurement.
- **Cost.** The ladder is a cost decision. Cost per completed slice is the number that decides which rung a slice starts on.

## Where the numbers come from

The figures in this skill come from measured runs. **The reference build** is a measured run that rebuilt this skill's own protocol with the loop, every context priced from its transcript. **The tuning campaign** is a replay-scored self-improvement loop. A content-drafting run and an audit run supply the rest. The method itself was first proved on a Lean 4 loop, which supplies no figures. Every count, budget, and starting rung they set is a design default. Change it when your own run logs say otherwise.

## Triggers

- "Run it until it's done" / "keep going until it's real" / "loop until it clears the bar" / "run the loop"
- "Have it self-correct" / "verify and fix its own work" / "iterate until it's right"
- Writing success criteria or a definition of done for an agent task ("when is it done?")
- Setting up a `/loop` or `/schedule` run, an unattended overnight agent, or "let it run itself" / "run this on a schedule"
- "Ralph Wiggum" / "agent loop" / "run an agent in a loop until it succeeds"
- A task that keeps coming back to you turn by turn when it could run itself
- An agent that stops too early, calls weak work done, or games its own score
- "When is it done?" for any AI-produced deliverable
- "Hand this slice to a cheaper model" / "delegate this to a cheaper model" / "which model should do this pass"
- A delegated pass that came back below the bar ("the sub-agent's work isn't good enough"), and the question of what happens next
- "Escalate to a bigger model" / promotion / "judge on a different model"
- Writing a delegation brief
- A sub-agent that scored itself higher than the work deserves

## Core Directives

### What a Loop Is

- MUST hold the definition plainly: an agent loop is telling the AI to keep working on a task until it is actually done, or it hits a limit you set. Nothing fancier than that.
- MUST run the four moves on repeat: PLAN the single next step, DO the work, VERIFY honestly against the bar, DECIDE to stop or go again. `PLAN -> DO -> VERIFY -> DECIDE` and back.
- MUST recognize your move as the handoff. You give the agent three things: the task, a way to check its own work, and permission to keep going. Then you stop approving every turn.
- MUST state the thesis when it helps land: you do not need to be right the first time, you need to know when you are right. The loop is cheap. The knowing is the asset.

### The Judge (Success Criteria)

- MUST write success criteria before running anything. A loop is only ever as good as its definition of done. Without a bar the agent is only talking to itself.
- MUST make the criteria strict, with no soft passes. Vague criteria ("make it good") produce vague loops that declare victory early. Name what "done" actually looks like, in terms that can be scored.
- MUST prefer an incorruptible judge: something that cannot lie about whether the work is done. Compiles or it does not. Test passes or it does not. A scorecard clears the line or it does not. The stronger the judge, the more you can trust the loop unattended.
- MUST turn skills into judges wherever possible. "Your style-guide skill did its job", "a claims check ran, all claims verified", "a logic check ran, all arguments sound", "your brand skill applied" are far stronger criteria than "reads well". This is what makes a skill-routed loop different from a plain one.
- SHOULD keep a human bar in the set when the work ships in someone's name: "the author would be proud to publish this." It catches what the mechanical judges miss.

### The Four Moves

- MUST run PLAN as one step only. State the single next step. This keeps each pass small and honest.
- MUST run DO as produce-or-improve. First pass creates, every later pass fixes the weakest thing from the last VERIFY, even when something else is easier to touch.
- MUST run VERIFY as a brutally honest score: rate each criterion 1 to 10 and list exactly what is still weak. The value of the loop is entirely in the honesty of this step. A flattering VERIFY is a broken loop.
- MUST run DECIDE as a hard gate: if every criterion is 8 or higher on an independent score, print "FINAL" and stop; otherwise print "ITERATING" and go again, fixing the weakest point first. The gate opens on the floor across all criteria.

### The Ladder (Model Choice, Priced)

- MUST name the ladder before delegating anything. Four rungs, cheapest first, with first-party prices per million tokens in and out, and context windows, from the claude-api skill's model table (cached 2026-06-24): **Haiku 4.5** (`claude-haiku-4-5`, $1 / $5, 200K context), **Sonnet 5** (`claude-sonnet-5`, $2 / $10, 1M), **Opus 5.5** (`claude-opus-5-5`, $4 / $20, 1M), **Fable 5.1** (`claude-fable-5-1`, $10 / $50, 1M). Fable 5.1 orchestrates and holds the final judge. The full table with what each rung is good for is in `references/model-ladder.md`.
- MUST treat effort as the first lever and the rung as the second, and set it on every delegated call. Effort (low, medium, high, xhigh) is a field of the brief and an argument of the call, and a delegate never inherits it: a Workflow `agent()` call without `effort` takes the orchestrator's session effort. In the reference build, that put every Sonnet 5, Opus 5.5, and Fable 5.1 worker at xhigh while the run log said "default". Log the effort the transcript shows, which `scripts/cost_by_class.py` reads back, beside the effort the brief asked for. Max stays out of delegated work. Haiku 4.5 takes a thinking budget instead of an effort setting, per the claude-api skill's thinking and effort table, so its lever is the brief. The claude.dev post "What a task costs on Opus 5.5" (2026-09-25) states the order: "Raise effort before you change models." Thinking bills as output, and output was 15 to 35 percent of an attempt's cost in that run, so one effort step is cheap next to a failed attempt. Measure the strongest model at low effort before building a cascade; the claude-api skill's effort guidance reports that low effort on a newer model often beats high effort on the prior one.
- MUST count fresh contexts, because each one pays to open. Every delegate and every judge starts in a fresh context and writes its whole opening prompt to the cache at 1.25 times the input price: about 68K tokens before the brief for a Sonnet 5, Opus 5.5, or Fable 5.1 context in the reference build (about 47K for Haiku 4.5), most of it harness (system prompt, tool schemas, instructions, skill listing). Counted once per message, that run cost $65.08. The orchestrator's own session took $26.72, half of it output at xhigh, and the 61 delegate and judge contexts took $38.36, of which the judges took $26.89. A Fable 5.1 verdict averaged $0.90, 79 percent of it cache writes and 15 percent output. Fewer failed attempts and cheaper judge rungs move that bill; a lower judge effort barely touches it. The run log records contexts opened per completed slice.
- MUST price by cost per completed slice: every attempt, retry, promotion, and judge call until the slice passed. A cheaper request that needs two retries and a promotion costs more than a dearer one that passes first time. The run log records tier, attempts, and the final cost of the slice, and that number decides where the slice starts next time.
- MUST remember Haiku 4.5's 200K context. A slice that must read more than that belongs one rung up, however simple the task. Digest the inputs first or start on Sonnet 5.
- MUST NOT let the ladder become a way to avoid the judge. A cheap rung is only cheap if the same bar applies to its work.

### Delegation (The Brief)

- MUST delegate by slice. A slice is one piece of work judged against a named subset of the criteria. The orchestrator keeps the loop; the delegate gets a slice of DO and returns it for VERIFY.
- MUST hand every delegate a complete brief with six fields: the **task slice** (one thing), the **criteria slice** (which criteria this slice is scored on, by id, with thresholds, and the command for each machine check), the **rung and effort** it runs on (both set on the call), the **budget** (tokens, dollars, or turns), the **inputs** (exact paths or content, digested to fit the rung's context), and the **return shape**. The copy-paste form is `templates/delegation-brief.md`. A brief missing a field is a guess with a model attached.
- MUST require the same return shape from every delegate: the work, a self-score per criterion in the slice, the weakest point named, the assumptions made, and the log lines the delegate would have written. The orchestrator writes those log lines itself. Delegates drop logs; the orchestrator is the backstop.
- MUST fence the delegate. A delegate returns its work. The orchestrator alone writes into the tree the judge reads, the criteria the judge scores against, and the run log, and it writes the winning attempt to disk after the verdict. In the reference build, two Haiku 4.5 delegates wrote their first attempts straight into the skill directory against a brief that said to return them, and the tuning campaign's first build let a candidate patch its own scorer. A hash check on the fenced files before scoring is the cheap guard; treat any mismatch as a failed attempt.
- MUST put the check in the brief. The criteria slice carries the command for each machine-judged criterion (a dash count, a reversal count, a test, a render check), and the delegate runs it on its own scratch copy (a folder it owns, or stdin) before it returns. It never runs a check against the fenced tree. The orchestrator reruns every check on the fenced tree after the hash check, and only that run counts. The claude.dev post: "A check can catch the same bug." In the reference build's reword pass, eight of the nine failed Sonnet 5 attempts missed the reversal budget, a criterion the workers had no way to count.
- MUST digest the inputs. A delegate gets what its slice needs, cut to size, without the loop's history. The tuning campaign watched every worker read every earlier proposal, score, and diff until an attempt faced 150K to 300K tokens by round three, burned its budget cap as a wasted error, and outgrew Haiku 4.5's context. In a multi-round delegation the orchestrator writes a one-line-per-attempt digest and the brief carries that.
- MUST start a slice on the cheapest rung and the lowest effort that have cleared that kind of slice before, per the run logs. With no history, split by what the slice does. A **read slice** finds, searches, extracts into the return, lists claims with sources, reads logs or test output, or checks paths; a mistake there is cheap to spot, so it starts on Haiku 4.5, or on Sonnet 5 at low when its inputs pass 200K. A **write slice** puts words or code into the deliverable and starts on Sonnet 5 or above: mechanical writes (formatting, table-building, column additions) on Sonnet 5 at low, judgment writes (drafting, analysis, synthesis) on Sonnet 5 at medium, hard reasoning (protocol design, argument, anything the orchestrator would otherwise do itself) on Opus 5.5 at high. A slice that both reads and writes is a write slice when its output lands in the deliverable. The split follows the claude.dev post ("Move down to Sonnet or Haiku for lookups, not for writing code") and the reference build, where two Haiku 4.5 writers wrote to disk against the brief and every Haiku write slice needed a retry. These starting efforts are design defaults: that run held its workers at inherited xhigh, so no run has yet measured Sonnet 5 at low or medium, and your first runs are the measurement. Default budgets with no history, each a hard limit per attempt: 40K tokens for a read slice or a mechanical write, 90K for a judgment write, 150K for hard reasoning. These are design defaults sized around the reference build, where the three workflows averaged 80K to 90K tokens per agent call as the Workflow completion summaries count them (955,804 over 12 agents, 827,610 over 9, 3,349,884 over 40; a measure the summaries do not define and the per-agent transcripts do not reproduce), halved for the smallest slices and raised for hard reasoning. The promotion rule's retry runs inside them.
- MUST keep the orchestrator's own work small. Fable 5.1 writes the criteria, writes the briefs, judges, decides, and takes a slice itself only when the ladder has run out (see promotion). This is a design default with two reasons: the orchestrator's context is the loop's memory, and its tokens are the dearest on the ladder. The tuning campaign's role table keeps its orchestrator off worker work on the same grounds.
- MUST run the orchestrator's session at a set effort. High is the default (`references/loop-defaults.toml`); xhigh is a choice for a hard loop. Change it only between passes. Per the claude.dev post, on an API key or a subscription the cache survives the change, and on Bedrock, Google Cloud, or a gateway the change clears it, so there the effort set at the start holds for the run. Never switch the orchestrator's model mid-run: the new model pays to write the whole conversation again. Compact only at a DECIDE boundary, with a note on what to keep, once the context passes about 150K; the claude.dev post puts the payback at about ten turns. A `/loop` or `/schedule` run starts each pass fresh from the run log.
- SHOULD run independent slices in parallel through a workflow, with the promotion rule written into the script so control flow is deterministic and every attempt is journaled. Every `agent()` call in the script carries `model` and `effort`.

### Judge Separation

- MUST open every gate on an independent score. A single-context prompt loop may self-score its ITERATING passes; that is how a prompt loops itself. FINAL prints only when a context other than the one that did the work confirms the floor: a machine check, a fresh sub-agent, or the human on an attended run. A content-drafting run showed drafters scoring their own work two to four points above an independent judge. A self-score never opens the gate.
- MUST keep the worker and the judge in separate contexts for every delegated slice, and for any slice the orchestrator takes itself, which a fresh Fable 5.1 context judges.
- MUST run the model judge one rung up or higher. Haiku 4.5 work is judged by Sonnet 5 or above, Sonnet 5 by Opus 5.5 or above, Opus 5.5 by Fable 5.1, and Fable 5.1 work by a fresh Fable 5.1 context, the one exception at the top of the ladder. A machine check may judge any rung. This is the advisor rule from the claude-api skill (the reviewer is at least as capable as the one reviewed), and in this skill it means a rung up.
- MUST judge on the cheapest rung the advisor rule allows, at an effort set on the call. Haiku 4.5 read work goes to a machine check for every criterion that has one and to Sonnet 5 for the rest (a slice whose criteria are all machine-checked spends no model verdict); Sonnet 5 work to Opus 5.5; Opus 5.5 work to Fable 5.1. Judge effort is high. In the reference build every verdict ran on Fable 5.1; judging the Sonnet 5 attempts on Opus 5.5 would have cut the reword pass from $2.18 to $1.40 per completed slice (over the seven reword slices that shipped; the eighth ran the ladder out) on the same tokens (`scripts/cost_by_class.py`, re-priced). The gate that prints FINAL stays with a fresh Fable 5.1 context.
- MUST rank judges and let the stronger one win on disagreement: a machine check outranks a model judge; a model judge outranks a self-score. If the machine check fails, the slice fails, whatever the model judge said, and no model verdict is spent on it. A pass/fail judge scores 10 on a pass and 1 on a fail, so the floor rule works unchanged.
- MUST move the judge when the slice moves. A slice promoted from Sonnet 5 to Opus 5.5 is now judged by Fable 5.1; the judge climbs with the worker so it stays one rung up. In the reference build every verdict came from Fable 5.1, which made this invisible; the loop library (`references/loop-library.md`) makes it explicit.
- MUST withhold the self-score from the judge and compare the two after the verdict. The judge reads the work and the criteria slice. The orchestrator logs the self-score beside the independent score every pass; a gap above two points on the same criterion means the brief was unclear or the delegate is soft passing, and either way the next brief changes.
- MUST have the judge read the work itself, in full. A summary of the work is never the thing judged. Give the judge the criteria slice, the work, and exactly the reference material each criterion names (SKILL.md for a consistency criterion, the original file for a meaning criterion), and leave out the loop's history and every file no criterion names: each extra file is paid for again in every verdict.

### Promotion (When a Delegation Fails the Bar)

- MUST run the promotion rule, in this order, when a delegated slice scores below its threshold on the independent judge:
  1. **Retry once on the same rung, one effort step up**, with the judge's named weakness pasted into the brief: low to medium, medium to high, high to xhigh, which is the ceiling. Haiku 4.5 has no effort setting, so its retry changes the brief alone, and a retry already at xhigh changes the brief alone too. Most failures are a missing sentence in the brief, and the claude.dev post puts effort before model; the retry changes both, and the log records both. A calibration probe separates the two when it matters.
  2. **Promote one rung** if the retry also fails: Haiku 4.5 to Sonnet 5, Sonnet 5 to Opus 5.5, Opus 5.5 to Fable 5.1. Every rung in order. Skipping a rung is never allowed, for time or for money. The promoted rung starts at the effort the failed retry reached, and never lower, so the brief check cannot fire on an effort drop; a slice promoted off Haiku 4.5 starts Sonnet 5 at low. Opus 5.5 hard reasoning therefore runs high, then xhigh, then Fable 5.1: the post's rule (if Opus 5.5 on xhigh hits the same problem twice, switch), where the next rung up is Fable 5.1, with one xhigh attempt instead of two, because each attempt here costs a fresh context and a verdict.
  3. **Run the brief check on the promoted rung** after its first failed attempt and before any retry there: if its weakest criterion id matches the weakest id of the attempt that triggered the promotion (the prior rung's retry), the brief is the fault. Rewrite the brief, restart on the slice's original starting rung and effort (even when more than one promotion preceded the check), and log a brief fix. A brief fix resets the retry and promotion counters for the slice and is capped at one per slice. Match on the id: in the reference build a judge wrote its detail into the weakest field, the string comparison never matched, and a slice climbed three rungs failing on the same criterion with the check asleep. Constrain the judge's weakest field to the criteria ids.
  4. **Cap promotions at two per slice.** At the cap, at the top of the ladder, or on a second brief-fix condition, the orchestrator takes the slice itself, judged by a fresh Fable 5.1 context, provided at least one pass and the slice's budget remain. Otherwise the loop exits STOPPED_AT_LIMIT with the slice named. The loop never fakes a pass because it ran out of rungs.
- MUST treat a missing or malformed verdict as JUDGE_ERROR, which is never a failed attempt. Re-run the verdict once in a fresh judge context. A second JUDGE_ERROR stops the slice, and the loop reports STOPPED_AT_LIMIT with the judge failure named. In the reference build the workflow script turned an empty verdict into a fail, so a judge error could have cost a retry or a promotion.
- MUST treat these counts as design defaults until the run logs say otherwise: retry once, one effort step up, because every retry in the reference build passed once the weakness was in the brief (at an effort already held at xhigh), and the claude.dev post puts effort before model; xhigh as the retry ceiling, because the post keeps max for a single session; every rung in order, so the run log can attribute a fix to one rung and cost per completed slice stays comparable across runs; cap two, because three rungs on one brief is promotion churn; one brief fix, so the cycle is bounded by the rule; demote after two clean passes, because one clean pass is luck; budgets per attempt of 40K, 90K, and 150K tokens by slice type, sized around the reference build's 80K-to-90K average per call, halved for the smallest slices and raised for hard reasoning. Change them from evidence in the run logs.
- MUST keep the best failed attempt. A failed attempt is recorded with its work, its scores, and its cost, and the promoted rung starts from it. The loop never ships work worse than the best attempt it already has. The incumbent stays in the candidate set.
- MUST log every promotion with slice, from rung, to rung, the weakest criterion, the self-score, and the independent score. A promotion nobody can see is a cost nobody can explain. A promotion made before a brief check fires stays in the log with its cost, tagged as superseded by the brief fix; it still counts toward the cost per completed slice and no longer counts toward the cap.
- MUST NOT promote inside a campaign whose judge compares attempts across history. A replay-scored search tree, a tuning run, anything where attempt twelve is judged against attempts one to eleven: swap the worker there and the history stops predicting the future. Freeze the worker for that campaign, promote between campaigns, and test a different rung as a new campaign. The tuning campaign behind this skill's numbers learned this the expensive way.
- MUST demote deliberately. A slice type that clears the bar on first attempt at a rung and effort, twice in a row, starts one step lower next time: effort first, then the rung (Opus 5.5 at high drops to Opus 5.5 at medium before it drops to Sonnet 5). A slice type that needed a promotion starts on the rung and effort it passed at. The ladder learns from the run logs.
- MAY run a calibration probe: one slice started one step below its default (effort first, then the rung), judged exactly like any other, with the promotion rule live. It is the fast way to learn a rung without waiting for two clean passes, and the tuning campaign ran the same move as a `calibrate` step before freezing its worker. Log it as a probe, and count its cost per completed slice like any other.
- MUST keep the two senses of "up" apart. **Promotion** moves a slice up the model ladder within a loop. **Graduation** moves a trusted loop up the run methods, from a prompt to `/loop` to `/schedule`. One is about a model, the other is about trust.

### Three Ways to Run One

- MUST separate the goal from the mechanism. Every loop starts with the bar for done (the judge). Then it runs one of three ways.
- MUST know the three ways: (1) **a prompt**, write the loop protocol into a single prompt and the model loops itself to the bar with no command needed; (2) **`/loop`**, run a prompt on repeat until it clears the bar, leave the interval off and it self-paces; (3) **`/schedule`**, run it on a cadence, unattended, a cloud agent on a timer working while you sleep.
- MUST treat amplifiers as separate from the three ways. `workflow` and multi-agent fan-out spread the work across many agents; `ultrathink` and effort reason deeper on the hard step; the ladder picks the engine per slice. Amplifiers make a loop work better.
- MUST match the way to the trust level. Start as a prompt or attended `/loop`, watch it run, then graduate a trusted loop to `/schedule` and walk away.

### The Loop and Your Other Skills

- MUST treat the loop as a meta-skill. There is nothing to install. The loop protocol is a skill that lives alongside your other skills, and Claude knows from their descriptions when to loop and which skills to bring into each pass.
- MUST split the work cleanly: your other skills handle what to do (each carries a method and its own checkpoints, and Claude picks the one a pass needs, or you name it); this skill handles keep going until it is real (self-correct, verify, fix, go again).
- MUST claim the three payoffs when this is the point: **better routing** (each pass picks the right skill for that step, where a plain Ralph loop reruns one flat prompt), **compounding context** (every pass pulls richer, more personal context as your project folders and run logs grow with the business), and **cleaner stops** (tie "done" to your skills: every skill named in the criteria reports green and the checks pass).

### Stopping Conditions

- MUST define the stop before the start. The exit condition is the criteria clearing the bar on the independent judge.
- MUST tie "done" to your skills when the criteria name them: the loop only prints FINAL when every named skill-judge clears its threshold on the independent score. That is a stopping condition you can defend.
- MUST set a limit alongside the bar so a loop cannot run forever: a pass cap, a budget, or a wall-clock. If the loop hits the limit before the bar, it stops and reports the gap honestly. A faked pass is a failed loop.
- MUST report the exit state plainly: FINAL with the final scores, or stopped-at-limit with the weakest remaining criterion named, plus every promotion the run made.

### When to Loop, and When Not

- MUST loop when there is a checkable bar, the task is bounded, and iteration improves the work: drafting to a quality gate, code to a passing test, a deliverable to a scorecard, research to a coverage target.
- MUST NOT loop without a judge. A loop with no honest way to score itself drifts, and it will happily call bad work done.
- MUST NOT loop an irreversible or outward-facing action on autopilot. Sending, publishing, deleting, and spending belong behind a human on the exit. Keep the drafting in the loop and the send with a human.
- MUST watch for the seven loop failure modes and name them when seen: **soft passing** (VERIFY inflates scores to exit early), **gaming the judge** (optimizing the metric and leaving the work behind), **runaway** (no limit, looping past the point of return), **self-dealing** (the loop's own cost sits inside its own score, so it wins by doing less of the work that makes it better), **the rubber stamp** (the worker judges itself, or the judge sits on the worker's own rung or below, the top of the ladder excepted, so the gate opens on nothing), **promotion churn** (a broken brief is sent up the ladder rung by rung, and each rung fails the same way at a higher price), and **inherited effort** (a delegate runs at the orchestrator's session effort because the call left effort out, so the log and the bill disagree). Each has a fix: harden the criteria, harden the judge, set a limit, take the loop's own consumption out of the reward, separate and rank the judges, fix the brief before the model, set effort on every call and read it back from the transcript.

### Logging and Pricing

- MUST write the delegates' log lines on their behalf, into the run log. A delegate that applied a skill counts as the orchestrator applying it. Keep the run log with the output: it names every rung used and every promotion made, and the next run reads it to choose its starting rungs. Delegates dropping their log lines is expected. The orchestrator catching it is required.
- MUST price a delegated run with `scripts/cost_by_class.py` and carry cost per completed slice, contexts opened, and the effort each call actually ran at into the run log. It counts each message once; summing every transcript line counts a message once per content block, which is how the reference build's own record reached $88.51 for delegation work that cost $38.36.

## Validation Checkpoints

Before calling a loop well-formed:
- [ ] Success criteria written before the run, strict, and stated in scorable terms.
- [ ] At least one incorruptible judge in the criteria (a test, a compile, a scorecard, a named skill), beyond "reads well."
- [ ] The four moves present: PLAN one step, DO produce-or-improve, VERIFY 1 to 10 with weaknesses named, DECIDE on the floor, on an independent score.
- [ ] The exit is a hard gate (every criterion 8+ on the independent judge), and each pass fixes the weakest prior score first.
- [ ] A limit is set (pass cap, budget, or wall-clock) so the loop cannot run forever.
- [ ] The run method (prompt / `/loop` / `/schedule`) matches the trust level; amplifiers, if used, stay additive.
- [ ] Irreversible or outward-facing steps are behind a human on the exit.
- [ ] If criteria name skills, "done" is tied to those skill-judges clearing their thresholds.
- [ ] Every delegated slice has a six-field brief (task slice, criteria slice, rung and effort, budget, inputs, return shape) and a starting rung chosen from the run logs or the defaults.
- [ ] The gate on every pass opens on a score from a context other than the one that did the work; for delegated slices that judge sits one rung up or higher, or is a machine check; no self-score opens a gate.
- [ ] Delegates are fenced: they return work, the orchestrator writes it after the verdict, and the fenced files are hash-checked before scoring.
- [ ] The promotion rule is stated in the run (retry once, one effort step up, with the weakness named, then one rung up at the retry's effort, every rung in order, brief check on the promoted rung before its retry, cap two, one brief fix) and every promotion is logged with both scores.
- [ ] Every delegated call sets its model and effort, and the run log shows the effort the transcript recorded.
- [ ] Read slices start on Haiku 4.5 and write slices on Sonnet 5 or above, unless the run logs say otherwise.
- [ ] Every model judge sits on the cheapest rung the advisor rule allows, at high effort, and reads the criteria slice, the work, and only the references the criteria name.
- [ ] Machine checks ride in the brief, and delegates run them on a scratch copy.
- [ ] A missing verdict is logged as JUDGE_ERROR and re-run, and it does not count as an attempt.
- [ ] The run is priced with `scripts/cost_by_class.py`: contexts opened and cost per completed slice, each message counted once.
- [ ] The run log carries self-score beside independent score for every delegated pass, and names every rung used.
- [ ] The run log is kept with the output, including the delegates' log lines written on their behalf.

## References

### Core
- `references/loop-protocol.md`: the four moves in depth, the copy-paste protocol anatomy, and the LOOPS 101 worked example
- `references/the-judge.md`: success criteria as an incorruptible judge, the Ralph Wiggum technique, skills-as-judges, judge separation, and why VERIFY honesty is the whole game
- `references/three-ways-to-run.md`: a prompt vs `/loop` vs `/schedule`, the amplifiers (workflow, ultrathink, effort, the ladder), graduation, and matching the method to trust
- `references/loop-with-other-skills.md`: the loop as a meta-skill alongside your other skills, the clean split between them, and the three payoffs (better routing, compounding context, cleaner stops)
- `references/failure-modes.md`: soft passing, gaming the judge, runaway loops, self-dealing, the rubber stamp, promotion churn, and when to keep a task out of a loop, each with a fix
- `references/model-ladder.md`: the four rungs with IDs, prices, context windows, effort settings, the effort-before-rung escalation path, read and write starting points, the cost of a fresh context, and the cost-per-completed-slice rule
- `references/delegation-and-promotion.md`: the six-field brief, the return shape, the fence, judge separation and the advisor rule, the promotion rule with worked scenarios, demotion, the calibration probe, and the brief check
- `references/loop-library.md`: four ready-to-run loops (drafting to a quality gate, code to a passing test, research to a coverage target, a recurring ops ritual to a checklist), each with its judges and judge rungs, slices with starting rungs, a limit and run method, and the step that stays behind a human

### Defaults and Spec
- `references/loop-defaults.toml`: every default in one file: the orchestrator's effort, the promotion counts, the judge rules, starting rungs and budgets by slice type, and the priced ladder
- `references/loop-spec.schema.json`: a spec, in JSON Schema style, of a loop's inputs and outputs (task, criteria with judges and thresholds, run method, amplifiers, orchestrator, delegation slices, promotion counts, limit), with the outcome words as enums

### Templates
- `templates/loop-prompt.md`: the copy-paste loop protocol, fill the two brackets and run
- `templates/success-criteria-worksheet.md`: write strict criteria, pick your skill-judges, and name the judge rung for each, before the run
- `templates/delegation-brief.md`: the six-field brief a delegate receives and the return shape it sends back
- `templates/loop-run-log.md`: log each pass, each delegation, both scores, each promotion, and the FINAL state

### Scripts
- `scripts/cost_by_class.py`: prices a loop from its transcripts, counting each message once: cost by token class, role, and rung; the effort each call ran at; contexts opened and cost per completed slice

## Workflows

### Build-a-Loop Workflow
When turning a task into a loop:
1. Route the task: name the skills that belong in each pass, or let Claude pick them from the skill descriptions
2. Write the success criteria strict and name the skill-judges (`templates/success-criteria-worksheet.md`)
3. Wrap the criteria in the loop protocol (`templates/loop-prompt.md`), set the limit, pick the run method
4. Harden the VERIFY step so scores are honest: the gate score comes from a separate context, and the judges are ranked (`references/the-judge.md`)

### Skill-as-Judge Workflow
When "done" should be tied to your skills:
1. Decide which skills are the judges (your style-guide skill, a claims check, a logic check, your brand or design skill, a reader-benefit scorecard)
2. Run each named skill as a scored criterion, in a context other than the one that did the work
3. Print FINAL only when every named skill-judge clears its threshold on the independent score

### Delegated-Loop Workflow
When a loop is big enough to hand slices to cheaper rungs:
1. Cut the DO step into slices, each with its criteria subset, and pick a starting rung and effort for each from the run logs or the defaults (read slices on Haiku 4.5, write slices on Sonnet 5 or above)
2. Write one six-field brief per slice (`templates/delegation-brief.md`)
3. Run the slices in parallel through a workflow with the promotion rule in the script (`references/delegation-and-promotion.md`)
4. Judge every slice in a separate context on the cheapest rung the advisor rule allows, apply the promotion rule, log both scores and every promotion
5. Record cost per completed slice (`scripts/cost_by_class.py`) so the next run starts each slice on the right rung and effort

### Unattended-Loop Workflow
When a trusted loop should run without you:
1. Confirm the bar is incorruptible and a limit is set
2. Keep irreversible steps behind a human on the exit
3. Put the loop on a cadence with `/schedule`
4. Report FINAL or stopped-at-limit with the weakest remaining criterion named

## Your Context

Before building a loop, gather from your own notes and project folders:
- Which recurring tasks are candidates to hand to a loop (bounded, checkable, high frequency)
- The quality bars and scorecards that already exist and can serve as judges
- What must stay behind a human on the exit (sending, publishing, spending, deleting)
- Existing scheduled or automated work that a loop could absorb or replace
- The rung and effort each recurring slice type last cleared on, so the ladder starts from history, with the top rung as the fallback
