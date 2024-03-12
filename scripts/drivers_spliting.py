import pandas as pd

# Load the first dataset where driver's names are split
df_split_names = pd.read_csv('input_csv/drivers.csv')

# Load the second dataset where names are not split
df_not_split_names = pd.read_csv('input_csv/F1Drivers_Dataset.csv')

# Assuming the first dataset has columns 'forename', 'surname', and 'ID'
# And the second dataset has columns 'name' and 'ID'

# Create a function to concatenate the name from the second dataset
def concat_name(row):
    name_parts = row['Driver'].split()
    # Assuming the last word in the name is the surname
    surname = name_parts[-1]
    # Assuming the rest are forenames
    forename = ' '.join(name_parts[:-1])
    return pd.Series([forename, surname])

# Apply the function to create 'forename' and 'surname' columns in the second dataset
df_not_split_names[['forename', 'surname']] = df_not_split_names.apply(concat_name, axis=1)

# Merge the two datasets based on the concatenated name
merged_df = pd.merge(df_split_names, df_not_split_names, on=['forename', 'surname'], how='inner')

# Drop duplicate columns if needed
merged_df = merged_df.drop(columns=['forename', 'surname'])

# Save the merged dataset to a new CSV file
merged_df.to_csv('output_csv/drivers.csv', index=False)
