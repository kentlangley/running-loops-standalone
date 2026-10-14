# The Loop and Your Other Skills

There is nothing to install. The loop protocol is a meta-skill: it runs alongside whatever other skills you have installed. Claude picks the skill each pass needs from the skill descriptions, or you name it.

This is the piece that makes a skill-routed loop different from a plain Ralph loop.

## The clean split

Two systems, each doing one job:

- **Your skills** handle what to do: the work itself, with their own checkpoints and your loaded business context.
- **This loop skill** handles keep going until it is real: self-correct, verify, fix its own work, and go again until the bar is met.

Put the two together and the loop routes into the right skill on each pass, then persists until done.

## The three payoffs

1. **Better routing.** Claude picks the right skill each pass from the skills you have installed. Pass one might draft with your style-guide skill; pass two might run a claims check; pass three might restyle with your brand or design skill. The loop routes, where a plain Ralph loop reruns one flat prompt.

2. **Compounding context.** Every pass pulls richer, more personal context as your skills and projects grow with the business. Your project folders and run logs are the long-term memory. It reads them back. The loop you run next month starts from more than the loop you ran today. The run logs are part of that memory: they record which rung and effort cleared which slice type at what cost per completed slice, so the next loop starts each slice on the cheapest rung and lowest effort that have already proven themselves, and the ladder learns downward as well as up. See `model-ladder.md` and `delegation-and-promotion.md`.

3. **Cleaner stops.** Tie "done" to your skills. The stopping condition becomes: every skill named in the criteria reports green and its checks pass. That is a definition of done you can defend.

## Tying "done" to your skills

When success criteria name skills, the loop's exit is tied to those skill-judges:

```
SUCCESS CRITERIA:
  - <your style skill> did its job
  - a claims check ran, all claims verified
  - a logic check ran, all arguments sound
  - your brand or design skill applied cleanly
  - the author would be proud to publish this
```

The loop prints FINAL only when every named skill clears its threshold on the independent score. Each skill brings its own validation checkpoints, so the loop inherits a real bar instead of inventing a loose one. See `the-judge.md` for skills-as-judges.

## Loops as an operating primitive

In ExO terms, loops are the Three Compounding Loops of the agentic firm. A firm that runs its work as skill-routed loops with incorruptible judges is a firm where "done" is measured, and where the system carries more of the work each cycle. The loop is how the operating layer runs itself.
