/*---------------------------------------------------
CIRCUITS
---------------------------------------------------*/

CREATE TABLE circuits (
    circuit_id SERIAL PRIMARY KEY,
    circuit_ref VARCHAR(30),
    name VARCHAR(100),
    location VARCHAR(100),
    country VARCHAR(30),
    lat FLOAT,
    lng FLOAT,
    alt INT,
    url TEXT
);

/*---------------------------------------------------
CONSTRUCTORS
---------------------------------------------------*/

CREATE TABLE constructors (
    constructor_id SERIAL PRIMARY KEY,
    constructor_ref VARCHAR(30),
    name VARCHAR(100),
    nationality VARCHAR(30),
    url TEXT
);

/*---------------------------------------------------
DRIVERS
---------------------------------------------------*/

CREATE TABLE drivers (
    driver_id SERIAL PRIMARY KEY,
    driver_ref VARCHAR(30),
    number INT,
    code VARCHAR(3),
    forename VARCHAR(30),
    surname VARCHAR(30),
    dob DATE,
    nationality VARCHAR(30),
    url TEXT
);

/*---------------------------------------------------
DRIVERS CAREER STATS
---------------------------------------------------*/

CREATE TABLE drivers_career_stats (
    driver_id INT PRIMARY KEY REFERENCES drivers(driver_id),
    championships INT,
    race_entries INT,
    race_starts INT,
    pole_positions INT,
    race_wins INT,
    podiums INT,
    fastest_laps INT,
    points FLOAT,
    active BOOLEAN,
    decade INT,
    pole_rate FLOAT,
    start_rate FLOAT,
    win_rate FLOAT,
    podium_rate FLOAT,
    fastlap_rate FLOAT,
    points_per_entry FLOAT,
    years_active INT,
    champion BOOLEAN
);

/*---------------------------------------------------
SEASONS
---------------------------------------------------*/

CREATE TABLE seasons (
    season_id SERIAL PRIMARY KEY,
    year INT,
    url TEXT
);

/*---------------------------------------------------
DRIVER SEASONS
---------------------------------------------------*/

CREATE TABLE driver_seasons (
    driver_id INT REFERENCES drivers(driver_id),
    season_id INT REFERENCES seasons(season_id),
    is_championship BOOLEAN
);

/*---------------------------------------------------
STATUS
---------------------------------------------------*/

CREATE TABLE status (
    status_id SERIAL PRIMARY KEY,
    status VARCHAR(30)
);

/*---------------------------------------------------
EVENTS
---------------------------------------------------*/

CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    round INT,
    circuit_id INT REFERENCES circuits(circuit_id),
    name VARCHAR(100),
    date DATE,
    time VARCHAR(10),
    url TEXT,
    fp1_date date,
    fp1_time VARCHAR(8),
    fp2_date date,
    fp2_time VARCHAR(8),
    fp3_date date,
    fp3_time VARCHAR(8),
    quali_date date,
    quali_time VARCHAR(8),
    sprint_date date,
    sprint_time VARCHAR(8),
    season_id INT REFERENCES seasons(season_id)
);

/*---------------------------------------------------
CONSTRUCTOR RESULTS
---------------------------------------------------*/

CREATE TABLE constructor_results (
    constructor_results_id SERIAL PRIMARY KEY,
    event_id INT REFERENCES events(event_id),
    constructor_id INT REFERENCES constructors(constructor_id),
    points FLOAT,
    status VARCHAR(2)
);

/*---------------------------------------------------
LAP TIMES
---------------------------------------------------*/

CREATE TABLE lap_times (
    event_id INT REFERENCES events(event_id),
    driver_id INT REFERENCES drivers(driver_id),
    lap INT,
    position INT,
    time VARCHAR(30),
    milliseconds INT
);

/*---------------------------------------------------
STANDINGS
---------------------------------------------------*/

CREATE TABLE standings (
    standings_id SERIAL PRIMARY KEY,
    event_id INT REFERENCES events(event_id),
    driver_id INT REFERENCES drivers(driver_id),
    constructor_id INT REFERENCES constructors(constructor_id),
    points FLOAT,
    position INT,
    wins INT
);

/*---------------------------------------------------
PIT STOPS
---------------------------------------------------*/

CREATE TABLE pit_stops (
    event_id INT REFERENCES events(event_id),
    driver_id INT REFERENCES drivers(driver_id),
    stop INT,
    lap INT,
    time VARCHAR(10),
    duration VARCHAR(30),
    milliseconds INT
);

/*---------------------------------------------------
EVENT FACTS
---------------------------------------------------*/

CREATE TABLE event_facts (
    event_fact_id SERIAL PRIMARY KEY,
    event_id INT REFERENCES events(event_id),
    driver_id INT REFERENCES drivers(driver_id),
    constructor_id INT REFERENCES constructors(constructor_id),
    number INT,
    race_grid INT,
    race_position INT,
    race_position_order INT,
    race_points FLOAT,
    race_laps INT,
    race_time VARCHAR(30),
    race_milliseconds INT,
    race_fastest_lap INT,
    race_rank INT,
    race_fastest_lap_time VARCHAR(10),
    race_fastest_lap_speed VARCHAR(10),
    race_status_id INT REFERENCES status(status_id),
    sprint_grid INT,
    sprint_position INT,
    sprint_position_order INT,
    sprint_points INT,
    sprint_laps INT,
    sprint_time VARCHAR(30),
    sprint_milliseconds INT,
    sprint_fastest_lap INT,
    sprint_fastest_lap_time VARCHAR(10),
    sprint_status_id INT REFERENCES status(status_id),
    qualifying_position INT,
    q1 VARCHAR(10),
    q2 VARCHAR(10),
    q3 VARCHAR(10)
);

/*---------------------------------------------------
ACCIDENTS
---------------------------------------------------*/

CREATE TABLE accidents (
    event_fact_id INT REFERENCES event_facts(event_fact_id),
    age INT,
    date_of_accident DATE,
    session VARCHAR(50)
);

/*---------------------------------------------------
SAFETY CARS
---------------------------------------------------*/

CREATE TABLE safety_cars (
    event_id INT REFERENCES events(event_id),
    cause VARCHAR(50),
    deployed INT,
    retreated INT,
    full_laps INT
);

/*---------------------------------------------------
RED FLAGS
---------------------------------------------------*/

CREATE TABLE red_flags (
    event_id INT REFERENCES events(event_id),
    lap INT,
    resumed CHAR(1),
    incident TEXT,
    excluded TEXT
);