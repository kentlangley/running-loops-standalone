# running-loops-standalone

A Claude skill that turns any task into a self-correcting agent loop. You set a strict bar for done. The agent plans one step, does the work, scores it against the bar, and goes again until an independent judge says it clears, or until it hits a limit you set.

By [Kent Langley](https://kentlangley.com).

## What it covers

- **The loop.** PLAN, DO, VERIFY, DECIDE, on repeat. The exit is a hard gate: every criterion scores 8 or higher on an independent judge.
- **The judge.** Success criteria written before the run, at least one judge that cannot fake a pass (a test, a compile, a scorecard), and a gate score that comes from a context other than the one that did the work.
- **The model ladder.** Fable 5.1 orchestrates. Opus 5.5, Sonnet 5, and Haiku 4.5 take delegated slices, each with its model and effort set on the call.
- **Delegation and promotion.** A six-field brief for every delegate. A slice that fails its judge retries once, one effort step up, then moves one rung up the ladder, every rung in order, every move logged.
- **Cost.** Price a run by cost per completed slice with the bundled `scripts/cost_by_class.py`, which reads Claude Code transcripts.
- **Three ways to run.** A single prompt, `/loop`, or `/schedule`, matched to how far you trust the loop.

## Install

**Claude Code.** Clone the repo into your skills folder:

```
git clone https://github.com/kentlangley/running-loops-standalone.git ~/.claude/skills/running-loops-standalone
```

Or download `running-loops-standalone-1.0.0.zip` from the [latest release](https://github.com/kentlangley/running-loops-standalone/releases/latest) and unzip it into `~/.claude/skills/`. To use it in one project only, put it in that project's `.claude/skills/` folder instead.

**claude.ai.** Download `running-loops-standalone-1.0.0.zip` from the [latest release](https://github.com/kentlangley/running-loops-standalone/releases/latest) and upload it under Skills in your settings. Use that attached zip. GitHub's "Source code" archives name their folder with the version number, and the skill expects its folder to match its name.

## Start here

Open `templates/loop-prompt.md`, fill in the task and the success criteria, paste it into Claude, and run it. When a loop is big enough to hand pieces to cheaper models, write one brief per piece from `templates/delegation-brief.md` and log each pass in `templates/loop-run-log.md`. For four loops ready to run, see `references/loop-library.md`.

## What's inside

| Path | What it holds |
|---|---|
| `SKILL.md` | The skill: when it triggers, its rules, and the checklist a well-formed loop meets |
| `references/` | The protocol, the judge, three ways to run, failure modes, the model ladder, delegation and promotion, the loop library, the defaults, and the loop spec |
| `templates/` | The loop prompt, the success-criteria worksheet, the delegation brief, and the run log |
| `scripts/cost_by_class.py` | Prices a loop from its transcripts, counting each message once |

## Version

1.0.0. Model names and prices come from Anthropic's model table as of 2026-06-24.

## License

The text and templates are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The script in `scripts/` is licensed under MIT. Both require credit to stay with the work. When you share or adapt this skill, keep this line with it:

> running-loops-standalone by Kent Langley (https://kentlangley.com). Text licensed under CC BY 4.0; scripts licensed under MIT.

Full terms are in [LICENSE](LICENSE).
