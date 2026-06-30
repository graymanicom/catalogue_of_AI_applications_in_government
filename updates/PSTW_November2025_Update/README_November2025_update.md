# PSTW Catalogue Update - November 2025

## Overview
This document outlines the full workflow used to update and filter the PSTW dataset for the November 2025 release. The process includes comparing the June 2025 and November 2025 datasets, applying automated filtering, conducting manual reviews, and incorporating newly identified cases from external GovTech and data-for-policy sources.

### Key Dates
- **Previous dataset release:** June 2025  
- **Latest dataset release:** November 2025

---

## Dataset Comparison Process
1. **Identify New Entries:** Extract items present in the November 2025 dataset but not in the June 2025 dataset.  
2. **Format Consistency:** Normalise formatting (e.g., whitespace in PSTW ID and Name columns) to ensure accurate comparison.  
3. **Output Formats:** Save filtered results in both Excel (`.xlsx`) and CSV (`.csv`) formats for auditing and analysis.  

### Automated Script: `clean_filter.py`
- **Load Datasets:** Reads `PSTW_Dataset.csv` (June 2025) and `PSTW_Dataset_0.csv` (November 2025).  
- **Whitespace Normalisation:** Ensures consistent formatting of PSTW ID and Name columns.  
- **Comparison & Filtering:** Identifies and removes duplicates based on `(PSTW ID, Name)` pairs.  
- **Output:** Produces **`Filtered_PSTW_Dataset_0.xlsx`** (206 entries) in the designated output directory.  

---

## Filtering Steps

Before describing **Step 1a Filter**, it is important to clarify where the filtering workflow occurs and how the required input file is prepared.

All filtering and transformation steps take place in the following directory:

**`PSTW_November2025_Update/Next Step`**

---

### Preparing the Input for Step 1a

The **Step 1a Filter** process expects an input file named:

**`PSTW_Dataset.xlsx`**

This file is *not* created manually. Instead, it must be generated and prepared through the following steps:

1. Run the preprocessing script **`clean_filter.py`**, which outputs:  
   - **`Filtered_PSTW_Dataset_0.xlsx`**
2. **Rename** this output file to:  
   - **`PSTW_Dataset.xlsx`**
3. Move the renamed file into:  
   - **`PSTW_November2025_Update/Next Step`**

The renamed file (`PSTW_Dataset.xlsx`) is the required input for **Step 1a Filter**.

---

### Step 1a Filter
- Applied the `Step1a_filter` script (with minor modifications).  
- Reduced the dataset to **94 cases**.

### Ranking System
A ranking mechanism was applied to the 94 cases:
- **0** – Relevant to South Africa; keep  
- **1** – Not relevant; remove  
- **2** – Very relevant; review carefully  
- **3** – Highly relevant for Policy Innovation Lab projects  
- **4** – Not very relevant  

### Step 1b Filter
- Applied `Step1b_filter` to remove additional irrelevant cases.  
- Removed **16 cases**, resulting in **78 cases**.

---

### Addition of New Cases
- Added **29 new cases** to `Other AI Tools.xlsx`, sourced from publicly available GovTech and data-for-policy repositories, including:

  - **KitSoft GovTech Case Studies** — Liquio-based low-code + AI solutions for rapid deployment of government and city services:  
    https://kitsoft.ua/projects

  - **Data to Policy Navigator – Use Cases** — Global examples of data innovations (citizen science, social media, geospatial data, etc.) applied to policy design and implementation:  
    https://www.datatopolicy.org/use-cases

  - **MomConnect** — South Africa’s maternal-health mobile messaging service:  
    https://www.health.gov.za/momconnect/

  - **Ask-a-Metric** — IDinsight’s WhatsApp-based AI data-analysis assistant:  
    https://www.idinsight.org/article/ask-a-metric-your-ai-data-analyst-on-whatsapp/

  - **GepBot** — A conversational AI assistant for accessing government information and services:  
    https://gepbot.com/

  - **Lesedi AI** — Palindrome Data’s AI platform for analytics and decision support:  
    https://www.palindromedata.com/lesedi-ai-platform/

---

### Sorting
- Applied `Step_3_sort` to organise the dataset consistently and systematically.

---

## Final Result
- After filtering, ranking, adding new cases, and sorting, the final dataset contains **107 cases**.

The final combined dataset of cases is saved in the file:

**`AI Tools Database November 2025`**

---

## Notes
- **Documentation:** Each step was carefully documented and verified.  
- **Script Modifications:**  
  - In `Step1a_filter`, the column name `'Technology'` was updated to `'Primary Technology'` to match the latest PSTW public dataset schema.  
- **Data Source:** Official PSTW dataset available at:  
  https://data.jrc.ec.europa.eu/dataset/e8e7bddd-8510-4936-9fa6-7e1b399cbd92

---

## Appendix
### PSTW IDs Deleted in Step 1b
- `PSTW-90`  
- `PSTW-169`  
- `PSTW-2439`  
- `PSTW-2500`  
- `PSTW-2504`  
- `PSTW-2528`  
- `PSTW-2531`  
- `PSTW-2544`  
- `PSTW-2547`  
- `PSTW-2556`  
- `PSTW-2557`  
- `PSTW-2571`  
- `PSTW-2577`  
- `PSTW-2580`  
- `PSTW-2581`  
- `PSTW-2583`

