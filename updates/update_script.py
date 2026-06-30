import pandas as pd

# Define file paths
curated_path = '/Users/graym/Library/CloudStorage/OneDrive-StellenboschUniversity/Stellenbosch/Digital tools/Catalogue of AI tools for government/December 2025/Curated_dataset_June_2025.xlsx'
update_path_1 = '/Users/graym/Library/CloudStorage/OneDrive-StellenboschUniversity/Stellenbosch/Digital tools/Catalogue of AI tools for government/December 2025/AI Tools Database November 2025.xlsx'
output_path = '/Users/graym/Library/CloudStorage/OneDrive-StellenboschUniversity/Stellenbosch/Digital tools/Catalogue of AI tools for government/December 2025/Curated_dataset_Dec_2025.xlsx'

ID_COL = "ID"
INTERACTION_COL = "Interaction"

# Load datasets
curated_df = pd.read_excel(curated_path)
update_1_df = pd.read_excel(update_path_1)

# Ensure consistent columns: only those in curated_df
common_columns = curated_df.columns.tolist()
update_1_df = update_1_df.loc[:, update_1_df.columns.isin(common_columns)]
update_1_df = update_1_df.reindex(columns=common_columns)


def pick_first_non_empty(series: pd.Series):
    """
    For collapsing multiple rows with the same ID inside ONE dataset:
    return the first non-null and non-blank value, else NA.
    """
    for val in series:
        if pd.notna(val) and str(val).strip() != "":
            return val
    return pd.NA


def collapse_by_id(df: pd.DataFrame):
    """
    For a given df, return:
      - df_id: one row per ID (collapsed using pick_first_non_empty)
      - df_no_id: rows where ID is missing
    """
    if ID_COL not in df.columns:
        return df.copy(), pd.DataFrame(columns=df.columns)

    df = df.copy()
    df_with_id = df[df[ID_COL].notna()]
    df_no_id = df[df[ID_COL].isna()]

    if df_with_id.empty:
        return df_with_id, df_no_id

    agg_dict = {col: pick_first_non_empty for col in df.columns if col != ID_COL}

    df_with_id = (
        df_with_id
        .groupby(ID_COL, as_index=False)
        .agg(agg_dict)
    )

    return df_with_id, df_no_id


# 1) Collapse multiple rows with the same ID within each source
curated_by_id, curated_no_id = collapse_by_id(curated_df)
update_by_id, update_no_id = collapse_by_id(update_1_df)

# 2) Merge curated and update rows by ID
if ID_COL in curated_by_id.columns and ID_COL in update_by_id.columns:
    merged_by_id = curated_by_id.merge(
        update_by_id,
        on=ID_COL,
        how='outer',
        suffixes=('_cur', '_upd')
    )

    def choose_value(update_val, curated_val):
        """
        Cell-level rule:
        - If update value is non-empty → use it
        - Else use curated value
        - Else NA
        """
        if pd.notna(update_val) and str(update_val).strip() != "":
            return update_val
        if pd.notna(curated_val) and str(curated_val).strip() != "":
            return curated_val
        return pd.NA

    # Build final one-row-per-ID table using the choose_value rule
    combined_id_data = {}
    combined_id_data[ID_COL] = merged_by_id[ID_COL]

    for col in common_columns:
        if col == ID_COL:
            continue

        cur_col = f"{col}_cur"
        upd_col = f"{col}_upd"

        cur_series = merged_by_id[cur_col] if cur_col in merged_by_id.columns else pd.Series([pd.NA] * len(merged_by_id))
        upd_series = merged_by_id[upd_col] if upd_col in merged_by_id.columns else pd.Series([pd.NA] * len(merged_by_id))

        combined_id_data[col] = [
            choose_value(u, c) for u, c in zip(upd_series, cur_series)
        ]

    combined_by_id_df = pd.DataFrame(combined_id_data, columns=common_columns)

else:
    # Fallback: if ID not present for some reason
    combined_by_id_df = pd.concat([curated_by_id, update_by_id], ignore_index=True)

# 3) Add rows without IDs from both sources
null_id_df = pd.concat([curated_no_id, update_no_id], ignore_index=True)
combined_df = pd.concat([combined_by_id_df, null_id_df], ignore_index=True)

# 4) Clean Interaction column: keep only G2C, G2G, G2B
valid_codes = ["G2C", "G2G", "G2B"]

def clean_interaction(value):
    if pd.isna(value):
        return pd.NA
    text = str(value).upper()

    found = [code for code in valid_codes if code in text]

    # Remove duplicates while preserving order
    seen = set()
    unique_found = []
    for code in found:
        if code not in seen:
            seen.add(code)
            unique_found.append(code)

    return "; ".join(unique_found) if unique_found else pd.NA

if INTERACTION_COL in combined_df.columns:
    combined_df[INTERACTION_COL] = combined_df[INTERACTION_COL].apply(clean_interaction)
else:
    print(f"Warning: interaction column '{INTERACTION_COL}' not found in combined_df")

# 5) Remove rows where "Responsible Organisation category" is "Private Sector"
if "Responsible Organisation category" in combined_df.columns:
    combined_df = combined_df[
        ~combined_df["Responsible Organisation category"]
        .astype(str)
        .str.strip()
        .str.lower()
        .eq("private sector")
    ]
else:
    print("Warning: 'Responsible Organisation category' column not found; no filtering applied.")

# 6) Make ID the first column
cols = combined_df.columns.tolist()
if ID_COL in cols:
    cols.remove(ID_COL)
    cols = [ID_COL] + cols
    combined_df = combined_df[cols]

# 7) Sort alphabetically by ID (IDs without value go last)
if ID_COL in combined_df.columns:
    combined_df = combined_df.sort_values(by=ID_COL, ascending=True, na_position='last')

# 8) Save to Excel
combined_df.to_excel(output_path, index=False)
print(f"Merged dataset saved successfully at {output_path}")