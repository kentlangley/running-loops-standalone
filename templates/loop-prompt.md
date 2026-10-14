# Template: Loop Prompt

The copy-paste loop protocol. Fill the two brackets, paste it into the agent, and run. This is the whole take-home artifact of this skill.

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

## How to fill it

- **TASK:** one thing. If you have two, run two loops.
- **SUCCESS CRITERIA:** strict and scorable. Name skills as judges where you can ("your style-guide skill did its job", "a claims check ran, all claims verified"). At least one criterion must be an incorruptible judge (a test, a compile, a scorecard, a named skill). See `../references/the-judge.md`.
- Add a **limit** in the rules if you are running unattended: "stop after N passes" or "stop at <budget>."
- The last three lines in RULES stay in every loop. The first applies to every run: on an attended prompt loop the human on the exit is the independent score for FINAL; on `/loop` or `/schedule` it is a machine check or a fresh sub-agent. The ladder lines cost nothing until a slice is handed off. When one is, write the brief from `delegation-brief.md`.

## Optional add-ons

- Run it with `/loop` to rerun until the bar clears; leave the interval off to self-pace.
- Run it with `/schedule` to run unattended on a cadence, once the loop is trusted.
- Layer `workflow`, multi-agent fan-out, or `ultrathink` on the hard pass. Raise effort before you raise the rung, and set it on every delegated call. See `../references/three-ways-to-run.md` and `../references/model-ladder.md`.
