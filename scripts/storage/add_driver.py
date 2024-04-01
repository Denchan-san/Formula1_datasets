from config import env
import psycopg2
import pandas as pd

def driver_exists(cursor, driver):
    cursor.execute("SELECT COUNT(*) FROM drivers WHERE forename = %s AND surname = %s", (driver['forename'], driver['surname']))
    count = cursor.fetchone()[0]
    return count > 0

def insert_driver(cursor, driver):
    cursor.execute("INSERT INTO drivers (driver_ref, number, code, forename, surname, dob, nationality, url) \
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING driver_id",
                   (driver['driverRef'],
                    driver['number'],
                    driver['code'],
                    driver['forename'],
                    driver['surname'],
                    driver['dob'],
                    driver['nationality'],
                    driver['url']))
    inserted_id = cursor.fetchone()[0]
    
    cursor.execute("INSERT INTO drivers_career_stats (driver_id, championships, race_entries, race_starts, pole_positions, \
                    race_wins, podiums, fastest_laps, points, active, decade, pole_rate, start_rate, win_rate, \
                    podium_rate, fastLap_rate, points_per_entry, years_active, champion) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (inserted_id,
                    driver['Championships'],
                    driver['Race_Entries'],
                    driver['Race_Starts'],
                    driver['Pole_Positions'],
                    driver['Race_Wins'],
                    driver['Podiums'],
                    driver['Fastest_Laps'],
                    driver['Points'],
                    driver['Active'],
                    driver['Decade'],
                    driver['Pole_Rate'],
                    driver['Start_Rate'],
                    driver['Win_Rate'],
                    driver['Podium_Rate'],
                    driver['FastLap_Rate'],
                    driver['Points_Per_Entry'],
                    driver['Years_Active'],
                    driver['Champion']))
    
    return inserted_id

def main():

    drivers_df = pd.read_csv('input_csv/new_drivers.csv')

    connection = psycopg2.connect(
        database=env.DB_NAME,
        user=env.DB_USER,
        password=env.DB_PASSWORD,
        host=env.DB_HOST,
        port=env.DB_PORT,
        client_encoding=env.CLIENT_ENCODING
    )

    cursor = connection.cursor()

    try:
        for _, driver in drivers_df.iterrows():
            if not driver_exists(cursor, driver):
                driver_id = insert_driver(cursor, driver)
                print(f"Added driver {driver['forename']} {driver['surname']} to the database with ID {driver_id}")
        connection.commit()
        print('Transaction committed succesfully.')
    except Exception as e:
        connection.rollback()
        print(f'Error occured: {e}')
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()

