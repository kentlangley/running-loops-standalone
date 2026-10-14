# Template: Success Criteria Worksheet

Write the judge before you run the loop. A loop is only as good as its definition of done. Fill this out first, then paste the criteria into the loop prompt.

## 1. The task (one line)

> <the single thing the loop will carry to done>

## 2. What "done" actually looks like

List the outcomes: what exists when the loop ends. An activity ("run the tests", "draft the copy") is a step, and steps do not go in this table. Each one must be scorable 1 to 10. Name where each judge runs: a machine check, a rung on the ladder, or a human.

| # | Criterion (what done looks like) | Judge (how it is scored) | Judge rung | Threshold |
|---|----------------------------------|--------------------------|------------|-----------|
| 1 | | | | 8 |
| 2 | | | | 8 |
| 3 | | | | 8 |
| 4 | | | | 8 |

Judge types, strongest first:
- **Machine-checkable:** a test, a compile, a linter, a schema, a numeric threshold.
- **Skill-as-judge:** a named skill run as a scored criterion (your style-guide skill, a claims check, a logic check, your brand or design skill, a reader-benefit scorecard).
- **Scorecard:** a rubric with named dimensions.
- **Human bar:** "the author would be proud to publish this."

Judge rungs: `machine`, `sonnet`, `opus`, `fable`, `human`. A model judge runs one rung up or higher from the worker whose slice it grades; Fable 5.1 work is judged by a fresh Fable 5.1 context. Haiku 4.5 never judges, because no worker sits below it.

## 3. The incorruptible-judge check

- [ ] At least one criterion is something that cannot fake a pass (machine-checkable or a named skill with its own checkpoints).
- [ ] No criterion is just "reads well" or "looks good" with nothing behind it.
- [ ] The score that opens FINAL comes from a context other than the one that did the work (a machine check, a fresh sub-agent, or the human on an attended run). No self-score opens a gate.
- [ ] Every model judge sits one rung up or higher from its worker (Fable 5.1 work: a fresh Fable 5.1 context). Machine outranks model; model outranks self-score.

## 4. The slices (if DO is delegated)

| Slice | Criteria it is scored on | Starting rung | Effort | Budget |
|-------|--------------------------|---------------|--------|--------|
| | | | | |
| | | | | |

Starting rung and effort with no history: read slices on Haiku 4.5 (Sonnet 5 at low above 200K of input); mechanical writes on Sonnet 5 at low, judgment writes on Sonnet 5 at medium, hard reasoning on Opus 5.5 at high. With history: the cheapest rung and lowest effort that cleared this slice type before, per the run logs. Put each judge on the cheapest rung the advisor rule allows. Write one brief per slice from `delegation-brief.md`.

## 5. The limit (so it cannot run forever)

- Max passes: ____   or   Budget: ____   or   Wall-clock: ____
- Promotions per slice: 2 (the default cap)

## 6. The exit and the guard

- [ ] Exit is FINAL only when the FLOOR across all criteria clears its threshold, on the independent judge. The lowest score is the one that counts; an average hides a failing criterion.
- [ ] Any irreversible or outward-facing step (send, publish, delete, spend) sits behind a human on the exit. An unattended pass has no authority to take it.
- [ ] If this loop is a campaign whose judge compares attempts across history, the worker rung is frozen for the campaign and no promotion runs inside it.

Now paste the filled criteria into `loop-prompt.md` and run.
