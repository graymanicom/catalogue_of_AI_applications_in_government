# ******************* Arguments ********************************
import argparse
import os
parser = argparse.ArgumentParser(description="Filter dataset based on specified criteria and save to Excel and CSV formats.")
parser.add_argument('dataset_path', type=str, nargs='?', help="Path to PSTW_Dataset_June2025.", default = os.getcwd() + '/PSTW_Dataset.csv')
parser.add_argument('dataset_0_path', type=str, nargs='?', help="Path to PSTW_Dataset_Nov2025.", default = os.getcwd() + '/PSTW_Dataset_0.csv')
parser.add_argument('output_path', type=str, nargs='?', help="Directory to save the output files.", default=os.getcwd())
args = parser.parse_args()

# ******************* Parameters ********************************
output_name = 'Filtered_PSTW_Dataset_0'

# ******************* Packages ********************************
import pandas as pd


# ********************** Code **********************************

# Load the datasets
pstw_dataset = pd.read_csv(args.dataset_path) # Nov2024 Dataset
pstw_dataset_0 = pd.read_csv(args.dataset_0_path)  # June2025 Dataset

# Function to normalize whitespace
def normalize_whitespace(text):
    if isinstance(text, str):
        return ' '.join(text.split())
    return text

# Normalize whitespace in relevant columns for both datasets
pstw_dataset_0['PSTW ID'] = pstw_dataset_0['PSTW ID'].str.strip().apply(normalize_whitespace)
pstw_dataset_0['Name'] = pstw_dataset_0['Name'].str.strip().apply(normalize_whitespace)

pstw_dataset['PSTW ID'] = pstw_dataset['PSTW ID'].str.strip().apply(normalize_whitespace)
pstw_dataset['Name'] = pstw_dataset['Name'].str.strip().apply(normalize_whitespace)

# Filter out rows in PSTW_Dataset_0 that aren't in PSTW_Dataset based on 'PSTW ID' and 'Name'
filtered_dataset_0 = pstw_dataset_0[~pstw_dataset_0[['PSTW ID', 'Name']].apply(tuple, axis=1).isin(
    pstw_dataset[['PSTW ID', 'Name']].apply(tuple, axis=1)
)]



# Save the filtered dataset as Excel and csv
filtered_dataset_0.to_excel(args.output_path + '/' + output_name + '.xlsx', index=False)
filtered_dataset_0.to_csv(args.output_path + '/' + output_name + '.csv', index=False)

print(f"Filtered dataset saved to: {args.output_path}")