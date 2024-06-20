# ******************* Arguments ********************************
import argparse
import os
parser = argparse.ArgumentParser(description="Filter dataset based on specified criteria and save to Excel and CSV formats.")
parser.add_argument('input_path', type=str, help="Path to Dataset_filtered_step_1b.xlsx", default = os.getcwd() + '/Dataset_filtered_step_1b.xlsx')
parser.add_argument('output_directory', type=str, help="Directory to save the output files.",  default=os.getcwd())
args = parser.parse_args()

# ******************* Parameters ********************************
output_dataset_name = 'Dataset_sorted_step_3'

# ******************* Packages ********************************
import pandas as pd

# ******************* Functions *******************************
def fill_ai_keywords(df):
    count = 0
    # Extract the AI keywords from the dataframe
    ai_keywords = df['AI Keywords'].dropna().unique()

    # Iterate over each row in the dataframe
    for index, row in df.iterrows():
        if pd.isna(row['AI Keywords']):
            # Check if any AI keyword is present in the description
            for keyword in ai_keywords:
                if keyword.lower() in row['Description'].lower():
                    count += 1
                    df.at[index, 'AI Keywords'] = keyword
                    if count < 3:
                        print(f"keyword: {keyword}")
                        print(f"description: {row['Description']}")
                    break
    print("New AI keywords: ", count)
    return df

# ******************* Code ********************************
# Load the modified dataset with deletion flags
if 'Dataset_filtered_step_1b.xlsx' not in args.input_path:
    df = pd.read_excel(args.input_path + '/Dataset_filtered_step_1b.xlsx')
else:
    df = pd.read_excel(args.input_path)

print("Initial DF shape: ",df.shape)

# clean
df = fill_ai_keywords(df)
print("AI keywords filled")

# Display the filtered DataFrame
print("Unsorted")
print(df.head())

cols_v_to_z = ["Personalised Services", "Public (citizen)-centred services", "Increase quality of PSI and services", 
               "More responsive, efficient, and cost-effective public services", "New services or channels"]
cols_ab_to_ah = ["Cost-reduction", "Responsiveness of government operation", "Improved management of public resources", 
                 "Increased quality of processes and systems", "Better collaboration and better communication", 
                 "Reduced or eliminated the risk of corruption and abuse of the law by public servants", 
                 "Enabled greater fairness, honesty, equality"]

sorted_df_3 = df.sort_values(["Improved Public Service"] + cols_v_to_z + ["Improved Administrative Efficiency"] + cols_ab_to_ah + ["AI Keywords"])
#print("Sorted 1:\n ", sorted_df_1[["Improved Public Service"] + cols_v_to_z].head())
##sorted_df_2 = sorted_df_1.sort_values(["Improved Administrative Efficiency"] + cols_ab_to_ah)
#print("Sorted 2:\n ", sorted_df_1[["Improved Administrative Efficiency"] + cols_ab_to_ah].head())
#sorted_df_3 = sorted_df_2.sort_values("AI Keywords")
print("Sorted 3:\n ", sorted_df_3.head())

print("Shape final df: ",df.shape)
print(sorted_df_3.head())

sorted_df_3.to_csv(args.output_directory + '/' + output_dataset_name + '.csv', index=False)
sorted_df_3.to_excel(args.output_directory + '/' + output_dataset_name + '.xlsx', index=False)