import pandas as pd

accidents_df = pd.read_csv('input_csv/fatal_accidents_drivers.csv')
drivers_df = pd.read_csv('input_csv/drivers.csv')

def concat_name(row):
    name_parts = row['Driver'].split()
    # Assuming the last word in the name is the surname
    surname = name_parts[-1]
    # Assuming the rest are forenames
    forename = ' '.join(name_parts[:-1])
    return pd.Series([forename, surname])

# Apply the function to create 'forename' and 'surname' columns in the second dataset
accidents_df[['forename', 'surname']] = accidents_df.apply(concat_name, axis=1)

merged_df = pd.merge(drivers_df[['driverId', 'forename', 'surname']], accidents_df, on=['forename', 'surname'], how='inner')

merged_df.drop(['forename', 'surname', 'Driver'], axis=1, inplace=True)

merged_df.to_csv('output_csv/accidents.csv', index=False)