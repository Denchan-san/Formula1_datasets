import pandas as pd
import numpy as np
import os
from config import INPUT_CSV_DIR, OUTPUT_CSV_DIR

driver_standings_path = os.path.join(INPUT_CSV_DIR, 'driver_standings.csv')
constructor_standings_path = os.path.join(INPUT_CSV_DIR, 'constructor_standings.csv')
driver_standings_df = pd.read_csv(driver_standings_path)
constructor_standings_df = pd.read_csv(constructor_standings_path)

driver_standings_df['constructorId'] = np.nan
constructor_standings_df['driverId'] = np.nan

standings_df = pd.concat([driver_standings_df, constructor_standings_df], ignore_index=True)

standings_df.reset_index(drop=True, inplace=True)

standings_df['standingsId'] = standings_df.index + 1

standings_df.rename(columns={'raceId': 'eventId'}, inplace=True)

standings_df['driverId'] = standings_df['driverId'].astype('Int64')
standings_df['constructorId'] = standings_df['constructorId'].astype('Int64')

standings_df.drop(columns=['positionText'], inplace=True)

standings_df = standings_df[['standingsId', 'eventId', 'driverId', 'constructorId', 'points', 'position', 'wins']]

standings_df.to_csv(os.path.join(OUTPUT_CSV_DIR, 'standings.csv'), index=False)