# Three Ways to Run a Loop

Separate the goal from the mechanism. Every loop starts with the bar for done, the judge you set in the success criteria. Then you run it one of three ways. Amplifiers are a separate thing you layer on top.

## First: set the goal

The bar for done comes first, always. Write strict success criteria (see `the-judge.md`). Without a bar there is no loop, just an agent talking to itself.

## The three ways

1. **A prompt.** Write the loop protocol into a single prompt (see `../templates/loop-prompt.md`). The model runs the loop itself until it hits the bar. No special command needed. This is the simplest form and the place to start. Effort here is the session's own: whatever was set when the session started, changed only between passes (see below).

2. **`/loop`.** The command that reruns a prompt on repeat until it clears the bar. Leave the interval off and it self-paces, deciding when to go again. Good for a task you want to watch converge without babysitting every turn. Each pass starts fresh from the run log, at the session effort set when the session started and changed only between passes; any delegated call inside a pass still carries its own effort, set on that call.

3. **`/schedule`.** The walk-away version. Runs on a cadence, unattended, a cloud agent on a timer working while you sleep. This is for trusted loops with incorruptible judges, once you have watched them run. Like `/loop`, each pass starts fresh from the run log, at the effort set when the scheduled agent's session starts and holding for the run; every delegated call inside it still sets its own effort.

## Amplifiers

These make loops work better. They sit apart from how you loop, so keep them mentally separate.

- **`workflow` / multi-agent fan-out.** Spreads the work across many agents at once. Useful when a pass has independent sub-tasks, or when you want several independent verifiers on one finding. The fan-out carries the delegation protocol: each agent gets a six-field brief, a separate judge, and the promotion rule written into the script. See `delegation-and-promotion.md`.
- **`ultrathink` and effort.** Reasons deeper on the hard step. The three upper rungs take an effort setting (low, medium, high, xhigh, max); Haiku 4.5 takes a thinking budget. Max stays out of delegated work. Layer it only on the pass that needs the most thinking. Raise effort before you raise the rung. Effort is set per call for every delegate and is never inherited; a Workflow `agent()` call that leaves it out takes the orchestrator's own session effort instead, so set it explicitly every time. The orchestrator's own effort is a different setting: it is fixed when the session starts, high by default and xhigh by choice for a hard loop, and changed only between passes. On an API key or a subscription the cache survives that change; on Bedrock, Google Cloud, or a gateway an effort change clears the cache, so on those platforms the effort set at the start holds for the whole run.
- **The ladder.** Picks the engine per slice. Fable 5.1 orchestrates and holds the final judge; Haiku 4.5, Sonnet 5, and Opus 5.5 take slices by type, and a slice that fails its judge is retried once one effort step up, then moves one rung up. The judge runs on the cheapest rung the advisor rule allows (one rung up or higher, or a machine check; Fable 5.1 work is judged by a fresh Fable 5.1 context), and the gate that prints FINAL stays with a fresh Fable 5.1 context. See `model-ladder.md`.

## Match the method to trust

Graduate a loop as you learn to trust it:

1. Start as **a prompt**, watched. See whether the bar is strict enough and the VERIFY is honest.
2. Move to attended **`/loop`** once the loop converges reliably. Watch it clear the bar a few times.
3. Graduate a proven loop to **`/schedule`** and walk away. Only for incorruptible judges, and only with irreversible steps kept behind a human on the exit (see `failure-modes.md`).

Start attended, then let go. A loop is only as good as its "done," so prove the "done" before you stop watching.

One word of care: this is **graduation**, a loop moving up the run methods as trust grows. **Promotion** is a different move, a slice moving up the model ladder inside a loop when its work fails the judge. The run log uses both words and they never swap.
