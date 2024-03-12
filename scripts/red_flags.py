import pandas as pd

red_flags_df = pd.read_csv('input_csv/red_flags.csv')
races_df = pd.read_csv('output_csv/races.csv')

def concat_race(row):
    race = str(row['year']) + ' ' + row['name']
    return pd.Series([race])

races_df['Race'] = races_df.apply(concat_race, axis=1)

merged_df = pd.merge(races_df[['raceId', 'Race']], red_flags_df, on=['Race'], how='inner')

merged_df.drop(['Race'], axis=1, inplace=True)

merged_df.to_csv('output_csv/red_flags.csv', index=False)