import pandas as pd
import numpy as np
from config import INPUT_CSV_DIR, OUTPUT_CSV_DIR, join

safety_cars_path = join(INPUT_CSV_DIR, 'safety_cars.csv')
races_path = join(INPUT_CSV_DIR, 'races.csv')
safety_cars_df = pd.read_csv(safety_cars_path)
races_df = pd.read_csv(races_path)

def concat_race(row):
    race = str(row['year']) + ' ' + row['name']
    return pd.Series([race])

races_df['Race'] = races_df.apply(concat_race, axis=1)

merged_df = pd.merge(races_df[['raceId', 'Race']], safety_cars_df, on=['Race'], how='inner')

merged_df.drop(['Race'], axis=1, inplace=True)

merged_df['Retreated'].replace('', np.nan, inplace=True)
merged_df['Retreated'] = merged_df['Retreated'].astype(float).astype('Int64')

merged_df = merged_df.rename(columns={'raceId': 'eventId'})

merged_df.to_csv(join(OUTPUT_CSV_DIR, 'safety_cars.csv'), index=False)