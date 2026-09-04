<!-- PR TARGET: https://github.com/haliamai/halia-kealoha | Stage 1.1 -->
# Stage 1.1 review — engagement brief

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/haliamai/halia-kealoha/blob/main/docs/briefs/perfect-competition-brief.md)

> Re-graded 2026-09-04 against your revision of 3 September. You have been reviewed on this before. You put a number to the compounding, which was the main thing outstanding, and you sharpened the problem statement while you were in there.

| Criterion | Where it stands |
|---|---|
| Problem restated in your own voice | Stronger. The new clause names the thing the case is actually about: "the crops are competing for the farm's limited bed space, and the farm has to determine which combination produces the highest profit." You already had the two ways a crop can stop — its planting limit, or marginal cost overtaking price — and stating the competition for beds explicitly is what makes those two alternatives meaningful rather than abstract. |
| Hypothesis names a specific mix | 20 tomato, 20 carrot, 24 mesclun. Three integers, all inside their caps, summing to 64. Unchanged. |
| Economic mechanism | Stronger. "By the 10th tomato bed, the labor required per bed is already about 2.6 times what it was for the first bed." That is the arithmetic the brief was missing — 1.10 to the tenth is about 2.59 — and you then do the harder thing, which is to hold your prediction anyway: "even with that faster increase, I think the higher return on tomatoes will still make it worth planting all 20 beds." Naming the force working against your own conclusion and keeping the conclusion is what makes a prediction worth testing. One small thing: measured against the first bed's actual 99 hours the multiplier is about 2.36, and 2.6 is the ratio against the 90-hour base before compounding. Both are defensible readings; say which one you mean. |
| Falsifiability and process | Unchanged and still at the top. "Fewer than 17 tomato beds... I would consider 17–20 close enough to support my prediction, but anything below that would mean I underestimated how much the 10% increase in labor adds up." You and Micah Kosasa are the only two who committed to a threshold in advance, and yours was first. |

### You are predicting against the grain, and that is the right kind of brave

The published optimum is 10 tomato beds. You are predicting 20, you know the labor cost more than doubles by bed 10, and you are holding the prediction anyway with a stated band of 17 to 20.

That is exactly what this stage wants. You are not graded on being right — you are graded on making a claim that could be shown wrong, and yours can be, decisively, by a single number the model returns. When it comes back at 10 you will have the most interesting Stage 1.3 reflection in the cohort, because you will be able to point at the precise sentence where your reasoning parted company with the arithmetic.

Do not revise it now that the model is close. The comparison is the deliverable.

### The thing your own number is telling you

You wrote that labor per bed roughly 2.6 times by bed 10 and concluded the return still justifies 20 beds. Push the same arithmetic four beds further and see whether you still believe it.

At 20 beds the crop needs 20 x 2.50 x 36 x 1.10^20, about 12,110 hours. The farm has 6,480 hours in total — the farmer's 720 plus four temporary workers at 1,440 each — before either of the other two crops gets planted at all.

So there is a second question hiding under your prediction, and it is a different one from profitability: can 20 tomato beds be staffed at all? Working that out before the model runs would let you separate two ways of being wrong — the beds are not worth planting, versus the beds cannot be planted. Your falsification section currently treats both as the same outcome.

### Stage 1.2 is due 6 september

capabilities/marginal-analysis/ has no spec.md. Your prompt log has been kept properly all the way through and your commit history is the cleanest in the cohort, so the habits are there; the specification is a document you have not written yet.

Two hand-checks to put in it: one tomato bed is 1 x 2.50 x 36 x 1.10 = 99 hours exactly, and ten tomato beds are 2,334.37. The second is the one that catches a model applying the rate once instead of compounding it per bed — and it is your 2.6 figure, restated as something a spreadsheet can fail.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error.*

*Your score and the per-criterion breakdown are in your Lamaku comment, not here — this repository is public.*

— Adam
