import pandas as pd
import ast
from config import INPUT_CSV_DIR, OUTPUT_CSV_DIR, join

drivers_path = join(INPUT_CSV_DIR, 'F1Drivers_Dataset.csv')
seasons_path = join(INPUT_CSV_DIR, 'seasons.csv')
drivers = pd.read_csv(drivers_path)
seasons = pd.read_csv(seasons_path)

driver_seasons = pd.DataFrame(columns=['driverId', 'seasonId', 'isChampionship'])
for index, row in drivers.iterrows():
    driver_id = row['driverId']
    seasons_list = ast.literal_eval(row['Seasons'])  # convert string to list
    championship_years = ast.literal_eval(row['Championship Years'])  # convert string to list
    for season_year in seasons_list:
        season_id = seasons.loc[seasons['year'] == season_year, 'id'].values[0]
        is_championship = season_year in championship_years
        driver_seasons = driver_seasons.append({'driverId': driver_id, 'seasonId': season_id, 'isChampionship': is_championship}, ignore_index=True)

driver_seasons.to_csv(join(OUTPUT_CSV_DIR, 'driver_seasons.csv'), index=False)