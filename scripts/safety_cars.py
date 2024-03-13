import pandas as pd
import numpy as np

safety_cars_df = pd.read_csv('input_csv/safety_cars.csv')
races_df = pd.read_csv('output_csv/races.csv')

def concat_race(row):
    race = str(row['year']) + ' ' + row['name']
    return pd.Series([race])

races_df['Race'] = races_df.apply(concat_race, axis=1)

merged_df = pd.merge(races_df[['raceId', 'Race']], safety_cars_df, on=['Race'], how='inner')

merged_df.drop(['Race'], axis=1, inplace=True)

merged_df['Retreated'].replace('', np.nan, inplace=True)
print(merged_df)
merged_df['Retreated'] = merged_df['Retreated'].astype(float).astype('Int64')

merged_df.to_csv('output_csv/safety_cars.csv', index=False)