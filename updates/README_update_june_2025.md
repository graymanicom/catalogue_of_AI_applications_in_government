# PSTW Dataset Update and Filtering Process

### Overview
This document describes the steps taken to update and filter the PSTW dataset, ensuring accuracy and relevance. The process involved comparing datasets, manual inspection of cases, and applying systematic filtering and ranking methods.

---

### What we Did:

1. **Downloaded the Latest Dataset**
   - The latest version of the PSTW dataset was downloaded, with the last update dated **June 2025**.

2. **Comparison of Datasets**
   - Started with two datasets:
     - `PSTW_Dataset.csv` (May Dataset)
     - `PSTW_Dataset_0.csv` (November Dataset)
   - Filtered and combined the datasets to create `Filtered_PSTW_Dataset_0.csv`.

3. **Initial Filtering**
   - Narrowed the dataset down to **82 cases**.

4. **Manual Inspection**
   - Manually reviewed the **82 cases** due to slight variations in their wording. 
   - Some cases, already present in the May dataset, were mistakenly identified as "new cases" due to minor title differences. These duplicates were identified and removed.
   - This resulted in a total of **51 new cases**.

5. **Step 1a Filter**
   - Applied `Step1a_filter` to the dataset (minor modifications were made to the Python script).
   - Trimmed the dataset down to **34 cases**.

6. **Ranking System**
   - A ranking system was applied to the **34 cases**.
   - Further reduced the dataset to **25 cases** by removing **9 irrelevant cases**.

7. **Step 1b Filter**
   - Applied `Step1b_filter` to remove additional irrelevant cases.

8. **Addition of New Cases**
   - Incorporated cases from **'AI Tools for Catalogue Nov 2024 update.xlsx'** into the dataset of **25 cases**.

9. **Sorting**
   - Performed `Step_3_sort` on the dataset to organize it systematically.

---

### Final Result
- The final filtered dataset includes **38 cases** that were thoroughly reviewed, filtered, and ranked.

---

### Notes:
- Each step of the process was carefully documented and verified to ensure accuracy.
- The Python scripts used for filtering (`Step1a_filter` and `Step1b_filter`) were slightly modified to suit the updated requirements.
- The resulting dataset is ready for further analysis or integration into other processes.

---
# Appendix

## List of PSTW IDs deleted in step 1b
PSTW-2158
PSTW-2164,PSTW-2167,PSTW-2197,PSTW-2201,PSTW-2204,PSTW-2208,PSTW-2209,PSTW-2214.

