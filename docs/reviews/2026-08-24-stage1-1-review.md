<!-- PR TARGET: https://github.com/haliamai/halia-kealoha | Stage 1.1 (2.5 pts) -->
# Stage 1.1 review — engagement brief · **80 / 100** (B-) · 2.00 / 2.5 pts

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/haliamai/halia-kealoha/blob/main/docs/briefs/perfect-competition-brief.md)

| Criterion | Earned | Notes |
|---|---|---|
| Problem restated in your own voice | 25 / 30 | Accurate and in your own words, and you name the four things that matter — return per crop, labor, diminishing returns, planting limits. It is on the brief side of the "half a page to a page" the stage asks for, and it stops at listing the factors rather than saying how they interact. |
| Hypothesis names a specific mix | 25 / 25 | You name 20 tomato / 20 carrot / 24 mesclun. Specific and committed. No complaints here. |
| Economic mechanism | 15 / 25 | This is where the score comes from. The reasoning is "I think tomatoes may have the largest return, but the cost of labor could impact how many beds are actually worth planting" — and that sentence is hedged in both directions, so no result can contradict it. Your assumptions section goes further the wrong way: "we should try to use all 64 beds and diversify the crops rather than rely too heavily on one" is close to the one rationale the stage explicitly rules out, because diversification-for-its-own-sake would justify any mix. The case gives you three numbers that decide this — 10%, 2.5%, 1.25% per bed — and the brief does not use them. |
| Falsifiability and process | 12 / 20 | You wrote the section, which puts you ahead of several people, but the content is circular: "I would know I was wrong if the model shows that a different mix would generate more profit." That is true of every hypothesis by construction. The second clause gets closer — "if labor costs make some of my predicted beds more expensive to produce than what they earn" is an actual mechanism — and that is the sentence to build on. Brief committed 2026-08-22 with no modeling before it. Correct path, correct order. |
| **Raw total** | **77 / 100** | — |
| **Floor applied** | **+3** | 80% floor: a committed brief that states the problem and names a specific mix |
| **Final** | **80 / 100** | floored |

### A straight word about this score

You scored 99 on Stage 0 and had the cleanest repository in the cohort. This stage is testing something different, and it is worth naming the difference rather than letting the number speak for itself.

Stage 0 rewarded craft: structure, discipline, follow-through. You were the best in the cohort at it. Stage 1 rewards committing to a claim that could be wrong, and your brief avoids committing. "Tomatoes may have the largest return, but labor could impact how many beds are worth planting" is true no matter what the model says, and a prediction that survives every outcome is not a prediction. This is a very common instinct and it is not carelessness — hedging feels careful. In an engagement brief it is the opposite, because the whole value of the document is that it can be shown wrong later.

The good news is that this is one paragraph of work for you, and the deadline has not passed.

### What I'd fix first

- Commit to a mechanism, using the three numbers the case hands you. Tomato labor grows 10% per additional bed, carrots 2.5%, mesclun 1.25%. Those compound: the 20th tomato bed needs roughly 6.7 times the labor per bed of the first, while the 20th carrot bed needs about 1.6 times. Given that, ask whether you still believe tomatoes run all the way to 20. Whatever you conclude, say why in terms of those rates. Something like "tomatoes reach their cap because even at 6.7x labor the $8,800 price still covers marginal cost" is a claim the model can knock down — which is exactly what you want.

- Cut the diversification sentence, or make it economic. "Diversify rather than rely too heavily on one crop" is a risk argument, and this model has no risk in it — prices and yields are certain. If you mean something economic (the caps force spreading, or labor smooths across crops), say that instead.

- Rewrite the falsification test so it can actually fail. Name outcomes: tomatoes finishing below 15 beds would mean the labor penalty bites much earlier than you assumed. Mesclun reaching its 30-bed cap rather than your 24 would mean you underweighted how flat its 1.25% curve is.

### Looking ahead to Stage 2

Everything about how you work — the commit discipline, the AGENTS.md rule about not pushing without your review, the prompt log — is already at the level this course is trying to reach. Point that same discipline at the economics and this stage looks very different.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief, this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule for this stage: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error — Stage 3 asks you to explain the gap, and a brief quietly edited to be right afterwards has nothing left to explain.*

— Adam
