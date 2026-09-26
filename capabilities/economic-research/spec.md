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

Every row below is a research requirement, not a finding. Status starts at **Pending** for all rows and should only change to **Verified** once a primary source and retrieval date are actually recorded (in `data/sources.md` — see Section 9 and the source-management convention below), or to **Partially Supported** when the evidence gathered bears on the question but does not fully resolve it — partial status still requires cited, recorded sources; it is not a lower sourcing bar, only an honest description of what the evidence establishes.

| # | Item | Status | Source | Retrieval Date | Notes |
|---|---|---|---|---|---|
| 1 | $5 million allocation amount and fund | Verified | Hawaiʻi State Energy Office — Testimony of Mark B. Glick before the Senate Committee on Energy and Intergovernmental Affairs re: SCR 136 (Mar. 25, 2025); corroborated by University of Hawaiʻi Office of Research Services, BOR Consolidated Q1 FY2025 | 2026-09-25 | Confirms $5,000,000 from the Coronavirus State Fiscal Recovery Fund, allocated in 2024 by Governor Josh Green, for slim-hole geothermal resource characterization; corroborated by a matching $5,000,000 HSEO-sponsored UH award for the same purpose. Full citations in `data/sources.md`. |
| 2 | Program purpose / use of funds | Pending | TBD | TBD | What the allocation is authorized to be spent on (e.g., slim-hole drilling, resource characterization scope). |
| 3 | Legislative activity concerning continuation/future funding | Verified (scope: SB 3081 status only) | Hawaiʻi State Legislature — SB 3081 (2026); see `data/sources.md` row 6 | 2026-09-25 | SB 3081 passed House second reading (Mar. 19, 2026) and was referred to the House Water & Land Committee; no Act number is on record as of the retrieval date — not enacted as of that date. Its accessibility provisions are legislative intent only, not current law, and do not govern the existing $5M project. Broader legislative-activity research (e.g., SB 1068 or successor bills) may continue if the Recommendation Framework needs it. |
| 4 | Geothermal resource characterization / resource evidence | Pending | TBD | TBD | UH/state geothermal resource assessments; USGS or comparable federal assessments where relevant. |
| 5 | Private incentives / private provision of comparable characterization | Pending | TBD | TBD | Evidence bearing on whether private developers already have sufficient incentive to fund comparable characterization without public support. |
| 6 | Accessibility / public availability of publicly funded characterization information | Partially Supported | DBEDT Non-General Fund Report (S-276-B); HSEO geothermal program page; current-project Statement of Work (identity only); SB 3081 status — see `data/sources.md` rows 3, 4, 5, 6 | 2026-09-25 | The current $5M program is structured to produce analyzed and published information (DBEDT Fund Measures #6–7: "data analysis and publication," "report of findings"), and official sources frame characterization as supporting broader resource understanding rather than one developer. However, no primary source confirms that the underlying characterization *data* (as opposed to summarized findings) will be released, where, in what form, or to whom. The current-project SOW's own release terms are unverified. SB 3081's accessibility language does not govern this program and is not enacted. Do not move this row to fully Verified without evidence closing that gap. |
| 7 | Defensible components of `V_public` | Partially Supported | HRS §182-7; HRS §182-18; HAR §13-183-31; PGV/KLP royalty precedent (secondary sources) — see `data/sources.md` rows 7–10 | 2026-09-26 | Several genuine public-value categories identified (royalty revenue; avoided fossil-fuel/ratepayer benefit; avoided emissions damages; energy-security/reliability — qualitative only), but none supports a single observed Hawaiʻi-specific dollar `V_public`. Royalty revenue is the strongest directly observable component but is scenario-dependent, not a fixed base case: HAR §13-183-31 sets a 10–20% range on geothermal-resource value at the wellhead, while HRS §182-7 and §182-18 contain separate BLNR rate-setting/waiver authority whose interaction with that rule is unresolved; WebSearch-derived evidence indicates §182-18 may authorize a full royalty waiver for up to eight years, but this has not yet been directly verified against official statutory text. The one operating Hawaiʻi precedent (PGV) reportedly yields only ~3% of gross revenue to the State — observed practice should not be assumed to equal the administrative-rule range. Avoided-fuel-cost and avoided-emissions components are plausible but require additional unsourced assumptions and are appropriate only as sensitivity components. Private developer PPA revenue is explicitly excluded. `V_public` must be represented through transparent stated assumptions/sensitivity cases rather than a single precisely observed value; do not force royalty revenue alone to define it. |
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

**2026-09-25 — Research Step 2: Partially Supported.** Investigated whether the current $5M program's characterization information is broadly accessible and useful beyond the first/private developer (Data Sources row 6). The evidence reasonably supports that publicly funded geothermal characterization can produce information useful beyond a single developer, including for state resource understanding, utility planning, and subsequent private-sector development. For the current $5M program specifically, DBEDT's "data analysis and publication" language (Fund Measures #6–7) indicates an intent to publish some project output. However, it has not been verified what "publication" requires, whether underlying characterization data or only summarized findings will be released, where they will be available, or whether they will be broadly accessible/reusable by other developers and stakeholders. SB 3081 was investigated: it passed House second reading (Mar. 19, 2026) and was referred to the House Water & Land Committee, with no Act number on record as of the retrieval date — **not enacted** as of that date. Its accessibility provisions are evidence of proposed legislative design/intent only and do not govern the current program (Data Sources row 3). Two categories of evidence were deliberately kept out of this row's formal sourcing: older HGGRC/Play Fairway public-data infrastructure (a different, DOE-funded project — institutional precedent only, not evidence for the current program) and reporting on the project's drilling timeline (contextual only, explains why output may not yet exist but does not establish accessibility either way). Data Sources row 6 remains **Partially Supported**, not Verified.

**2026-09-26 — Research Step 3: `V_public` components — Partially Supported.** Investigated defensible categories of public economic value for `V_public` (Data Sources row 7). Four categories were tested: geothermal royalty revenue (HRS §182-7, §182-18; HAR §13-183-31), avoided fossil-fuel/ratepayer benefit (PUC avoided-cost framework; PGV PPA precedent), avoided emissions damages (a Hawaiʻi-specific UHERO/HSEO carbon-price study, Act 122 SLH 2019), and energy security/reliability/diversification (HSEO/DBEDT testimony). Private developer PPA revenue (e.g., PGV's own PPA) was tested and confirmed excluded, as required by definition.

Royalty revenue is the strongest directly observable Hawaiʻi-specific public-value mechanism but is not suitable as a single fixed base-case dollar value. HAR §13-183-31 sets a 10–20% range applied to geothermal-resource value at the wellhead, while HRS §182-7 (board sets/readjusts the rate before and during a lease) and §182-18 (board may fix a rate "to encourage production" and may waive royalties entirely for up to eight years) contain separate BLNR rate-setting/waiver authority whose interaction with that administrative-rule range has not been resolved by this research. The one operating Hawaiʻi precedent — the State's geothermal mining lease with Kapoho Land Partnership, subleased to Puna Geothermal Venture — reportedly yields approximately 3% of gross revenue to the State, well below the rule's nominal range; this demonstrates that observed practice should not be assumed to equal that range. The 3% figure and PGV's private-land tenure come from secondary sources (news reporting, SEC filings), not primary government lease records, and remain independently unverified.

Avoided fossil-fuel/ratepayer benefit and avoided emissions damages are both plausible public-value categories with real Hawaiʻi-specific mechanisms and reference points, but each requires additional assumptions this research did not resolve (future generation price and counterfactual fuel cost; quantity of emissions displaced) and are appropriate only as sensitivity components, not observed program-specific values. Energy security/reliability/diversification is supported qualitatively but has no defensible dollar valuation and stays qualitative.

As with prior steps, the primary legal texts (HRS, HAR) were located via WebSearch synthesis in this environment — direct fetch to official state sites remains blocked — and have not yet been independently read in full; the PGV ~3% figure and land-tenure characterization rest on secondary sources only. Both should be independently verified before being treated as fully Verified in `data/sources.md`.

`V_public` must be represented through transparent stated assumptions and sensitivity cases rather than a single precisely observed Hawaiʻi-specific value; royalty revenue alone should not be forced to serve as its entire definition. Unresolved and explicitly not solved by assumption: the interaction among HRS §182-7, §182-18, and HAR §13-183-31; future plant capacity/generation; future wellhead resource value; future royalty rate; land tenure/DHHL applicability for any candidate site; the OHA/ceded-land distribution question (a lead for Row 8, not pursued further here); future PPA/counterfactual fuel price; and emissions quantity displaced. Data Sources row 7 remains **Partially Supported**.

---

**Source-management convention (established here, not yet in use):**

- `data/sources.md` will serve as the master source/provenance log for this engagement, once created.
- Primary documents used materially in the analysis — funding, legislative, testimony, or official assessment documents in particular — should be preserved in `data/raw/` when practical.
- Each row in `data/sources.md` should record: the claim/input it supports, the issuing organization, the document title, the URL, the retrieval date, verification status, and the local raw-file path in `data/raw/` where applicable.
- Neither `data/sources.md` nor `data/raw/` exists yet; this convention is recorded here for approval before either is created.
