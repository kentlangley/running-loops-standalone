# The Loop Protocol

An agent loop is telling the AI to keep working on a task until it is actually done, or it hits a limit you set. The shape is four moves on repeat.

```
PLAN -> DO -> VERIFY -> DECIDE  (and back to PLAN)
```

You hand the agent three things: the **task**, a way to **check its own work**, and permission to **keep going**. Then you stop approving every turn.

## The four moves

1. **PLAN.** State the single next step. One step is the whole plan for this pass. Small steps keep each pass honest and easy to score.
2. **DO.** Produce or improve the work. The first pass creates. Every later pass fixes the weakest thing named in the last VERIFY, even when something else is easier to touch. DO is the move that can be delegated by slice; see `delegation-and-promotion.md`.
3. **VERIFY.** Score each criterion 1 to 10. Be brutally honest. List exactly what is still weak. This step is the entire value of the loop. A flattering VERIFY is a broken loop. The score that opens the gate comes from a context other than the one that did DO: a machine check, a fresh sub-agent, or the human on an attended run. The DO context may self-score to steer the next pass, and that score is logged only. When DO was delegated, the judge sits one rung up or higher.
4. **DECIDE.** If every criterion is 8 or higher on the independent score, print "FINAL" and stop. Otherwise print "ITERATING" and go again, fixing the weakest point first. The gate opens on the floor across all criteria.

## The copy-paste protocol

This is the take-home artifact. Fill the two brackets, paste, and run.

```
TASK
  <the thing you want done>

SUCCESS CRITERIA  (be strict. no soft passes.)
  - <what "done" actually looks like>
  - <bring in more skills or agents where they help>

LOOP PROTOCOL  repeat every turn:
  1. PLAN    state the single next step.
  2. DO      produce or improve the work.
  3. VERIFY  score each criterion 1-10. be brutally
             honest. list exactly what is still weak.
  4. DECIDE  every criterion 8+ ?  print "FINAL" and stop.
             otherwise print "ITERATING" and go again,
             fixing the weakest point first.

RULES
  - never call it done until every criterion is 8 or higher.
  - each pass fixes the weakest score from the last VERIFY.
  - do not ask questions. make a sensible assumption,
    note it, and keep going.
  - the score that opens FINAL comes from a context other
    than the one that did the work: a machine check, a fresh
    sub-agent, or the human on the exit. self-scores steer
    ITERATING passes and are logged; they never open the gate.
  - Fable 5.1 orchestrates. Hand slices of DO to Haiku 4.5,
    Sonnet 5, or Opus 5.5 by a six-field brief, with the
    model and the effort set on every call: read slices on
    Haiku 4.5, write slices on Sonnet 5 or above. Judge every
    delegated slice in a separate context on the cheapest
    rung the advisor rule allows (one rung up or higher, or
    a machine check), at high effort.
  - if a delegated slice fails the judge: retry once on the
    same rung one effort step up with the weakness named,
    then promote one rung at that effort, every rung in
    order. on the promoted rung, after its first failure and
    before any retry there, if the weakest criterion id
    matches the id of the attempt that triggered the
    promotion, fix the brief, restart on the original rung
    and effort, log it; once per slice. cap two promotions
    per slice. a missing verdict is JUDGE_ERROR: rerun it
    once; it does not count as a failure. log every
    promotion.

Begin. Run the loop until FINAL.
```

The brackets are the only thing you fill in. The VERIFY step is your judge, turned into a rule, and the gate opens on a score from outside the context that did the work.

## Anatomy: why each part is there

- **TASK** keeps the loop pointed at one thing. A loop with two tasks is two loops.
- **SUCCESS CRITERIA** is the judge. Strict, scorable, no soft passes. This is the part that makes or breaks the loop. See `the-judge.md`.
- **LOOP PROTOCOL** is the engine: plan, do, verify, decide, on repeat.
- **RULES** keep it moving without you. Never call it done early. Always fix the weakest score first. Settle every open question with a noted assumption and keep going. The gate line says whose score opens FINAL. The two ladder lines say who does the work, who grades it, and what happens when the grade is low; they cost nothing until a slice is delegated.
- **Begin.** is the go signal. The loop runs until FINAL or until it hits a limit.

## Worked example: LOOPS 101

A real loop with every field filled in. Read one essay, produce a better second version, and let named skills be the judges.

```
# LOOPS 101

TASK:
  read this article, then create a second, better version:
  <path or URL to the source>

SUCCESS CRITERIA (be strict, no soft passes):
  - a reader-benefit scorecard scores 8 or higher
  - <your style skill> did its job
  - a claims check ran, every claim verified or noted
  - a logic check ran, every argument sound
  - the author would be proud to publish this in their name

LOOP PROTOCOL, repeat every turn:
  1. PLAN    state the single next step.
  2. DO      produce or improve the work.
  3. VERIFY  score each criterion 1-10, brutally honest.
             list exactly what is still weak.
  4. DECIDE  every criterion 8+ ?  print "FINAL" and stop.
             else print "ITERATING", go again,
             fixing the weakest point first.

RULES:
  - never call it done until every criterion is 8+.
  - each pass fixes the weakest score from the last VERIFY.
  - do not ask questions. make a sensible assumption, keep going.
  - the score that opens FINAL comes from a context other than
    the one that did the work: a machine check, a fresh
    sub-agent, or the author reading the final draft.

Begin. Run the loop until FINAL.
```

Notice the criteria do not say "make it good." They name skills as the judges. Each pass routes into those skills, scores against them honestly, and only prints FINAL when all of them clear 8 on the independent score. That is a loop whose stopping condition is tied to your skills. See `loop-with-other-skills.md`.

To run LOOPS 101 with the ladder, the DO step becomes slices: a Sonnet 5 draft at medium (a write slice) and a Haiku 4.5 claims-extraction table for the claims check (a read slice), each judged on the cheapest rung the advisor rule allows, with a fresh Fable 5.1 context scoring all five criteria at the gate. Same criteria, same gate, cheaper passes.
