---
type: spec
capability: marginal-analysis
engagement: perfect-competition
date: 2026-09-07
status: draft
built_with: "Claude Code (openpyxl build, LibreOffice recalculation)"
---

# Marginal Analysis — Model Specification

## Purpose

The purpose of this model is to figure out the most profitable way to divide the farm’s 64 available beds among tomatoes, carrots, and mesclun. Since each crop generates different revenue and requires different amounts of labor and fertilizer, planting more of the highest-revenue crop does not necessarily mean we will make the most profit. The model needs to account for these differences, along with diminishing returns, crop-specific planting limits, available labor, and the limit on temporary workers.

Ultimately, the model should answer: With 64 beds available, what combination of tomatoes, carrots, and mesclun will maximize the farm’s profit while staying within its planting and labor constraints?

## Inputs — the named contract

| Name | Value | Unit | Source |
|---|---:|---|---|
| Total Bed Capacity | 64 | beds | Perfect Competition Case |
| Season Length | 36 | weeks | Perfect Competition Case |
| Fixed Costs | $20,000 | dollars/season | Perfect Competition Case |
| Farmer Field Hours | 720 | hours/season | Perfect Competition Case |
| Farmer Labor Rate | $34.72 | dollars/hour | Perfect Competition Case |
| Maximum Temporary Workers | 4 | workers | Perfect Competition Case |
| Temporary Worker Hours | 1,440 | hours/worker/season | Perfect Competition Case |
| Temporary Labor Rate | $17.36 | dollars/hour | Perfect Competition Case |
| Tomato Bed Limit | 20 | beds | Perfect Competition Case |
| Tomato Revenue per Bed | $8,800 | dollars/bed/season | Perfect Competition Case |
| Tomato Base Labor | 2.5 | hours/week/bed | Perfect Competition Case |
| Tomato Fertilizer Cost | $880 | dollars/bed/season | Perfect Competition Case |
| Tomato Diminishing-Returns Rate | 10% | per additional bed | Perfect Competition Case |
| Carrot Bed Limit | 20 | beds | Perfect Competition Case |
| Carrot Revenue per Bed | $2,094 | dollars/bed/season | Perfect Competition Case |
| Carrot Base Labor | 0.833 | hours/week/bed | Perfect Competition Case |
| Carrot Fertilizer Cost | $440 | dollars/bed/season | Perfect Competition Case |
| Carrot Diminishing-Returns Rate | 2.5% | per additional bed | Perfect Competition Case |
| Mesclun Bed Limit | 30 | beds | Perfect Competition Case |
| Mesclun Revenue per Bed | $2,700 | dollars/bed/season | Perfect Competition Case |
| Mesclun Base Labor | 1.25 | hours/week/bed | Perfect Competition Case |
| Mesclun Fertilizer Cost | $880 | dollars/bed/season | Perfect Competition Case |
| Mesclun Diminishing-Returns Rate | 1.25% | per additional bed | Perfect Competition Case |

Revenue per Bed and Fertilizer Cost per Bed are full-season amounts and should not be multiplied by Season Length. Season Length is used to convert weekly labor requirements into seasonal labor requirements.

## Structure

- **Inputs:** Contains all farm-wide and crop-specific assumptions used by the model, including bed limits, revenue, labor, fertilizer, diminishing-return rates, and other farm constraints.
- **Cost Structure:** Calculates the farm’s major costs, including fertilizer, farmer labor, temporary labor, and fixed costs, based on the selected crop mix.
- **Marginal-Cost Schedules:** Shows the labor requirement, costs, and marginal cost at each possible quantity for tomatoes, carrots, and mesclun so the cost of adding another bed can be evaluated. Each crop is analyzed independently in its standalone schedule.
- **Optimization:** Uses the whole-number quantities of tomato, carrot, and mesclun beds as the decision variables and uses Solver with the GRG Nonlinear method to maximize season profit. Decision variables must be nonnegative integers and must satisfy the crop-specific bed limits, total bed capacity of 64, maximum of four temporary workers, and available labor capacity.
- **Checks:** Provides visible pass/fail checks showing whether the optimized crop mix stays within the farm’s total-bed, crop-specific, temporary-worker, and labor-capacity constraints.

## Calculation Logic

- TomatoLaborHours = TomatoBeds × Tom_BaseLabor × SeasonLength × (1 + Tom_DR)^TomatoBeds
- CarrotLaborHours = CarrotBeds × Car_BaseLabor × SeasonLength × (1 + Car_DR)^CarrotBeds
- MesclunLaborHours = MesclunBeds × Mes_BaseLabor × SeasonLength × (1 + Mes_DR)^MesclunBeds
- For the standalone marginal-cost schedules, the same three formulas apply at each evaluated quantity q, with q substituted for TomatoBeds, CarrotBeds, or MesclunBeds respectively.
- The diminishing-returns rate compounds based on the number of beds planted. It increases labor requirements and does not reduce revenue per bed.
- TomatoRevenue = TomatoBeds × Tom_Rev
- CarrotRevenue = CarrotBeds × Car_Rev
- MesclunRevenue = MesclunBeds × Mes_Rev
- TotalRevenue = TomatoRevenue + CarrotRevenue + MesclunRevenue
- TomatoFertilizerCost = TomatoBeds × Tom_Fert
- CarrotFertilizerCost = CarrotBeds × Car_Fert
- MesclunFertilizerCost = MesclunBeds × Mes_Fert
- TotalFertilizerCost = TomatoFertilizerCost + CarrotFertilizerCost + MesclunFertilizerCost
- TotalLaborRequired = TomatoLaborHours + CarrotLaborHours + MesclunLaborHours
- FarmerHoursUsed = MIN(TotalLaborRequired, FarmerHours)
- TempLaborHoursNeeded = MAX(TotalLaborRequired − FarmerHours, 0)
- TempWorkersNeeded = the minimum whole number of temporary workers needed to provide sufficient temporary-labor capacity. Each temporary worker provides up to TempWorkerHours hours, and no more than MaxTempWorkers temporary workers are available.
- TotalLaborCapacity = FarmerHours + (TempWorkersNeeded × TempWorkerHours)
- For the optimized crop mix, TotalLaborRequired must be less than or equal to TotalLaborCapacity and cannot exceed MaxLaborCapacity.
- FarmerLaborCost = FarmerHoursUsed × FarmerRate
- TempLaborCost = TempLaborHoursNeeded × TempRate
- TotalLaborCost = FarmerLaborCost + TempLaborCost
- BlendedLaborRate = TotalLaborCost ÷ TotalLaborRequired. If TotalLaborRequired equals zero, BlendedLaborRate should be reported as zero to avoid a division-by-zero error.
- TotalCost = FixedCosts + TotalFertilizerCost + TotalLaborCost
- SeasonProfit = TotalRevenue − TotalCost
- MarginalCost(q) = TotalCost(q) − TotalCost(q−1). At q = 0, MarginalCost should be left blank because there is no prior quantity from which to calculate a change in TotalCost. MarginalCost is evaluated per quantity q within each crop's standalone marginal-cost schedule; because it varies by q rather than naming one fixed cell, it is not represented as a single scalar named range in model.xlsx — each schedule's Total Cost and Marginal Cost columns remain ordinary row-by-row formulas built from the same named-range inputs listed above.

## Conventions

- Farmer labor is used first, up to the 720 field hours available. Temporary labor covers the remaining required labor at $17.36 per hour.
- Temporary workers determine available labor capacity. Each worker provides up to 1,440 seasonal hours, with a maximum of four temporary workers. Temporary labor cost is based on the actual temporary hours needed rather than charging the full seasonal capacity of each worker.
- Bed-count decision variables must be whole, nonnegative integers. Each crop may have a quantity of zero and may not exceed its crop-specific bed limit.
- Revenue per Bed and Fertilizer Cost per Bed are full-season amounts. Season Length should only be used to convert weekly base labor requirements into seasonal labor requirements.
- Diminishing returns increase the labor required at each crop quantity; they do not decrease revenue per bed.
- The diminishing-returns adjustment applies to the crop’s total labor requirement at the quantity being evaluated, rather than only to the newest bed added.
- Each standalone marginal-cost schedule evaluates one crop independently, as if it were the farm’s only crop, while varying that crop from zero beds through its maximum bed limit.
- Standalone marginal-cost schedules should calculate every quantity from q = 0 through the crop-specific bed limit even when the labor requirement at a particular quantity exceeds the farm’s available labor capacity. Labor infeasibility should be visible but should not prevent the standalone schedule from calculating that quantity. The 6,480-hour maximum labor-capacity constraint applies to the optimized crop mix.
- Standalone Total Cost includes the farm’s $20,000 fixed cost at every quantity, including q = 0. Because Fixed Costs do not change with quantity, they cancel out when Marginal Cost is calculated.
- Farmer and temporary labor are determined at the farm level after combining the labor requirements of all three crops, rather than assigning individual workers to specific crops.
- For P&L reporting, labor costs should be allocated using a blended labor rate calculated as Total Labor Cost divided by Total Labor Required. Farmer and temporary labor are pooled at the farm level rather than assigned directly to individual crops.
- The model should maximize season profit. It should not be required to use all 64 beds, all available labor hours, or all available temporary-worker capacity if doing so would reduce profit.
- “Checks” and “Constraint Status” refer to the same visible set of pass/fail constraint checks in the workbook.

## Validation Rules

- At q = 1, the tomato labor schedule must calculate exactly 99 hours.
- At q = 10, the tomato labor schedule should calculate approximately 2,334.37 hours. This verifies that the 10% diminishing-returns rate compounds with quantity rather than being applied only once.
- The published check figure for the optimized solution is 10 tomato beds, 20 carrot beds, and 30 mesclun beds, for a total of 60 beds.
- The published check figure for optimized season profit is approximately $42,762.
- The standalone marginal-cost schedules should show P ≈ MC around q = 10 for tomatoes, q = 10 for carrots, and q = 6 for mesclun. Here, P means the crop’s Revenue per Bed and MC means Marginal Cost.
- Solver should use the GRG Nonlinear method with integer bed-count constraints as specified.
- Solver should be run from at least two starting points: 0/0/0 and 20/0/0. If the two runs produce different solutions, the difference should be documented as an audit finding rather than silently choosing one result.
- If Solver fails to converge or returns an error, do not silently switch Solver methods or alter the model logic. Document the issue as an audit finding so it can be investigated.
- All constraint checks should be visible and green when the solution satisfies the total-bed, crop-specific bed, labor-capacity, and temporary-worker limits.
- At least one intermediate marginal-cost result should be cross-checked against the Farm Profit Lab during the audit.
- Calculated cells must contain formulas tied to the model inputs rather than pasted values.
- The completed workbook should contain no formula errors, including #REF!, #DIV/0!, or #NAME?.

## Outputs

- **Optimal Crop Mix:** Reports the profit-maximizing number of tomato, carrot, and mesclun beds and the total number of beds used.
- **Revenue:** Reports revenue by crop and total farm revenue for the selected crop mix.
- **Labor:** Reports labor hours required by crop, total labor required, farmer hours used, temporary labor hours needed, temporary workers required, total labor capacity, and unused labor capacity.
- **Costs:** Reports fertilizer costs by crop, total fertilizer cost, farmer and temporary labor costs, total labor cost, blended labor rate, fixed costs, and total farm cost.
- **Profit:** Reports total season profit for the selected crop mix.
- **Marginal Analysis:** Reports the standalone marginal-cost schedule for each crop and makes it possible to identify the quantity where Price (Revenue per Bed) is approximately equal to Marginal Cost. The schedules should also make labor-infeasible quantities visible rather than removing them.
- **Constraint Status:** Clearly reports whether the optimized solution satisfies all bed, crop-specific, labor-capacity, and temporary-worker constraints.

## Audit Findings

1. **Labor calculation check:** I manually checked tomato labor at q = 1 and got 99 hours, which matched the workbook. I also checked q = 10 and got approximately 2,334.37 hours. This confirmed that the 10% diminishing-returns rate is compounding as the number of beds increases rather than being applied only once.

2. **Farm Profit Lab cross-check:** I compared the mesclun marginal-cost schedule in my workbook with the Farm Profit Lab. My workbook shows P ≈ MC at 6 beds, with marginal cost of about $2,667 compared with the $2,700 market price. The Farm Profit Lab also identifies P ≈ MC at 6 mesclun beds. This helped confirm that my marginal-cost schedule is behaving consistently with the independent reference model.

3. **Solver starting-point check:** I ran Solver using GRG Nonlinear from both required starting points. From 0/0/0, Solver remained at 0/0/0, while starting from 20/0/0 produced 10 tomato, 20 carrot, and 30 mesclun beds. This showed that the Solver result is sensitive to its starting values and could otherwise allow a local solution to be mistaken for the best solution.

4. **Solver constraint check:** During the manual Solver audit, I found that Excel for Mac would not accept the labor constraints when they referenced calculations on a different worksheet. Formula-driven helper cells were added to the Optimization sheet that link directly to the existing labor calculations. After this change, Solver accepted the full constraint set and all constraint checks remained TRUE. This caught an implementation issue that was not visible from reviewing the model outputs alone.

5. **Published profit check:** The optimized crop mix matches the published solution of 10 tomato, 20 carrot, and 30 mesclun beds, but my workbook calculates season profit of approximately $42,775 instead of the published $42,762. I traced the revenue, fertilizer, labor, and fixed-cost calculations and confirmed that the workbook uses the values currently stated in the case and committed specification. The approximately $13 difference appears to result from rounding or additional precision in the reference calculation. I kept the published input values rather than changing them simply to force the check figure.

**Additional observation for Stage 3:** The standalone tomato marginal-cost schedule shows a dip around q = 6. I noted the pattern during the audit but am leaving the economic explanation for the reporting stage.
