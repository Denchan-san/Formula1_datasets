import pandas as pd
import ast
import os
from config import INPUT_CSV_DIR, OUTPUT_CSV_DIR

drivers_path = os.path.join(INPUT_CSV_DIR, 'drivers.csv')
f1_drivers_path = os.path.join(INPUT_CSV_DIR, 'F1Drivers_Dataset.csv')
seasons_path = os.path.join(OUTPUT_CSV_DIR, 'seasons.csv')

drivers = pd.read_csv(drivers_path)
f1_drivers = pd.read_csv(f1_drivers_path)

drivers['full_name'] = drivers['forename'] + ' ' + drivers['surname']

merged_df = pd.merge(drivers, f1_drivers, left_on='full_name', right_on='Driver', how='left')

merged_df = merged_df.drop('full_name', axis=1)

output_drivers_cols = ['driverId', 'driverRef', 'number', 'code', 'forename', 'surname', 'dob', 'nationality', 'url']
output_drivers = merged_df[output_drivers_cols]
output_drivers.to_csv(os.path.join(OUTPUT_CSV_DIR, 'drivers.csv'), index=False)

career_stats_cols = ['driverId', 'Championships', 'Race_Entries', 'Race_Starts', 'Pole_Positions', 'Race_Wins', 'Podiums', 'Fastest_Laps', 'Points', 'Active', 'Decade', 'Pole_Rate', 'Start_Rate', 'Win_Rate', 'Podium_Rate', 'FastLap_Rate', 'Points_Per_Entry', 'Years_Active', 'Champion']
career_stats = merged_df[career_stats_cols]
career_stats.to_csv(os.path.join(OUTPUT_CSV_DIR, 'driver_career_stats.csv'), index=False)

seasons = pd.read_csv(seasons_path)

driver_seasons = pd.DataFrame(columns=['driverId', 'seasonId', 'isChampionship'])
for index, row in merged_df.iterrows():
    driver_id = row['driverId']
    seasons_list = ast.literal_eval(row['Seasons'])  # convert string to list
    championship_years = ast.literal_eval(row['Championship Years']) if isinstance(row['Championship Years'], str) else []  # convert string to list
    for season_year in seasons_list:
        season_id = seasons.loc[seasons['year'] == season_year, 'seasonId'].values[0]
        is_championship = season_year in championship_years
        driver_seasons = driver_seasons._append({'driverId': driver_id, 'seasonId': season_id, 'isChampionship': is_championship}, ignore_index=True)

driver_seasons.to_csv(os.path.join(OUTPUT_CSV_DIR, 'driver_seasons.csv'), index=False)