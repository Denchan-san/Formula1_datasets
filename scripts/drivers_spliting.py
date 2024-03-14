import pandas as pd
import csv

df_split_names = pd.read_csv('input_csv/drivers.csv')

df_not_split_names = pd.read_csv('input_csv/F1Drivers_Dataset.csv')

def concat_name(row):
    name = row['forename'] + ' ' + row['surname']
    return pd.Series([name])

df_split_names[['Driver']] = df_split_names.apply(concat_name, axis=1)

merged_df = pd.merge(df_split_names, df_not_split_names, on=['Driver'], how='inner')

merged_df = merged_df.drop(columns=['forename', 'surname', 'Nationality'])

merged_df.to_csv('output_csv/drivers.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
