import pandas as pd
from config import INPUT_CSV_DIR, OUTPUT_CSV_DIR, join

red_flags_path = join(INPUT_CSV_DIR, 'red_flags.csv')
races_path = join(INPUT_CSV_DIR, 'races.csv')
red_flags_df = pd.read_csv(red_flags_path)
races_df = pd.read_csv(races_path)

def concat_race(row):
    race = str(row['year']) + ' ' + row['name']
    return pd.Series([race])

races_df['Race'] = races_df.apply(concat_race, axis=1)

merged_df = pd.merge(races_df[['raceId', 'Race']], red_flags_df, on=['Race'], how='inner')

merged_df.drop(['Race'], axis=1, inplace=True)

merged_df = merged_df.rename(columns={'raceId': 'eventId'})

merged_df.to_csv(join(OUTPUT_CSV_DIR, 'red_flags.csv'), index=False)