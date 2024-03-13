import pandas as pd

# Assuming the 'driverId' column contains the IDs in the merged_df
merged_df = pd.read_csv('output_csv/drivers.csv')

# Create a DataFrame with all IDs from 1 to 858
all_ids = pd.DataFrame({'driverId': range(1, 859)})

# Merge the two DataFrames to identify missing IDs
missing_ids = pd.merge(all_ids, merged_df[['driverId']], how='left', indicator=True).loc[lambda x: x['_merge'] == 'left_only']

# Print the missing IDs
print("Missing IDs:")
print(missing_ids['driverId'].tolist())