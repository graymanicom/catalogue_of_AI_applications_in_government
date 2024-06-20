# ********************** Objective *******************************
""" 
The purpose of this script is to filter PSTW_dataset from AI watch and then to export a new filtered dataset for further analysis.
We add a 'Deletion Flag' column which we will manually label with 0 or 1.
"""

# ******************* Arguments ********************************
import argparse
import os
parser = argparse.ArgumentParser(description="Filter dataset based on specified criteria and save to Excel and CSV formats.")
parser.add_argument('input_path', type=str, nargs='?', help="Path to PSTW_Dataset.xlsx.", default = os.getcwd() + '/PSTW_Dataset.xlsx')
parser.add_argument('output_directory', type=str, nargs='?', help="Directory to save the output files.", default=os.getcwd())
args = parser.parse_args()

# ******************* Parameters ********************************
output_name = 'Dataset_filtered_step_1'

# ******************* Packages ********************************
import pandas as pd

# ********************** Code **********************************
# Load the dataset
df = pd.read_excel(args.input_path)

# Print the initial shape of the dataset
print(f"Initial dataset shape: {df.shape}")

# clean the data
df['Responsible Organisation category'] = df['Responsible Organisation category'].replace('Central-government', 'Central-Government')

# Apply the filtering criteria
filter_conditions = (
    df['Responsible Organisation category'].isin([
        'Academic-research', 'Central-Government', 'Local Government', 'Regional Government'
    ]) &
    (df['Status'].isin([
        'Implemented', 'In development', 'Pilot', 'Planned'
    ])) &
    (df['Cross Border'] == 'No') &
    (df['Technology'] == 'Artificial Intelligence') &
    (df['Date-updated'] <= '2024-05-30')
    )

filtered_df = df[filter_conditions].copy()
# Add the 'Relevance Flag' column and set to 0 for all rows initially
filtered_df.loc[:, 'Relevance Flag'] = 0

# Sanity check: 
print(f"Filtered dataset shape: {filtered_df.shape}")

# Save the filtered dataset as Excel and csv
filtered_df.to_excel(args.output_directory + '/' + output_name + '.xlsx', index=False)
filtered_df.to_csv(args.output_directory + '/' + output_name + '.csv', index=False)

print("Filtered dataset has been saved to both Excel and CSV formats.")