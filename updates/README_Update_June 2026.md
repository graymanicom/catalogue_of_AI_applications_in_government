# Catalogue of AI Tools in Government — April 2026 Update

## Overview
This document details the steps taken to update and filter the PSTW dataset, ensuring accuracy and relevance. The process involved comparing the December 2025 curated dataset with the April 2026 PSTW export, followed by manual review and automated filtering, and the addition of manually sourced entries.

### Key Dates
- **Previous dataset release:** December 2025
- **Latest dataset release:** April 2026

---

## Dataset Comparison Process
1. **Identify New Entries:** Extract entries present in the April 2026 PSTW export but not in the December 2025 base dataset, comparing on PSTW ID.
2. **Format Consistency:** Normalise column names to align with the December 2025 schema (American vs. British spelling variants, leading whitespace in column headers).
3. **Output Formats:** Save filtered results in both Excel (`.xlsx`) and CSV (`.csv`) formats at each stage.

### Automated Script: `step_1a_filter_apr2026.py`
- **Load Dataset:** Reads the April 2026 PSTW export.
- **Apply Filters:** Retains only entries meeting all four criteria: Primary Technology = Artificial Intelligence; Status ∈ {Implemented, In development, Pilot, Planned}; Cross Border = No; Responsible Organisation Category ∈ {Central Government, Local Government, Regional Government, Academic-Research}.
- **Output:** Generates `Dataset_filtered_step_1` (228 entries).

---

## Filtering Steps

### Step 1a Filter
- Applied `step_1a_filter_apr2026.py` (with column name updates to match the April 2026 schema — see Notes).
- Reduced the full April 2026 export to **228 candidate entries**.

### Manual Review and Ranking (Step 1b)
- Each of the 228 entries was reviewed and assigned a relevance flag:

| Flag | Meaning |
|------|---------|
| 0 | Keep — generally relevant |
| 1 | Exclude — not relevant for this catalogue |
| 2 | Keep — specific SA / Africa interest |
| 3 | Keep — citizen data / participation interest |
| 4 | Borderline — kept with note |

- **66 entries** were excluded (Flag = 1). See Appendix for full list.
- **162 entries** were retained for inclusion in the merge step.

### Deduplication
- Retained entries were compared against the December 2025 base dataset by PSTW ID.
- **18 entries** already present in the December 2025 base were removed.
- **119 new PSTW entries** proceeded to the final merge.

### Addition of New Manual Cases
- **10 new entries** (PIL-60–PIL-69) were incorporated from `AI tool databases - future updates TC.xlsx`, covering AI tools for civic engagement, parliamentary monitoring, and conversational AI in government, sourced via desk research and generative AI-assisted search, and manually verified.
- Entries already present in the December 2025 base were excluded.

### Sorting
- Applied `step_3_sort_apr2026.py` to organise entries systematically before merge.

### Final Merge: `merge_final_apr2026.py`
- Concatenated: December 2025 base (904 entries) + new manual entries (10) + new PSTW entries (119).
- AI Keywords standardised to a single concise term per entry throughout.
- Output saved as `Final_Catalogue_Apr2026.xlsx` and `Final_Catalogue_Apr2026.csv`.

---

## Final Result
The final dataset contains **1,033 entries** after filtering, deduplication, manual review, and merge.

| Source | Count |
|--------|------:|
| December 2025 base | 904 |
| New manual entries (PIL-60–69) | 10 |
| New PSTW entries | 119 |
| **Total** | **1,033** |

---

## Observations from the April 2026 Cohort

The 129 new entries (119 PSTW + 10 manual) added since December 2025 reveal several notable patterns:

- **Generative AI has entered mainstream government use.** 49 of 129 new entries (38%) are chatbots, virtual assistants, or voicebots; 27 (21%) explicitly reference large language models or generative AI in their descriptions — compared to near-zero in the December 2025 baseline.
- **A shift toward off-the-shelf procurement.** Eight new entries are Microsoft Copilot deployments across UK and EU local councils. Governments with mature digital infrastructure are increasingly licensing existing generative AI tools rather than commissioning bespoke systems.
- **Most new AI adoption targets internal administration, not citizens.** New entries skew toward back-office productivity (internal management, 40 entries) over citizen-facing service delivery (6 entries). The AI tools with the broadest public impact tend to be the chatbot and advisory tools rather than internal process automation.
- **AI governance is emerging as a distinct category.** Two new entries — Z-Inspection (Netherlands) and IEEE CertifAIEd (Vienna) — are frameworks specifically for auditing and certifying other government AI systems for ethics and accountability. This meta-governance layer was barely represented in earlier catalogue versions.
- **Notable individual entry — Diella (PSTW-2746, Albania).** Described as the world's first AI system appointed to a cabinet-level role, overseeing public procurement. Relevant to contexts where procurement integrity is a policy priority.
- **UK leads new PSTW entries** (23 entries) despite the dataset being EU-focused, driven largely by local council Copilot rollouts.
- **Denmark** (16 entries) and **Luxembourg** (15 entries) are also prominent in the new cohort.

---

## Notes
- **Script modifications:** Three scripts were adapted from the original pipeline to handle the April 2026 schema:
  - `step_1a_filter_apr2026.py`: Column names updated (`Primary Technology` retained; `Responsible organisation category` casing variants added; ` Status` leading-space variant handled; date filter removed as no longer applicable).
  - `step_3_sort_apr2026.py`: Column names updated to American-spelling variants used in the April 2026 export (`Personalized Services`, `Public (citizen)-centered services`).
  - `merge_final_apr2026.py`: Column mapping added to translate April 2026 schema to December 2025 schema before concatenation.
- **Data source:** PSTW public dataset available [here](https://data.jrc.ec.europa.eu/dataset/e8e7bddd-8510-4936-9fa6-7e1b399cbd92).

---

## Appendix
### PSTW IDs Deleted in Step 1b (Flag = 1)

PSTW-671, PSTW-942, PSTW-945, PSTW-974, PSTW-1026, PSTW-1038, PSTW-1040, PSTW-1045, PSTW-1046, PSTW-1047, PSTW-1048, PSTW-1166, PSTW-1181, PSTW-1184, PSTW-1191, PSTW-1195, PSTW-1197, PSTW-1198, PSTW-1356, PSTW-1374, PSTW-1382, PSTW-1412, PSTW-1808, PSTW-1809, PSTW-1810, PSTW-1867, PSTW-2492, PSTW-2677, PSTW-2686, PSTW-2706, PSTW-2708, PSTW-2719, PSTW-2723, PSTW-2724, PSTW-2726, PSTW-2747, PSTW-2748, PSTW-2758, PSTW-2761, PSTW-2762, PSTW-2763, PSTW-2764, PSTW-2770, PSTW-2785, PSTW-2789, PSTW-2790, PSTW-2799, PSTW-2800, PSTW-2810, PSTW-2822, PSTW-2824, PSTW-2825, PSTW-2826, PSTW-2827, PSTW-2828, PSTW-2829, PSTW-2831, PSTW-2832, PSTW-2854, PSTW-2858, PSTW-2859, PSTW-2861, PSTW-2870, PSTW-2887, PSTW-2912, PSTW-2915
