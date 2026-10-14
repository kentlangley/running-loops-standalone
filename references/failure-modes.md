# Failure Modes, and When Not to Loop

A loop is powerful because it runs without you. That is also how it goes wrong. Watch for these, name them when you see them, and apply the fix.

## The seven loop failure modes

1. **Soft passing.** The VERIFY step inflates scores to exit early. The loop prints FINAL on work that is not there yet.
   - Fix: harden the criteria so a soft pass is obviously wrong. Require every VERIFY to name the specific weakness alongside a number. Add an incorruptible judge that cannot be talked into a pass.

2. **Gaming the judge.** The loop optimizes the metric and leaves the work behind. It raises the score the cheap way (padding, keyword-stuffing, teaching to the test) without improving the real outcome.
   - Fix: add a judge that measures the real outcome directly. Keep the human bar in the set. If a machine judge can be gamed, pair it with one that cannot.

3. **Runaway.** No limit, so the loop keeps going past the point of return, burning budget or drifting away from the task.
   - Fix: set a limit alongside the bar. A pass cap, a budget ceiling, or a wall-clock. When the loop hits the limit before the bar, it stops and reports the gap honestly. A faked pass is a failed loop.

4. **Self-dealing.** The loop's own token consumption sits inside its own scorecard. An agent told to maximize a yield figure can raise it by researching less, raising the reward number while draining the factory's real output. This is the failure mode that a factory-wide efficiency metric invents by itself, and it differs from gaming the judge: the metric is satisfied honestly and the wrong thing is optimized.
   - Fix: separate the reward from the published number. Reward on verified value per token at the experiment level, over minutes to hours. Advance on a slower lane-level contribution number. Keep the company-wide figure as a veto gate only; the policy trains on the experiment-level and lane-level numbers, and the company-wide figure stays out of the gradient. Never let the loop hold the pen on the map from quality improvements to dollars, and keep a human on any step that commits new spend, since spending is outward-facing and hard to reverse.

5. **The rubber stamp.** The worker grades its own pass, or the judge sits on the worker's own rung or below (the top of the ladder excepted), so the gate opens on nothing. A content-drafting run measured it: drafters scored themselves two to four points above the independent judge. A rubber stamp looks like a healthy loop right up to the fresh reader.
   - Fix: separate the judge from the worker (a fresh context, or a machine check) and run it one rung up or higher (Fable 5.1 work: a fresh Fable 5.1 context). Rank the judges so the machine outranks the model and the model outranks the self-score. Log both scores and read the gap. See `the-judge.md`.

6. **Promotion churn.** A delegated slice fails, gets sent one rung up, fails the same way, gets sent up again. Each rung fails on the same named weakness at a higher price, because the fault is in the brief, and a bigger model reads the same brief. In a tuning campaign (a replay-scored self-improvement loop), the worker prompt made every worker read the whole history; no rung on any ladder fixes that prompt.
   - Fix: the brief check. On the promoted rung, after its first failed attempt and before any retry there, compare the weakest criterion id with the id of the attempt that triggered the promotion. A match means rewrite the brief and restart on the slice's original starting rung and effort. Cap promotions at two per slice so churn has a ceiling even when the check is missed. See `delegation-and-promotion.md`.

7. **Inherited effort.** A delegated call leaves effort out, so the delegate runs at the orchestrator's own session effort instead of the effort the brief meant to set. The run log says one thing and the bill says another. The reference build (a measured run that rebuilt this skill's own protocol with the loop, every context priced from its transcript) is the evidence: a Workflow `agent()` call without `effort` took the session's xhigh, so every Sonnet 5, Opus 5.5, and Fable 5.1 worker ran at xhigh while the run log recorded "default" for each of them.
   - Fix: set effort on every delegated call, with no exceptions. `scripts/cost_by_class.py` reads back the effort the transcript actually shows; the run log records that effort beside the effort the brief asked for, so a silent inheritance shows up as a mismatch instead of hiding in the total.

## The slow one: history growth

This is a failure mode of the inputs. A multi-round delegation that hands each worker everything that came before grows by a round's worth of tokens every round. Round one runs clean. It fails on round three, as capped worker errors that score nothing and cost full price, and on Haiku 4.5 it fails as a context overflow. Caps alone do not catch it early because the early rounds are cheap.

- Fix: write a digest of the history. The orchestrator writes one line per prior attempt and the brief carries the digest. Treat the digest as a required part of any multi-round delegation.

## When to loop

Loop when all three hold:

- There is a **checkable bar** (a test, a compile, a scorecard, a named skill).
- The task is **bounded** (it has a finish).
- **Iteration improves it** (each pass can make the work better).

Good fits: drafting to a quality gate, code to a passing test, a deliverable to a scorecard, research to a coverage target, a recurring ops ritual to a checklist.

## When not to loop

- **No judge.** A loop with no honest way to score itself has no way to converge: it drifts, and it will happily call bad work done. Build the judge first, or do not loop.
- **Irreversible or outward-facing actions on autopilot.** Sending, publishing, deleting, and spending belong behind a human on the exit. Loop the drafting, gate the send.
- **Genuinely open-ended work.** If "done" cannot be defined, a loop has nothing to converge on. Do the divergent thinking first, define the bar, then loop the convergence.
- **A one-shot task.** If the work is done in a single pass and there is nothing to improve, a loop is overhead. Just do it.
- **A score that contains the loop's own cost.** If the number the loop is judged on rises when the loop spends less on itself, it will learn to spend less on itself. Take the loop's own consumption out of the reward first, or do not loop. See self-dealing above.

## When not to promote

- **Inside a campaign whose judge compares attempts across history.** A replay-scored search tree, a tuning run, an autoresearch campaign: attempt twelve is judged against attempts one to eleven. Swap the worker mid-campaign and the history stops predicting the future. Freeze the worker for the campaign, promote between campaigns, test a different rung as a new campaign.
- **Before the brief check.** See promotion churn above.
- **Past the cap.** Two promotions per slice, then the orchestrator takes the slice or stops at limit. A promotion nobody can see is a cost nobody can explain, so every one is logged.

## The honest exit

Every loop ends one of two ways, and both are stated plainly:

- **FINAL**, with the final scores, when every criterion cleared its threshold on the independent judge.
- **Stopped at limit**, with the weakest remaining criterion named, when a limit was hit before the bar.

Both exits also report every rung used and every promotion made. A loop that hides its exit state is back to soft passing. The report is part of the loop.
