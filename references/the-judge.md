# The Judge

A loop is only ever as good as its definition of done. The success criteria are the judge. Get the judge right and the loop can run itself to the finish. Get it wrong and the agent just talks to itself until it feels finished.

The thesis of the whole method: you do not need to be right the first time. You need to know when you are right.

## The Ralph Wiggum technique

Named by Geoffrey Huntley after the Simpsons kid who is cheerfully relentless no matter how many times he faceplants: run an AI agent in a loop until it succeeds. Plain repetition does the work. Each failure feeds the next attempt.

> "Run an AI agent in a loop until it succeeds. No elegance required. Just repetition. Each failure feeds the next attempt."

One builder shipped a roughly $50,000 client build for about $297 in compute, just by looping. The trick is an incorruptible judge.

In the loop that first proved the method to this skill's author, the judge was Lean 4, a math prover: proofs compile or they do not. No negotiating, no hallucinating. That is why the loop worked. The judge could not lie.

## Incorruptible judges

An incorruptible judge is something that cannot fake a pass. Ranked by strength:

1. **Machine-checkable.** A test suite, a compile, a linter, a schema validation, a numeric threshold. Strongest. Trust these unattended.
2. **Skill-as-judge.** A named skill run as a scored criterion: your style-guide skill, a claims check, a logic check, your brand or design skill, a reader-benefit scorecard. Strong, because the skill has its own checkpoints the loop must clear. See `loop-with-other-skills.md`.
3. **Scorecard.** An explicit rubric with named dimensions and thresholds. Good, as long as the dimensions are concrete.
4. **Human bar.** "The author would be proud to publish this in their name." Keep one in the set when work ships in someone's name. It catches what the mechanical judges miss. Weakest on its own, so pair it with harder judges.

The rule: at least one judge in every loop must be something that cannot lie about whether the work is done.

## Skills as judges

This is what makes a skill-routed loop different from a plain Ralph loop. Replace "reads well" with the named skills that define done:

- weak: "the copy is good"
- strong: "your style-guide skill did its job, and a reader-benefit scorecard scores above the line"

- weak: "the claims are accurate"
- strong: "a claims check ran, every claim verified or flagged; a logic check ran, every argument sound"

Each named skill becomes a criterion scored every pass. The loop routes into the skill and applies its checkpoints; the score that opens the gate comes from an independent context (see the next section), and the loop's own score is logged beside it. FINAL only prints when all of them clear the threshold on the independent score.

## Judge separation

The worker never grades its own pass as the only score. Telling the worker to be brutally honest, and leaving it there, falls short. Two measured runs show why: a content-drafting run logged drafters scoring their own subjects two to four points above the independent judge, and the fresh-reader judge found the most real defects. An audit run's adversarial judges caught three factual defects after the self-scored gate had opened.

So the judge sits in a separate context. Five rules:

- **A fresh context reads the work.** The whole work, and the criteria slice. The worker's self-score is withheld from the judge; the orchestrator compares the two after the verdict and logs both. A self-score never opens the gate.
- **The advisor rule, one rung up.** Haiku 4.5 work is judged by Sonnet 5 or above, Sonnet 5 work by Opus 5.5 or above, Opus 5.5 work by Fable 5.1, and Fable 5.1 work by a fresh Fable 5.1 context, the one exception at the top of the ladder. A machine check may judge any rung. The reviewer is at least as capable as the one reviewed, and here that means a rung up. The full ladder is in `model-ladder.md`.
- **The cheapest rung the advisor rule allows, at effort high.** Haiku 4.5 read work goes to a machine check for every criterion that has one and to Sonnet 5 for the rest (a slice whose criteria are all machine-checked spends no model verdict); Sonnet 5 work to Opus 5.5; Opus 5.5 work to Fable 5.1. Effort is set on the call, high. In the reference build (a measured run that rebuilt this skill's own protocol with the loop, every context priced from its transcript) every verdict ran on Fable 5.1 regardless of what it judged; a Fable 5.1 verdict averaged $0.90, and the same tokens re-priced on Opus 5.5 come to $0.38, so judging the Sonnet 5 attempts on Opus 5.5 instead of Fable 5.1 would have cut the reword pass from $2.18 to $1.40 per completed slice (over the seven reword slices that shipped; the eighth ran the ladder out). The gate that prints FINAL still stays with a fresh Fable 5.1 context.
- **Ranked judges.** A machine check outranks a model judge, and a model judge outranks a self-score. When they disagree, the stronger one wins. A failed machine check fails the slice whatever the model judge said, and no model verdict is spent on it. A pass/fail judge scores 10 on a pass and 1 on a fail, so the floor rule works unchanged. When a slice promotes, its judge climbs with it and stays one rung up.
- **Every loop, delegated or single-context.** A prompt loop that runs in one context may self-score its ITERATING passes; that is how a prompt loops itself. FINAL prints only when a machine check, a fresh sub-agent, or the human on an attended run confirms the floor. A slice the orchestrator takes itself is judged by a fresh Fable 5.1 context.

The gap between self-score and independent score is data. Above two points on the same criterion, either the brief was unclear or the worker is soft passing. Both change the next brief. See `delegation-and-promotion.md` for what happens when the independent judge says no.

## The lean judge brief

Every extra file in a verdict is paid for again, because a fresh context writes its whole opening prompt to the cache before it reads a word of the work. So the judge's brief stays lean: the criteria slice it is scoring against, the work in full (never a summary), and only the reference material each criterion names, SKILL.md for a consistency criterion, the original file for a meaning criterion. Leave out the loop's history and any file no criterion in the slice names. A judge reading files nobody asked it to check pays for each of them again in every verdict, for nothing the score uses.

## JUDGE_ERROR

A missing or malformed verdict is JUDGE_ERROR. It never counts as a failed attempt. Re-run the verdict once, in a fresh judge context. A second JUDGE_ERROR stops the slice, and the loop reports STOPPED_AT_LIMIT with the judge failure named as the cause. In the reference build the workflow script turned an empty verdict into a fail, which could have cost the slice a retry or a promotion it did nothing to deserve. Keeping the two counters separate is the fix: a broken judge should never burn a worker's budget.

## Testing the judge

A judge you plan to trust unattended has been tested first. A tuning campaign (a replay-scored self-improvement loop) trusted its judge only after three checks, and it found a real corruption on the way: the first build let a candidate patch the scoring function and score J = 9 x 10^8, marked valid.

- **Unreachable.** The thing being scored cannot touch the scorer. In code that means a separate process and a static gate on imports. In a loop it means the worker never edits the criteria, the verify script, or the run log.
- **Deterministic.** Two runs, two contexts, same work, same score.
- **Leak-proof.** Scramble what the judge should not see and the verdict does not move.

Run these once before a loop graduates to `/schedule`.

## Why VERIFY honesty is everything

The DECIDE gate can only be as honest as the VERIFY that feeds it. Two ways VERIFY goes wrong:

- **Soft passing.** The agent inflates scores to exit early. Fix: harden the criteria so a soft pass is obviously wrong, require the specific weakness to be named alongside the number, and put the score that opens the gate in a separate context.
- **Gaming the judge.** The agent optimizes the metric at the expense of the work (keyword-stuffing to raise a copy score). Fix: add a judge that measures the real outcome, and keep the human bar in the set.

A brutally honest VERIFY that names exactly what is still weak keeps a loop improving and stops it from declaring victory early. See `failure-modes.md`.
