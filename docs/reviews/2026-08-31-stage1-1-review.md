<!-- PR TARGET: https://github.com/haliamai/halia-kealoha | Stage 1.1 (2.5 pts) -->
# Stage 1.1 review — engagement brief · **95 / 100** (A) · 2.38 / 2.5 pts

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/haliamai/halia-kealoha/blob/main/docs/briefs/perfect-competition-brief.md)

> Re-graded 2026-08-31 against your revised brief. Your previous score was 89, and 80 before that. You have now moved twice, both times by doing exactly the specific thing the feedback named, and both times without softening your prediction to make the objection go away.

| Criterion | Earned | Notes |
|---|---|---|
| Problem restated in your own voice | 28 / 30 | Up from 25, and the gain is two facts that were not there before. "The maximum planting limits add up to 70 beds, so all three crops cannot reach their maximum" — that is the arithmetic that makes this a choice rather than a checklist, and stating it means your hypothesis has to explain which crop gives ground. And "labor costs, which are added in $25,000 increments" catches something most of the cohort missed: temporary labor is not bought by the hour, it is bought by the worker, which is why the cost of one more bed can jump rather than creep. You also now name the two ways a crop can stop — its marginal cost reaching price, or its bed cap — which is the correct frame for the whole case. The two points off are length; this is still the short side of what the stage asks. |
| Hypothesis names a specific mix | 25 / 25 | 20 tomato, 20 carrot, 24 mesclun. Unchanged, specific, and you did not move it after the critique, which was the right call. |
| Economic mechanism | 22 / 25 | Unchanged and still good: you have the three diminishing-returns rates, you rank them correctly, and then you take the side that says the tomato revenue advantage survives the labor penalty all the way to the cap. That is a real position and the model can knock it down. The three points are in the same place as before — the argument is comparative where the case hands you the quantities. You say the 10 percent rate "adds up"; the case lets you say by how much. The tenth tomato bed needs about 2.6 times the labor per bed that the first one did, and that ratio is what your whole prediction rests on. |
| Falsifiability and process | 20 / 20 | Full marks, and this is the criterion that moved. Last round I said the word "significantly" was doing the work of a number, and that 20 down to 17 and 20 down to 10 are very different outcomes. You went and wrote the band: "I would know I was wrong if the model shows that the most profitable mix uses fewer than 17 tomato beds. I would consider 17-20 tomato beds close enough to support my prediction, but anything below that would mean I underestimated how much the 10% increase in labor adds up." |
| **Final** | **95 / 100** | earned on merit |

### What this section now does that almost no other brief does

You have committed, in advance and in writing, to a threshold that decides whether you were right. When the model returns a number you will not get to argue about whether it counts as close — you already said. That is the difference between a reflection that concludes something and one that grades itself generously after the fact, and there are two briefs in this cohort of twenty-five that have it.

It is also the thing that will make Stage 3 easy for you. Most people will spend that stage deciding retroactively what their prediction meant. You will spend it explaining a mechanism, which is the interesting part.

### What to carry into Stage 1.2

Your prediction and the mechanism behind it are now sharp enough to be tested directly, so build the standalone tomato marginal-cost schedule first, before the optimization. That schedule answers your own question on its own: it shows, bed by bed, what the next tomato bed costs and where that cost passes $8,800 with nothing else planted.

Two cautions for the build. The diminishing-returns rate multiplies labor hours, not yield — revenue per bed stays at $8,800 for the twentieth bed as much as the first. And the penalty applies to every bed of that crop at that quantity, not only to the newest one; a model that charges the increase only to the marginal bed will be tens of thousands of dollars off and will still look plausible.

Standing rule: whatever the model returns, do not edit the brief to match it.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief, this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule for this stage: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error — Stage 3 asks you to explain the gap, and a brief quietly edited to be right afterwards has nothing left to explain.*

— Adam
