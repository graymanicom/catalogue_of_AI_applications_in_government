# ********************** Objective *******************************
""" 
The purpose of this script is to take an Excel file with a 'Relevance Flag' column and to delete the rows marked for deletion.
Relevance Flags: 
1 - deletion
2 - particular interest for SA
3 - particular interest for citizen-generated open data
4 - not worth deleting but probably not worth considering in SA at the current time
Save the PSTW IDs that got deleted. 
"""

# ******************* Arguments ********************************
import argparse
import os
parser = argparse.ArgumentParser(description="Filter dataset based on specified criteria and save to Excel and CSV formats.")
parser.add_argument('input_path', type=str, nargs='?', 
                   help="Path to Dataset_filtered_step_1.xlsx", 
                   default=os.getcwd() + '/Dataset_filtered_step_1.xlsx')
parser.add_argument('output_directory', type=str, nargs='?', 
                   help="Directory to save the output files.", 
                   default=os.getcwd())


args = parser.parse_args()

# ******************* Parameters ********************************
output_dataset_name = 'Dataset_filtered_step_1b'
deleted_ids_csv_name = 'Deleted_PSTW_IDs.csv'

# ******************* Packages ********************************
import pandas as pd

# ******************* Code ********************************
# Load the modified dataset with deletion flags
if 'Dataset_filtered_step_1.xlsx' not in args.input_path:
    df = pd.read_excel(args.input_path + '/Dataset_filtered_step_1.xlsx')
else:
    df = pd.read_excel(args.input_path)

print("Initial DF shape: ",df.shape)

# Filter out the rows
deleted_rows = df[(df['Relevance Flag'] == 1) | (df['Relevance Flag'] == 4)]
non_deleted_rows = df[(df['Relevance Flag'] == 0) | (df['Relevance Flag'] == 2) | (df['Relevance Flag'] == 3)]

# Save the dataframe of non-deleted rows
non_deleted_rows.to_excel(args.output_directory + '/' + output_dataset_name + '.xlsx', index=False)
non_deleted_rows.to_csv(args.output_directory + '/' + output_dataset_name + '.csv', index=False)

print("Final DF shape: ",non_deleted_rows.shape)

# Save the deleted PSTW IDs to a CSV file
deleted_ids = deleted_rows['PSTW ID'].tolist()
deleted_ids_df = pd.DataFrame(deleted_ids, columns=['Deleted PSTW ID'])
deleted_ids_df.to_csv(args.output_directory + '/' + deleted_ids_csv_name, index=False)

print("Num PSTW IDs saved: ",deleted_ids_df.shape)

print(f"Non-deleted rows have been saved to {output_dataset_name} and deleted IDs to {deleted_ids_csv_name}")