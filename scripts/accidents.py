import pandas as pd
import numpy as np
from datetime import datetime, timedelta

accidents_df = pd.read_csv('input_csv/fatal_accidents_drivers.csv')
drivers_df = pd.read_csv('input_csv/drivers.csv')
races_df = pd.read_csv('output_csv/races.csv')
constructors_df = pd.read_csv('output_csv/constructors.csv')

def concat_name(row):
    name_parts = row['Driver'].split()
    # Assuming the last word in the name is the surname
    surname = name_parts[-1]
    # Assuming the rest are forenames
    forename = ' '.join(name_parts[:-1])
    return pd.Series([forename, surname])

def concat_race(row):
    race = str(row['year']) + ' ' + row['name']
    return pd.Series([race])

# Apply the function to create 'forename' and 'surname' columns in the second dataset
accidents_df[['forename', 'surname']] = accidents_df.apply(concat_name, axis=1)
races_df['Event'] = races_df.apply(concat_race, axis=1)
constructors_df.rename(columns={'name': 'Car'}, inplace=True)

merged_df = pd.merge(drivers_df[['driverId', 'forename', 'surname']], accidents_df, on=['forename', 'surname'], how='inner')
merged_df = pd.merge(merged_df, races_df[['raceId', 'Event']], on=['Event'], how='inner')
merged_df = pd.merge(merged_df, constructors_df[['constructorId', 'Car']], on=['Car'], how='inner')

merged_df.drop(['forename', 'surname', 'Driver', 'Car', 'Event'], axis=1, inplace=True)

merged_df['Date Of Accident'] = pd.to_datetime(merged_df['Date Of Accident'], format='mixed')
future_dates = merged_df['Date Of Accident'] > datetime.now()
merged_df.loc[future_dates, 'Date Of Accident'] -= timedelta(days=36525)

merged_df['Age'].replace('', np.nan, inplace=True)
merged_df['Age'] = merged_df['Age'].astype(float).astype('Int64')

merged_df.to_csv('output_csv/accidents.csv', index=False)