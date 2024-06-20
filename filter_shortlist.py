# ******************* Arguments ********************************
import argparse
import os
parser = argparse.ArgumentParser(description="Filter dataset based on specified criteria and save to Excel and CSV formats.")
parser.add_argument('input_path', type=str, help="Path to directory containing Curated_dataset.xlsx", default = os.getcwd() + '/Dataset_sorted_step_3.xlsx')
parser.add_argument('output_directory', type=str, help="Directory to save the output files.",  default=os.getcwd())
args = parser.parse_args()


# ******************* Parameters ********************************
output_dataset_name = 'shortlist'

# ******************* Code ********************************
import pandas as pd

# Load the dataset
if 'Dataset_sorted_step_3' in args.input_path:
    file_path = args.input_path
else:
    file_path = args.input_path+'/Dataset_sorted_step_3.xlsx'

df = pd.read_excel(file_path)

print(f"Df shape: {df.shape}")

# Filter rows where 'Relevance Flag' is 2
filtered_df = df[df['Relevance Flag'] == 2]

# Save the filtered data to a new Excel file

filtered_df.to_excel(args.output_directory + '/' + output_dataset_name + '.xlsx', index=False)

# Save the filtered data to a new CSV file
filtered_df.to_csv(args.output_directory + '/' + output_dataset_name + '.csv', index=False)
print(f"Shortlist Df shape: {filtered_df.shape}")
print(f"Filtered data saved to: {args.output_directory}")

