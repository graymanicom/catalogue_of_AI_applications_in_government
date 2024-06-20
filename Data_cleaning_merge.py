"""
In our first filtering we had not realised that "Central-government" and "Central-Government" were both values of the "Responsible Organisation category" feature.
Since we had already done labelling of relevance, we did not want to simply re-do the filtering correctly.
Therefore we used this script to filter the "Central-government" examples, apply the other filters, and merge the two docs. 
"""

import pandas as pd

# Load the datasets
pstw_dataset_path = 'PSTW datasets - last modified 30 May 2024/PSTW_Dataset.xlsx'
step_1_filtered_path = 'Step_1_filter/Dataset_filtered_step_1.xlsx'

# Read the datasets
pstw_df = pd.read_excel(pstw_dataset_path)
print(f"pstw dataset shape: {pstw_df.shape}")
step_1_filtered_df = pd.read_excel(step_1_filtered_path)
print(f"Initial dataset shape: {step_1_filtered_df.shape}")

# Filter rows with 'Central-government' in 'Responsible Organisation category'
central_gov_df = pstw_df[pstw_df['Responsible Organisation category'] == 'Central-government']
print(f"pstw filtered dataset shape: {central_gov_df.shape}")

# clean the data
central_gov_df['Responsible Organisation category'] = central_gov_df['Responsible Organisation category'].replace('Central-government', 'Central-Government')

# Apply the filtering criteria
filter_conditions = (
    central_gov_df['Responsible Organisation category'].isin([
        'Academic-research', 'Central-Government', 'Local Government', 'Regional Government'
    ]) &
    (central_gov_df['Status'].isin([
        'Implemented', 'In development', 'Pilot', 'Planned'
    ])) &
    (central_gov_df['Cross Border'] == 'No') &
    (central_gov_df['Technology'] == 'Artificial Intelligence') &
    (central_gov_df['Date-updated'] <= '2024-05-30')
    )

filtered_central_gov_df = central_gov_df[filter_conditions].copy()

# Concatenate the filtered rows to the step 1 filtered dataset
updated_df = pd.concat([step_1_filtered_df, filtered_central_gov_df], ignore_index=True)

# Save the updated dataframe to a new file
output_path = 'Step_1_filter/Dataset_filtered_step_1_updated.xlsx'
updated_df.to_excel(output_path, index=False)

print(f"Final dataset shape: {updated_df.shape}")

print(f"Updated dataset saved to {output_path}")
