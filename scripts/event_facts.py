import pandas as pd
import numpy as np
from config import INPUT_CSV_DIR, OUTPUT_CSV_DIR, join

results_path = join(INPUT_CSV_DIR, 'results.csv')
sprint_results_path = join(INPUT_CSV_DIR, 'sprint_results.csv')
qualifying_path = join(INPUT_CSV_DIR, 'qualifying.csv')
results_df = pd.read_csv(results_path)
sprint_results_df = pd.read_csv(sprint_results_path)
qualifying_df = pd.read_csv(qualifying_path)

results_df.replace({'\\N': np.nan}, inplace=True)
sprint_results_df.replace({'\\N': np.nan}, inplace=True)
qualifying_df.replace({'\\N': np.nan}, inplace=True)
results_df['number'] = results_df['number'].astype('Int64')

merged_df = pd.merge(results_df, sprint_results_df, on=['raceId', 'driverId', 'constructorId', 'number'], how='outer', suffixes=('_race', '_sprint'))

event_facts_df = pd.merge(merged_df, qualifying_df, on=['raceId', 'driverId', 'constructorId', 'number'], how='left')

event_facts_df = event_facts_df.rename(columns={
    'resultId_race': 'resultId',
    'raceId': 'eventId',
    'grid_race': 'race_grid',
    'position_race': 'race_position',
    'positionText_race': 'race_positionText',
    'positionOrder_race': 'race_positionOrder',
    'points_race': 'race_points',
    'laps_race': 'race_laps',
    'time_race': 'race_time',
    'milliseconds_race': 'race_milliseconds',
    'fastestLap_race': 'race_fastestLap',
    'rank': 'race_rank',
    'fastestLapTime_race': 'race_fastestLapTime',
    'fastestLapSpeed': 'race_fastestLapSpeed',
    'statusId_race': 'race_statusId',
    'resultId_sprint': 'sprintResultId',
    'grid_sprint': 'sprint_grid',
    'position_sprint': 'sprint_position',
    'positionText_sprint': 'sprint_positionText',
    'positionOrder_sprint': 'sprint_positionOrder',
    'points_sprint': 'sprint_points',
    'laps_sprint': 'sprint_laps',
    'time_sprint': 'sprint_time',
    'milliseconds_sprint': 'sprint_milliseconds',
    'fastestLap_sprint': 'sprint_fastestLap',
    'fastestLapTime_sprint': 'sprint_fastestLapTime',
    'statusId_sprint': 'sprint_statusId',
    'position': 'qualifying_position'
})

event_facts_df = event_facts_df[[
    'resultId', 'eventId', 'driverId', 'constructorId', 'number',
    'race_grid', 'race_position', 'race_positionText', 'race_positionOrder', 'race_points',
    'race_laps', 'race_time', 'race_milliseconds', 'race_fastestLap', 'race_rank',
    'race_fastestLapTime', 'race_fastestLapSpeed', 'race_statusId',
    'sprint_grid', 'sprint_position', 'sprint_positionText', 'sprint_positionOrder', 'sprint_points',
    'sprint_laps', 'sprint_time', 'sprint_milliseconds', 'sprint_fastestLap', 'sprint_fastestLapTime', 'sprint_statusId',
    'qualifying_position', 'q1', 'q2', 'q3'
]]

event_facts_df = event_facts_df.drop(['race_positionText', 'sprint_positionText'], axis=1)
event_facts_df['qualifying_position'] = event_facts_df['qualifying_position'].astype('Int64')
event_facts_df['sprint_grid'] = event_facts_df['sprint_grid'].astype('Int64')
event_facts_df['sprint_positionOrder'] = event_facts_df['sprint_positionOrder'].astype('Int64')
event_facts_df['sprint_laps'] = event_facts_df['sprint_laps'].astype('Int64')
event_facts_df['sprint_statusId'] = event_facts_df['sprint_statusId'].astype('Int64')

event_facts_df.to_csv(join(OUTPUT_CSV_DIR, 'event_facts.csv'), index=False)