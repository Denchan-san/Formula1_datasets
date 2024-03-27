import pandas as pd
import os
from config import INPUT_CSV_DIR, OUTPUT_CSV_DIR

races_path = os.path.join(INPUT_CSV_DIR, 'races.csv')
seasons_path = os.path.join(OUTPUT_CSV_DIR, 'seasons.csv')
races = pd.read_csv(races_path)
seasons = pd.read_csv(seasons_path)

year_season_map = dict(zip(seasons['year'], seasons['seasonId']))

races['seasonId'] = races['year'].map(year_season_map)

events = races.drop('year', axis=1)

events = events.rename(columns={'raceId': 'eventId'})

events.to_csv(os.path.join(OUTPUT_CSV_DIR, 'events.csv'), index=False)