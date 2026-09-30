Reviewed below, criterion by criterion. This is entered.

**CRITERION BY CRITERION**

* **Spec completeness — inputs, structure, calculation flow** — A full named contract with units and sources, nine sheets each described by content, and the calculation logic and conventions stated properly. What costs you here is the input values themselves: the wage rates and the carrot labor hours are carried as the case's rounded display figures rather than as derivations.
* **Spec validation rules** — Twelve rules, all stated before the build, including two hand checks, the published mix and profit, the expected crossings, and a two-starting-point Solver rule that says what to do if the runs disagree. The rule forbidding a silent switch of Solver method is a good one and nobody else wrote it.
* **Workbook satisfies the contract** — Formula-driven with named ranges, constraint checks all green, crossings correct. But it computes $42,775.16 against a published $42,762, and the Checks sheet contains no acceptance test at all — only feasibility checks — so the workbook cannot detect its own miss. Temporary workers are reported as 4 when the plan needs 3.16.
* **Audit note** — Five findings, each with what it caught. Two of them are the right kind of hard: you reported a Solver run that disagreed with the other rather than quietly keeping the good one, and you documented the profit gap instead of forcing the inputs to close it.

**Repo:** https://github.com/haliamai/halia-kealoha 
**Spec:** `capabilities/marginal-analysis/spec.md` (15,492 B) · **Workbook:** `capabilities/marginal-analysis/model.xlsx` (41,252 B) — *final 2026-09-08 versions; 14,741 / 40,329 were intermediate commits the same day*

**WHAT I'D FIX FIRST**

* **Derive the three inputs instead of typing them.** Your contract carries the two wage rates and the carrot labor hours as the case's rounded display figures. That is the whole cause of the $42,775.16 your workbook returns against the published $42,761.66 — you documented that $13.50 honestly and did not close it, and the close is exactly this: build those three from the underlying quantities the case gives, and let the rounded figures be something you display, never something you compute from. That one change is worth most of the nine points in the workbook row.

* **Put your acceptance tests in the workbook.** You already wrote five of them in the spec — the q = 1 hand calculation, the q = 10 figure of 2,334.37 hours, the published mix, the published profit, the expected crossings — and not one of them made it into a cell. Your Checks sheet has seven checks and all seven ask the same question: is this allocation feasible? A workbook out by $13 passes every one of them. Feasibility is not correctness, and a check that lives in a document instead of a cell does not run. An afternoon's work, and it makes the first fix self-verifying.

* **Report temporary workers as 3.16, not 4.** Rounding up to a whole worker is a staffing decision, not a model output. The plan needs 3.16 workers' worth of hours; recommending you hire 4 is a fine recommendation, shown against the 3.16 the model returned. Ten minutes, and it matters in the next stage, where the question is which constraints bind and which have slack.

**LOOKING AHEAD**

Your validation rules (24 of 25) and your audit note (11.5 of 12.5) are already close to the top of what this stage offers — the gap here is entirely between what you specified and what you built, which is a better problem to have than the reverse. Correct the spec first and regenerate the workbook from it, rather than patching the sheet by hand; the spec is the deliverable. Push the revision and I will re-read it, and a re-read can raise this grade and not lower it.

---
