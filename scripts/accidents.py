import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from config import INPUT_CSV_DIR, OUTPUT_CSV_DIR, join

accidents_df = pd.read_csv(join(INPUT_CSV_DIR, 'fatal_accidents_drivers.csv'))
drivers_df = pd.read_csv(join(INPUT_CSV_DIR, 'drivers.csv'))
races_df = pd.read_csv(join(INPUT_CSV_DIR, 'races.csv'))
event_facts_df = pd.read_csv(join(OUTPUT_CSV_DIR, 'event_facts.csv'))

def concat_name(row):
    name_parts = row['Driver'].split()
    surname = name_parts[-1]
    forename = ' '.join(name_parts[:-1])
    return pd.Series([forename, surname])

def concat_race(row):
    race = str(row['year']) + ' ' + row['name']
    return pd.Series([race])

accidents_df[['forename', 'surname']] = accidents_df.apply(concat_name, axis=1)
races_df['Event'] = races_df.apply(concat_race, axis=1)

merged_df = pd.merge(drivers_df[['driverId', 'forename', 'surname']], accidents_df, on=['forename', 'surname'], how='inner')
merged_df = pd.merge(merged_df, races_df[['raceId', 'Event']], on=['Event'], how='inner')
merged_df = pd.merge(merged_df, event_facts_df[['resultId', 'eventId', 'driverId', 'constructorId']], left_on=['raceId', 'driverId'], right_on=['eventId', 'driverId'], how='inner')

merged_df.drop(['forename', 'surname', 'Driver', 'Event'], axis=1, inplace=True)
merged_df.rename(columns={'resultId': 'eventFactId'}, inplace=True)

merged_df['Date Of Accident'] = pd.to_datetime(merged_df['Date Of Accident'], format='%m/%d/%y')

future_dates = merged_df['Date Of Accident'] > datetime.now()
merged_df.loc[future_dates, 'Date Of Accident'] -= timedelta(days=36525)

merged_df['Age'].replace('', np.nan, inplace=True)
merged_df['Age'] = merged_df['Age'].astype(float).astype('Int64')

merged_df = merged_df[['eventFactId', 'Age', 'Date Of Accident', 'Session']]

merged_df.to_csv(join(OUTPUT_CSV_DIR, 'accidents.csv'), index=False)