# PSTW Catalogue Update - June 2025

## Overview
This document details the steps taken to update and filter the PSTW dataset, ensuring accuracy and relevance. The process involved comparing the November 2024 dataset with the June 2025 dataset, followed by manual inspection and automated filtering techniques.

### Key Dates
- **Previous dataset release:** 31 October 2024  
- **Latest dataset release:** June 2025  

---

## Dataset Comparison Process
1. **Identify New Entries:** Extract entries present in the June 2025 dataset but not in the November 2024 dataset.  
2. **Format Consistency:** Normalize formatting (e.g., whitespace in PSTW ID and Name columns) for accurate comparison.  
3. **Output Formats:** Save filtered results in both Excel (`.xlsx`) and CSV (`.csv`) formats for further analysis.  

### Automated Script: `clean_filter.py`
- **Load Datasets:** Reads `PSTW_Dataset.csv` (November 2024) and `PSTW_Dataset_0.csv` (June 2025).  
- **Whitespace Normalization:** Ensures consistent formatting of PSTW ID and Name columns.  
- **Comparison & Filtering:** Identifies and removes duplicate entries by comparing `(PSTW ID, Name)` tuples.  
- **Output:** Generates `Filtered_PSTW_Dataset_0` (175 entries) in the specified output directory.  

---

## Filtering Steps
### Step 1a Filter
- Applied `Step1a_filter` (with minor script modifications).  
- Reduced dataset to **20 cases**.  

### Ranking System
- Ranked the 20 cases and removed **3 irrelevant cases**, resulting in **17 cases**.  

### Step 1b Filter
- Applied `Step1b_filter` to remove additional irrelevant cases.  

### Addition of New Cases
- Incorporated **26 cases** from `May 2025 update fields.xlsx` (South African AI use cases sourced via Google and generative AI searches, manually verified).  

### Sorting
- Applied `Step_3_sort` to organize the dataset systematically.  

---

## Final Result
- The final filtered dataset contains **43 cases** after thorough review, filtering, and ranking.  

---

## Notes
- **Documentation:** Each step was carefully documented and verified for accuracy.  
- **Script Modifications:**  
  - `Step1a_filter`: Column name updated from `'Technology'` to `'Primary Technology'` to align with the latest PSTW public dataset notation.  
- **Data Source:** PSTW public dataset available [here](https://data.jrc.ec.europa.eu/dataset/e8e7bddd-8510-4936-9fa6-7e1b399cbd92).  

---

## Appendix
### PSTW IDs Deleted in Step 1b
- `PSTW-2323`  
- `PSTW-2333`  
- `PSTW-2290`  