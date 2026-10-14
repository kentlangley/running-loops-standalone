# Loop Library

Four loops you can paste into the loop prompt and run, with Fable 5.1 orchestrating and every slice starting on its default rung and effort, both set on the call. Each one names its judges and their rungs, sets a limit, and leaves the outward-facing step with you.

## Drafting to a quality gate

### Task

Draft a 900-word newsletter issue on [topic] in the author's voice, ready to send.

### Success criteria

| # | Criterion | Judge | Judge rung | Threshold |
|---|---|---|---|---|
| 1 | Zero em or en dashes, and 800 to 1,000 words | Script: counts U+2013 and U+2014, runs `wc -w` | machine | Pass |
| 2 | `<your style skill>` did its job: voice, varied rhythm, its banned-pattern list clean, one reversal at most | `<your style skill>` checkpoints | opus | 8 |
| 3 | Scores above the line on `<your reader-benefit scorecard>`: it speaks to the reader, names what they get, why it matters, and why now | `<your reader-benefit scorecard>` | opus | 8 |
| 4 | Every factual claim in the draft is listed with a source or flagged | a claims check, reading the draft and the list | sonnet | 8 |
| 5 | The author would be proud to send it under their own name | The author, at FINAL | human | 8 |

### Slices

| Slice | Criteria | Starting rung | Effort | Budget |
|---|---|---|---|---|
| Draft the issue from the topic brief and the last three issues | 1, 2, 3 | Sonnet 5 | medium | $2.00 |
| List every factual claim with its source, or flag it | 4 | Haiku 4.5 | none (thinking budget) | $0.50 |

### Limit and run method

Six passes or $6, whichever comes first. Run it as a prompt, attended: you are the independent score on criterion 5, and FINAL waits for you.

### Behind a human

Sending and publishing. The loop stops at a finished draft and a claim list. You clear the flagged claims and press send.

## Code to a passing test

### Task

Make the failing tests in [module] pass without editing any test file.

### Success criteria

| # | Criterion | Judge | Judge rung | Threshold |
|---|---|---|---|---|
| 1 | The full suite passes | `npm test` (or your test command) exits 0 | machine | Pass |
| 2 | No test file changed | Hash of `tests/` matches the hash taken before the run | machine | Pass |
| 3 | Lint and type check are clean | `npm run lint` and `npx tsc --noEmit` exit 0 | machine | Pass |
| 4 | The root cause is named, with the failing line and a one-step repro | Code review: rerun the repro, read the named line | fable | 8 |
| 5 | The diff fixes that cause, stays inside [module], and adds no branch written for a test input | Code review of the diff against the diagnosis | opus | 8 |

### Slices

| Slice | Criteria | Starting rung | Effort | Budget |
|---|---|---|---|---|
| Diagnose the failure and name the root cause | 4 | Opus 5.5 | high | $4.00 |
| Write the fix | 1, 2, 3, 5 | Sonnet 5 | medium | $3.00 |
| Clear lint and format errors | 3 | Sonnet 5 | low | $0.50 |

### Limit and run method

Ten passes or $15. Run it with `/loop` and no interval so it self-paces; watch the first run, then leave it, since three of its five judges are machine checks.

### Behind a human

Merging, deploying, and anything that touches production data. The loop runs against a test database and ends on a green branch with a pull request open. You review the diff and merge.

## Research to a coverage target

### Task

Build a grid of [eight named competitors] on price, offer, channel, and proof, every fact sourced, with three findings on top.

### Success criteria

| # | Criterion | Judge | Judge rung | Threshold |
|---|---|---|---|---|
| 1 | Every cell of the 8 by 4 grid holds a fact or reads "not found" | Script counts empty cells, expects 0 | machine | Pass |
| 2 | Every fact carries a source URL, and every URL resolves | Script requests each URL, expects status 200 | machine | Pass |
| 3 | Every fact matches its source page | a claims check, fact and page side by side | opus | 8 |
| 4 | Each finding follows from the grid and cites the cells behind it | a logic check | opus | 8 |
| 5 | The findings read clean and plain | `<your style skill>` checkpoints | opus | 8 |

### Slices

| Slice | Criteria | Starting rung | Effort | Budget |
|---|---|---|---|---|
| Fill one competitor's row from its digested pages, eight in parallel | 1, 2, 3 | Sonnet 5 | low | $1.00 each |
| Write the three findings from the finished grid | 4, 5 | Sonnet 5 | medium | $1.50 |

### Limit and run method

Four passes or $12, with the eight rows fanned out through a workflow and each row's pages digested first so a row fits one attempt. Run it as a prompt first, then `/schedule` it monthly once a run clears FINAL with no promotions.

### Behind a human

Spending. The loop reads public pages only, so buying a report or a data subscription stays with you. So does any pricing move the findings suggest.

## A recurring ops ritual to a checklist

### Task

Every Monday, turn [your checklist] into a one-page ops brief: cash, receivables past 30 days, pipeline movement, and the three decisions the week needs.

### Success criteria

| # | Criterion | Judge | Judge rung | Threshold |
|---|---|---|---|---|
| 1 | Every checklist line is present with a number and its source export | Script matches the brief against the checklist | machine | Pass |
| 2 | Cash ties to the bank export within $1, and pipeline ties to the CRM export total | Script reconciles both | machine | Pass |
| 3 | Every week-on-week move over 10% has a one-line cause | Review of each cause against the exports | opus | 8 |
| 4 | Each of the three decisions follows from the numbers and names an owner | a logic check | opus | 8 |
| 5 | Reads in two minutes: under 400 words, style-guide clean | `<your style skill>` checkpoints | opus | 8 |

### Slices

| Slice | Criteria | Starting rung | Effort | Budget |
|---|---|---|---|---|
| Pull the exports and fill the checklist numbers | 1, 2 | Sonnet 5 | low | $0.60 |
| Explain the moves and draft the three decisions | 3, 4, 5 | Sonnet 5 | medium | $1.50 |

### Limit and run method

Three passes or $3.50 per run. Run it attended as a prompt until four Mondays in a row clear FINAL, then `/schedule` it for Monday at 7 a.m.; a run that stops at the limit reports the gap to you with the weakest criterion named.

### Behind a human

Posting the brief to the team, chasing overdue invoices, and moving money. The loop reads exports and writes one draft. It has no write access to the books or the CRM.

## How to use one

1. Paste the Task line into TASK and the Success criteria table into SUCCESS CRITERIA in `../templates/loop-prompt.md`, then add the limit to RULES.
2. Write one brief per slice from `../templates/delegation-brief.md`. The Criteria column is the criteria slice, Starting rung and Effort fill RUNG AND EFFORT, and Budget covers every attempt, retry, promotion, and judge call on that slice.
3. Log every pass in `../templates/loop-run-log.md`: self-score beside independent score, each promotion, and the exit state.

A pass/fail judge scores 10 on a pass and 1 on a fail, so the floor of 8 holds on every row. Model judges read the whole work in a fresh context and never see the self-score. When a slice fails its judge, the promotion rule runs as SKILL.md states it, and the slice's model judges climb with it to stay one rung above the worker, up to a fresh Fable 5.1 context at the top. Every model judge sits on the cheapest rung the advisor rule allows, at high effort set on the call; the retry on the same rung runs one effort step up. Read slices (the claims list in the first loop) start on Haiku 4.5; every slice whose output lands in the deliverable, including grid rows and checklist numbers, is a write slice and starts on Sonnet 5 or above. These starting rungs and efforts are the no-history defaults. Once your run log shows where a slice type clears, start it there. Before any loop moves to `/schedule`, run the three judge tests in `the-judge.md`, and swap the example commands for your own.
