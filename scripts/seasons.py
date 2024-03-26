import pandas as pd
import os
from config import INPUT_CSV_DIR, OUTPUT_CSV_DIR

seasons_path = os.path.join(INPUT_CSV_DIR, 'seasons.csv')
seasons = pd.read_csv(seasons_path)

seasons = seasons.reset_index().rename(columns={'index': 'seasonId'})
seasons['seasonId'] = seasons['seasonId'] + 1

seasons.to_csv(os.path.join(OUTPUT_CSV_DIR, 'seasons.csv'), index=False)