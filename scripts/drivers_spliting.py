import pandas as pd
import csv

# Load the first dataset where driver's names are split
df_split_names = pd.read_csv('input_csv/drivers.csv')

# Load the second dataset where names are not split
df_not_split_names = pd.read_csv('input_csv/F1Drivers_Dataset.csv')

# Assuming the first dataset has columns 'forename', 'surname', and 'ID'
# And the second dataset has columns 'name' and 'ID'

# Create a function to concatenate the name from the second dataset
def concat_name(row):
    name = row['forename'] + ' ' + row['surname']
    return pd.Series([name])

# Apply the function to create 'forename' and 'surname' columns in the second dataset
df_split_names[['Driver']] = df_split_names.apply(concat_name, axis=1)

# Merge the two datasets based on the concatenated name
merged_df = pd.merge(df_split_names, df_not_split_names, on=['Driver'], how='inner')

# Drop duplicate columns if needed
merged_df = merged_df.drop(columns=['forename', 'surname', 'Nationality'])

# Save the merged dataset to a new CSV file
merged_df.to_csv('output_csv/drivers.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
