import pandas as pd

# Define file paths
curated_path = '/Users/graym/Library/CloudStorage/OneDrive-StellenboschUniversity/Stellenbosch/Digital tools/Catalogue of AI tools for government/December 2025/Curated_dataset_June_2025.xlsx'
update_path_1 = '/Users/graym/Library/CloudStorage/OneDrive-StellenboschUniversity/Stellenbosch/Digital tools/Catalogue of AI tools for government/December 2025/AI Tools Database November 2025.xlsx'
#update_path_2 = '/Users/graym/Library/CloudStorage/OneDrive-StellenboschUniversity/Stellenbosch/Digital tools/Catalogue of AI tools for government/June 2025/June 2025 update PSTW.xlsx'
output_path = '/Users/graym/Library/CloudStorage/OneDrive-StellenboschUniversity/Stellenbosch/Digital tools/Catalogue of AI tools for government/December 2025/Curated_dataset_Dec_2025.xlsx'

# Load datasets
curated_df = pd.read_excel(curated_path)
update_1_df = pd.read_excel(update_path_1)
#update_2_df = pd.read_excel(update_path_2)


# Ensure all DataFrames share consistent column names (particularly the first column) and don't add new
# columns that are not in the curated dataset (PSTW update has new fields)
# Ensure only columns from curated_df are retained explicitly
common_columns = curated_df.columns.tolist()

# Explicitly select only common columns, dropping unwanted columns
update_1_df = update_1_df.loc[:, update_1_df.columns.isin(common_columns)]
#update_2_df = update_2_df.loc[:, update_2_df.columns.isin(common_columns)]

july_update_df = update_1_df.reindex(columns=common_columns)
#june_update_df = update_2_df.reindex(columns=common_columns)
# Concatenate datasets
combined_df = pd.concat(
    [curated_df, update_1_df], ignore_index=True)
#    [curated_df, update_1_df, update_2_df], ignore_index=True)

# Remove duplicates
combined_df.drop_duplicates(inplace=True)

# Remove rows where "Responsible Organisation category" is "Private Sector"
combined_df = combined_df[
    ~combined_df["Responsible Organisation category"]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("private sector")
]

# Save to Excel
combined_df.to_excel(output_path, index=False)

print(f"Merged dataset saved successfully at {output_path}")
