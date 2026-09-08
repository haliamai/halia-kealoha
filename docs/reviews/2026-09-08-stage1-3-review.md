<!-- PR TARGET: https://github.com/haliamai/halia-kealoha | Stage 1.3 -->
# Stage 1.3 review — analysis, memo, prompt log

> **Hurricane Lowell.** If you are boarding up, packing, or hauling the patio furniture indoors, put this review down — it will keep, and nothing in it needs you today. And if you are reading a review while a hurricane bears down on the islands: I am writing one in the same weather, so there is no judgement coming from this end. :) Look after your people first — the coursework will survive whatever Lowell does.

**Analysis:** [`analysis/perfect-competition-analysis.md`](https://github.com/haliamai/halia-kealoha/blob/main/analysis/perfect-competition-analysis.md)

> Graded 2026-09-08 against the analysis, memo, figures and prompt log you committed. The structure is right, the voice is yours, and the hypothesis section is one of the best in the cohort. What holds it back is precision: several of the numbers are attached to the wrong bed, and the section that resolves the loss-making crops has no numbers in it at all.

| Criterion | Where it stands |
|---|---|
| P = MC evidence and binding constraints | The tomato crossing is right and cell-referenced, both caps are correctly identified as binding, and the priority between them is right. Two figures are attached to the wrong bed, and the temporary-worker sentence describes a constraint that is comfortably slack as though it were fully used. |
| MC dip and the at-a-loss resolution | The dip mechanism is correct in outline — the wage switch, then compounding overtaking it — but located loosely and without the hour figures that would pin it down. The at-a-loss reasoning is correct and clearly explained, and cites nothing from your own workbook. |
| Figures and the hypothesis revisit | Two figures, both referenced, both rendering. The hypothesis paragraph is the strongest part of the submission: you name the threshold you set in advance and hold yourself to it. |
| Prompt log and reflection | Curated, dated, with the tool and the verification recorded per session, and the reflection names a concrete instance of refusing an AI-proposed change. The reasoning you gave for refusing it is the thing to look at again — see below. The capability README was also not updated to point at the analysis and the memo. |

### The two numbers that are not the same number

This is the most useful thing I can tell you, and it explains your reflection as well as your analysis, so it is worth the space.

Your analysis says: at bed 20, carrot marginal cost is about $1,742, still about $352 below its $2,094 price. Those two figures cannot both describe bed 20. $2,094 minus $1,742 is $352, so the arithmetic is consistent — but the marginal cost of the twentieth carrot bed is $1,688.95, not $1,742. $1,741.51 is the marginal cost of bed twenty-one, the one the cap will not let you plant.

So there are two different quantities here and they answer two different questions. How far under price did the last bed I was allowed to plant come in? That is $2,094 minus $1,688.95, or $405.05. What would one more bed be worth if the cap moved? That is $2,094 minus $1,741.51, or $352.49. The first is about the bed you have. The second is the shadow price, and it is the one that belongs in the memo, because it is what the farmer would be buying.

The same pair exists for mesclun: $279.90 of gap at the cap, $246.47 for the next bed.

### Why this is also the answer to your reflection

Your reflection records that your assistant calculated $405.63 and $280 from the workbook and wanted you to correct your analysis to match the published $352 and $246, and that you checked the assignment instructions and declined.

Look at those numbers again. $405.63 and $280 are the gap at the cap. $352 and $246 are the value of the next bed. Your assistant had not made an error — it had computed a different, real quantity and mislabelled it, and so had the published figures you were comparing against, in the sense that neither of you said which question was being answered.

You made the right call. I want to be clear about that, because it took nerve and most people would have changed the numbers. But the reason you gave was that the assignment said so, and that reason will not survive contact with a client who has no answer key. The reason that works is the one above: those are two different quantities, here is which one the recommendation needs, here is why.

Deferring to the published figure is also what put $1,742 next to bed 20 in your analysis. You had $352 as fixed, and the marginal cost got adjusted to fit it. That is the direction of reasoning to watch — when your model and the key disagree, the disagreement is the finding, and your job is to work out which question each of them answered.

### The temporary-worker sentence

You write that temporary workers are not worth relaxing because we already have all four we would need and there is slack left in the hours.

The conclusion is right — the constraint is slack and relaxing it buys nothing. The description is not. The plan needs 4,557 temporary hours, which is 3.16 workers' worth of the four available. You are not using all four; you are using just over three, and that is why there is nothing to gain.

This traces back to your workbook, which reports temporary workers needed as 4. It is rounding 3.16 up to a whole worker. That is a defensible convention for hiring — you cannot hire sixteen-hundredths of a person — but it is the wrong number to read a constraint off, because it hides how much slack there is. Keep both: the fractional figure for the economics, the rounded one for the payroll.

### The section that needs your own numbers

Your at-a-loss paragraph explains the economics correctly. Fixed cost is paid regardless, so the question is whether price covers average variable cost; when it does, the crop covers its own variable costs and contributes to a cost you were paying anyway.

Every sentence of that is true, and none of it comes from your workbook. It would read the same if you had never built a model.

The figures are available to you and they are not hard to reach: carrot average variable cost at its cap is $1,918.45 against a $2,094 price, mesclun is $2,430.74 against $2,700. Two numbers, and the paragraph stops being a textbook explanation and starts being evidence.

This is the difference the rubric is pointing at when it says every claim should point at a cell. Not because citations are good practice in the abstract, but because a reviewer cannot check a generalisation, and can check $1,918.45.

### What you did better than almost anyone

Before you built anything, you wrote that you would consider yourself wrong if the model came in below 17 tomato beds. It came in at 10. Your analysis says so plainly and does not go back to soften the threshold.

That is the hardest part of this stage and most submissions quietly avoid it. A prediction with a number attached, held to afterwards, is what makes the comparison mean anything — and it is why your closing line, that filling every bed is not the same as maximising profit, reads as something you learned rather than something you were told.

### One small file fix

The stage asks you to update capabilities/marginal-analysis/README.md so its "exercised in" line points at the analysis and the memo as well as the brief. Yours still says only "exercised in: Perfect Competition".

It is a one-line edit and the reason it is on the checklist is that the capability folder is supposed to be the index somebody reads to find your evidence. Right now it names the engagement but does not link to anything you produced for it.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your analysis into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** The analysis, the memo and the reflection are yours to draft. An explanation you did not reason through cannot be defended when somebody asks you a follow-up question about it.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*Your score and the per-criterion breakdown are in your Lamaku comment, not here — this repository is public.*

— Adam
