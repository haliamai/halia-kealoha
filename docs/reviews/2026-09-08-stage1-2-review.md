<!-- PR TARGET: https://github.com/haliamai/halia-kealoha | Stage 1.2 -->
# Stage 1.2 review — spec, build, audit

> **Hurricane Lowell.** If you are boarding up, packing, or hauling the patio furniture indoors, put this review down — it will keep, and nothing in it needs you today. And if you are reading a review while a hurricane bears down on the islands: I am writing one in the same weather, so there is no judgement coming from this end. :) Look after your people first — the coursework will survive whatever Lowell does.

**Spec:** [`capabilities/marginal-analysis/spec.md`](https://github.com/haliamai/halia-kealoha/blob/main/capabilities/marginal-analysis/spec.md)

> Graded 2026-09-08 against the specification and workbook you committed. The specification is strong and the audit note is honest in a way that is rarer than it should be — you found a $13 gap against the published figure, traced it, and refused to change inputs to close it. The gap has a cause and it is findable, and the Checks sheet is the reason you could not find it.

| Criterion | Where it stands |
|---|---|
| Spec completeness — inputs, structure, calculation flow | A full named contract with units and sources, nine sheets each described by content, and the calculation logic and conventions stated properly. What costs you here is the input values themselves: the wage rates and the carrot labor hours are carried as the case's rounded display figures rather than as derivations. |
| Spec validation rules | Twelve rules, all stated before the build, including two hand checks, the published mix and profit, the expected crossings, and a two-starting-point Solver rule that says what to do if the runs disagree. The rule forbidding a silent switch of Solver method is a good one and nobody else wrote it. |
| Workbook satisfies the contract | Formula-driven with named ranges, constraint checks all green, crossings correct. But it computes $42,775.16 against a published $42,762, and the Checks sheet contains no acceptance test at all — only feasibility checks — so the workbook cannot detect its own miss. Temporary workers are reported as 4 when the plan needs 3.16. |
| Audit note | Five findings, each with what it caught. Two of them are the right kind of hard: you reported a Solver run that disagreed with the other rather than quietly keeping the good one, and you documented the profit gap instead of forcing the inputs to close it. |

### The $13, and where it lives

Your fifth audit finding reports $42,775 against the published $42,762, says you traced the revenue, fertilizer, labor and fixed-cost calculations, confirmed the workbook uses the values stated in the case, and concluded the difference is rounding or precision somewhere in the reference calculation. Then you kept your inputs rather than bending them to hit the target.

That last decision is right and I want it on the record before I tell you where the $13 is.

It is in three inputs, and your own sentence is nearly the answer. The case prints $34.72 and $17.36 and 0.833. None of those are the real values. The farmer's rate is $50,000 across 1,440 hours, which is $34.7222…; the temporary rate is $25,000 across 1,440 hours, which is $17.3611…; and carrot labor is tomato labor divided by three, which is 0.8333… rather than 0.833. Rounded figures are what the case can fit in a table, not what the farm actually pays.

Substitute the three exact values and your model returns $42,761.66. Your total labor hours should be 5,277.2161; they are currently 5,276.8228, and that gap is the carrot rounding on its own.

You were one step away. The step is a habit worth taking from this: when a printed number could have come from a division, use the division.

### Your checks sheet cannot fail

There are seven checks on that sheet and all seven ask the same kind of question: is this allocation feasible? Are the bed counts integers, within their caps, within 64 total, within the labor and worker limits?

Every one of those would pass on a workbook whose profit was out by $13, by $1,300, or by $130,000. Feasibility is not correctness. A mix can satisfy every constraint in the problem and still be computed by a broken formula.

Your own specification already names the checks that would have caught this — the q = 1 hand calculation, the q = 10 figure of 2,334.37 hours, the published mix, the published profit, the expected crossings. Five acceptance tests, written down before you built, and none of them made it into a cell.

That is the gap to close, and it is the same lesson as the $13: the check has to live in the workbook, where it runs every time the file opens, not only in the document that describes it.

### The Solver run you reported honestly

From 0/0/0 Solver stayed at 0/0/0. From 20/0/0 it returned 10/20/30. You wrote both down and said what it meant — that the result is sensitive to its starting values and a local solution could be mistaken for the best one.

Your spec told you to do that, and doing what your own spec says when the answer is inconvenient is the entire discipline this stage is testing. Most people would have run it again from a good starting point and reported the run that worked.

For what it is worth, the behaviour is expected rather than alarming: GRG Nonlinear is a local method and 0/0/0 is a flat spot in this problem, because the first bed of anything has to pay $20,000 of fixed cost before it shows a gain. That is why the case asks for two starting points at all.

### The worker count that rounds away your slack

TempWorkersNeeded reports 4. The plan requires 4,557 temporary hours, which is 3.1647 workers' worth of the 1,440 hours each.

Rounding up is correct for hiring — you cannot employ a sixth of a person. It is wrong for reading a constraint, because it turns a constraint with 0.84 of a worker in hand into one that looks exactly used up. That distinction matters in the next stage, where the question is which constraints bind and which are slack.

Carry both numbers: the fractional one for the economics, the rounded one for the payroll.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your spec into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then correct the spec, not the workbook.** This is the rule that makes the stage work: when a check fails, you fix the specification and regenerate, so the document keeps describing what was actually built.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*Your score and the per-criterion breakdown are in your Lamaku comment, not here — this repository is public.*

— Adam
