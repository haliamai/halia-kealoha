---
type: spec
capability: economic-research
engagement: hawaii-geothermal
date: 2026-09-25
status: draft
---

# Hawaiʻi Geothermal — Research Specification

## 1. Purpose

This spec exists to define the data sources, quantitative model, figure, and success criteria for the Hawaiʻi geothermal research paper before the underlying research is executed, so the paper does not become whatever the sources happen to turn up. It does not restate or re-argue the hypothesis in `docs/briefs/research-brief.md` — that document is locked. The decision-maker is the Hawaiʻi State Legislature, and the decision under evaluation is whether, and under what conditions, Hawaiʻi should continue public funding for geothermal resource characterization. This spec is a pre-research plan, not a record of conclusions already reached. No item below should be read as verified, sourced, or decided unless it is explicitly marked as such.

## 2. Data Sources — the named contract

Every row below is a research requirement, not a finding. Status starts at **Pending** for all rows and should only change to **Verified** once a primary source and retrieval date are actually recorded (in `data/sources.md`, once that file exists — see Section 9 and the source-management convention below).

| # | Item | Status | Source | Retrieval Date | Notes |
|---|---|---|---|---|---|
| 1 | $5 million allocation amount and fund | Verified | Hawaiʻi State Energy Office — Testimony of Mark B. Glick before the Senate Committee on Energy and Intergovernmental Affairs re: SCR 136 (Mar. 25, 2025); corroborated by University of Hawaiʻi Office of Research Services, BOR Consolidated Q1 FY2025 | 2026-09-25 | Confirms $5,000,000 from the Coronavirus State Fiscal Recovery Fund, allocated in 2024 by Governor Josh Green, for slim-hole geothermal resource characterization; corroborated by a matching $5,000,000 HSEO-sponsored UH award for the same purpose. Full citations in `data/sources.md`. |
| 2 | Program purpose / use of funds | Pending | TBD | TBD | What the allocation is authorized to be spent on (e.g., slim-hole drilling, resource characterization scope). |
| 3 | Legislative activity concerning continuation/future funding | Pending | TBD | TBD | Bill text, committee reports, testimony, or hearing records establishing that the Legislature is a live decision-maker for continued funding. Do not overstate as enacted law. |
| 4 | Geothermal resource characterization / resource evidence | Pending | TBD | TBD | UH/state geothermal resource assessments; USGS or comparable federal assessments where relevant. |
| 5 | Private incentives / private provision of comparable characterization | Pending | TBD | TBD | Evidence bearing on whether private developers already have sufficient incentive to fund comparable characterization without public support. |
| 6 | Accessibility / public availability of publicly funded characterization information | Pending | TBD | TBD | Whether HSEO/DBEDT characterization results are published or otherwise broadly accessible, or held/shared selectively. |
| 7 | Defensible components of `V_public` | Pending | TBD | TBD | Research task, not a defined list — see Section 4. Must exclude private developer return and total project value. |
| 8 | Distribution/capture of economic value among public, private, Native Hawaiian, and host-community stakeholders | Pending | TBD | TBD | Evidence on who bears costs and who captures benefits; feeds the Recommendation Framework. |
| 9 | Evidence relevant to `Δp` (probability improvement attributable to characterization) | Pending | TBD | TBD | A Hawaiʻi-specific or genuinely defensible estimate, if one exists. "No defensible estimate found" is an acceptable and expected outcome of this row — see Section 4. |

## 3. Research Tasks

These operationalize Professor Stauffer's four execution steps and the two market-failure tests, each tied to a Data Sources row above.

1. **Source the $5 million allocation** — amount and fund, with a primary source and retrieval date. (Row 1)
2. **Source the program's purpose/use of funds.** (Row 2)
3. **Pull the named primary sources into `data/`** — HSEO/DBEDT program materials, Hawaiʻi legislative bills/testimony/hearing records, UH/state geothermal resource assessments, and appropriate federal sources (DOE/USGS) where needed — each recorded with source and retrieval date per the source-management convention in Section 9. (Rows 1–4, 9)
4. **Test whether private developers already have sufficient incentive** to fund comparable characterization without public support, rather than assuming a market failure exists. (Row 5)
5. **Test whether publicly funded characterization information is sufficiently accessible** to create value beyond an individual developer, rather than assuming it behaves as a public good. (Row 6)
6. **Identify and source defensible components of `V_public`** — public economic value only, excluding private developer return and total project value — and explicitly check for double-counting across components. Do not invent or lock these components here. (Row 7)
7. **Research distribution/capture of value** among the public, private developers, Native Hawaiians, and host communities. (Row 8)
8. **Search for a defensible `Δp` estimate.** If none is found, document that explicitly in the Research Log (Section 9) rather than substituting an unjustified proxy. A comparable-jurisdiction proxy may only be used with explicit justification and my approval — it is not a default. (Row 9)
9. **Build the stated-assumption sensitivity chart** from whatever `V_public` and `Δp` information survives the tasks above, with assumptions visible on the page. (See Section 5.)
10. **Develop the recommendation as conditions on continuing the program**, using the candidate conditions in Section 6 as hypotheses to test against the evidence gathered above, not as a predetermined conclusion.

## 4. Quantitative Method

This section defines the calculation structure only. `C`, `Δp`, and `V_public` are each pending — see Section 2 — and none should be treated as known until sourced.

```
Expected public net value = Δp × V_public − C
Break-even Δp* = C / V_public
```

- `C` — the public cost of the program. Verified at $5,000,000 (Data Sources row 1; full citations in `data/sources.md`), sourced to Hawaiʻi State Energy Office testimony and corroborated by a matching University of Hawaiʻi award record. May now be used in the model.
- `Δp` — an assumed improvement in the probability of successful commercial development attributable to characterization. This is not empirically known from research completed so far. It must remain an explicit, stated assumption varied across the sensitivity analysis unless a genuinely defensible estimate is found (Data Sources row 9). A comparable-jurisdiction proxy is not a default substitute and requires explicit justification and approval before use.
- `V_public` — the public economic value of a successful development outcome. This explicitly excludes total project value and private developer return. Its components are not defined or invented in this spec; identifying defensible components, sourcing them, and avoiding double-counting across them is a research task (Section 3, task 6; Data Sources row 7).

This is a stated-assumption sensitivity analysis, not a precise empirical break-even estimate. The model's job is to show what would have to be true for the investment to break even, not to claim the actual probability improvement is known.

## 5. Figure Specification

One figure, required by the assignment and by Professor Stauffer's feedback, built from whatever survives the research tasks in Section 3:

- **X-axis:** assumed improvement in probability of successful commercial development (`Δp`).
- **Y-axis:** expected public net value of the investment (`Δp × V_public − C`).
- **Reference line/point:** the zero/break-even crossing.
- **Multiple curves:** lower, base, and higher defensible assumed values of `V_public`, each producing its own break-even point.
- **Assumptions visible:** every assumed value used (for `C`, `V_public` scenarios, and any `Δp` range) must be stated on the chart or in its caption, not left implicit.
- The chart's purpose is to show what would have to be true for the public investment to pay off — it must not imply that the actual probability improvement is known.

## 6. Recommendation Framework

Not a recommendation. This section names the candidate conditions the research will test; which of them, if any, hold is an empirical question to be settled by the research in Section 3.

Candidate conditions identified by Professor Stauffer, to be tested rather than assumed:

- Whether publicly funded characterization information is made broadly accessible (Data Sources row 6).
- How publicly created value is shared with the public and host communities, including Native Hawaiians (Data Sources row 8).

The eventual recommendation must be written as conditions on continuing the program (e.g., continued funding justified if X and Y hold, not justified or justified differently otherwise), consistent with the decision-maker and decision named in Section 1. No recommendation is written into this spec.

## 7. Success Criteria / Validation Rules

The research and resulting paper should be checked against the following before being considered complete:

- Every quantitative input used in the model or figure has a cited primary source and retrieval date recorded in `data/sources.md`.
- `C` is not used in any calculation until Data Sources row 1 is verified.
- `Δp` is either backed by a genuinely defensible source, or is explicitly presented as a varied assumption — never presented as a known quantity.
- `V_public` excludes private developer return and total project value in every use.
- The figure shows the break-even crossing and at least three `V_public` scenarios (lower/base/higher), with assumptions stated visibly.
- The private-incentive-sufficiency test and the information-accessibility test are both addressed with evidence, not assumed.
- The recommendation is stated as conditions on continued funding, not as a flat yes/no, and is not predetermined by this spec.
- The paper stays within the four-page limit (Section 8).

## 8. Scope Note

The final paper is four pages maximum, excluding title page, graphs, bibliography, and appendix. Every section above should be read with that constraint in mind: two primary economic concepts (information/incentives and market failure; distribution/capture of value), one quantitative method (stated-assumption sensitivity analysis), one figure, and one conditional recommendation. Research tasks that would require building a second, independently rigorous model (for example, a fully quantified distributional model alongside the break-even sensitivity model) should be treated as evidence-gathering for the Recommendation Framework, not as a second parallel analysis.

## 9. Research Log

Dated entries recording what was actually found or not found during research, including honest gaps — not a place to record conclusions in advance of the evidence.

**2026-09-25 — Spec established.** This spec was written before full research execution, consistent with the course workflow and Professor Stauffer's latest instructions to source, verify, build, and recommend in sequence. Key unresolved empirical items at this point: `C` (the $5 million figure) is unverified against a primary source; `V_public`'s components are undefined and unsourced; whether a defensible `Δp` estimate exists anywhere is unknown. No data has been pulled and no sources have been retrieved as of this entry.

**2026-09-25 — `C` verified (Research Step 1 complete).** `C = $5,000,000` is now verified against two independent primary sources: Hawaiʻi State Energy Office testimony (Mar. 25, 2025, re: SCR 136) confirming a 2024 allocation from the Coronavirus State Fiscal Recovery Fund for slim-hole geothermal resource characterization, allocated by Governor Josh Green; and a corroborating University of Hawaiʻi Office of Research Services award record (BOR Consolidated Q1 FY2025) showing a matching $5,000,000 HSEO-sponsored award to the UH Hawaiʻi Institute of Geophysics and Planetology for slim-hole subsurface/resource characterization. Both sources and retrieval dates are recorded in `data/sources.md`. Both sources have been independently re-verified against the official URLs listed in `data/sources.md`. Raw copies of both PDFs are not preserved locally, because downloading was unavailable in this environment. `Δp`, `V_public`, the figure, and the recommendation remain unresolved and are not addressed by this entry.

---

**Source-management convention (established here, not yet in use):**

- `data/sources.md` will serve as the master source/provenance log for this engagement, once created.
- Primary documents used materially in the analysis — funding, legislative, testimony, or official assessment documents in particular — should be preserved in `data/raw/` when practical.
- Each row in `data/sources.md` should record: the claim/input it supports, the issuing organization, the document title, the URL, the retrieval date, verification status, and the local raw-file path in `data/raw/` where applicable.
- Neither `data/sources.md` nor `data/raw/` exists yet; this convention is recorded here for approval before either is created.
