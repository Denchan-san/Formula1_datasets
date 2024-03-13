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
    dob DATE,
    nationality VARCHAR(30),
    url TEXT,
    name VARCHAR(100),
    seasons TEXT,
    championships INT,
    race_entries INT,
    race_starts INT,
    pole_positions INT,
    race_wins INT,
    podiums INT,
    fastest_laps INT,
    points FLOAT,
    active BOOLEAN,
    championships_years TEXT,
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
STATUS
---------------------------------------------------*/

CREATE TABLE status (
    status_id SERIAL PRIMARY KEY,
    status VARCHAR(30)
);

/*---------------------------------------------------
RACES
---------------------------------------------------*/

CREATE TABLE races (
    race_id SERIAL PRIMARY KEY,
    year INT,
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
    sprint_time VARCHAR(8)
);

/*---------------------------------------------------
LAP TIMES
---------------------------------------------------*/

CREATE TABLE lap_times (
    race_id INT REFERENCES races(race_id),
    driver_id INT REFERENCES drivers(driver_id),
    lap INT,
    position INT,
    time VARCHAR(30),
    milliseconds INT
);

/*---------------------------------------------------
DRIVER STANDINGS
---------------------------------------------------*/

CREATE TABLE driver_standings (
    driver_standings_id SERIAL PRIMARY KEY,
    race_id INT REFERENCES races(race_id),
    driver_id INT REFERENCES drivers(driver_id),
    points FLOAT,
    position INT,
    position_text VARCHAR(10),
    wins INT
);

/*---------------------------------------------------
CONSTRUCTOR STANDINGS
---------------------------------------------------*/

CREATE TABLE constructor_standings (
    constructor_standings_id SERIAL PRIMARY KEY,
    race_id INT REFERENCES races(race_id),
    constructor_id INT REFERENCES constructors(constructor_id),
    points FLOAT,
    position INT,
    position_text VARCHAR(2),
    wins INT
);

/*---------------------------------------------------
CONSTRUCTOR RESULTS
---------------------------------------------------*/

CREATE TABLE constructor_results (
    constructor_results_id SERIAL PRIMARY KEY,
    race_id INT REFERENCES races(race_id),
    constructor_id INT REFERENCES constructors(constructor_id),
    points FLOAT,
    status VARCHAR(2)
);

/*---------------------------------------------------
PIT STOPS
---------------------------------------------------*/

CREATE TABLE pit_stops (
    race_id INT REFERENCES races(race_id),
    driver_id INT REFERENCES drivers(driver_id),
    stop INT,
    lap INT,
    time VARCHAR(10),
    duration VARCHAR(30),
    milliseconds INT
);

/*---------------------------------------------------
QUALIFYING
---------------------------------------------------*/

CREATE TABLE qualifying (
    qualify_id SERIAL PRIMARY KEY,
    race_id INT REFERENCES races(race_id),
    driver_id INT REFERENCES drivers(driver_id),
    constructor_id INT REFERENCES constructors(constructor_id),
    number INT,
    position INT,
    q1 VARCHAR(10),
    q2 VARCHAR(10),
    q3 VARCHAR(10)
);

/*---------------------------------------------------
RESULTS
---------------------------------------------------*/

CREATE TABLE results (
    result_id SERIAL PRIMARY KEY,
    race_id INT REFERENCES races(race_id),
    driver_id INT REFERENCES drivers(driver_id),
    constructor_id INT REFERENCES constructors(constructor_id),
    number INT,
    grid INT,
    position INT,
    position_text VARCHAR(2),
    position_order INT,
    points INT,
    laps INT,
    time VARCHAR(30),
    milliseconds INT,
    fastest_lap INT,
    rank INT,
    fastest_lap_time VARCHAR(10),
    fastest_lap_speed VARCHAR(10),
    status_id INT REFERENCES status(status_id)
);

/*---------------------------------------------------
SPRINT RESULTS
---------------------------------------------------*/

CREATE TABLE sprint_results (
    result_id SERIAL PRIMARY KEY,
    race_id INT REFERENCES races(race_id),
    driver_id INT REFERENCES drivers(driver_id),
    constructor_id INT REFERENCES constructors(constructor_id),
    number INT,
    grid INT,
    position INT,
    position_text VARCHAR(2),
    position_order INT,
    points INT,
    laps INT,
    time VARCHAR(30),
    milliseconds INT,
    fastest_lap INT,
    fastest_lap_time VARCHAR(10),
    status_id INT REFERENCES status(status_id)
);

/*---------------------------------------------------
ACCIDENTS
---------------------------------------------------*/

CREATE TABLE accidents (
    driver_id INT REFERENCES drivers(driver_id),
    age INT,
    date_of_accident DATE,
    session VARCHAR(50),
    race_id INT REFERENCES races(race_id),
    constructor_id INT REFERENCES constructors(constructor_id)
);

/*---------------------------------------------------
SAFETY CARS
---------------------------------------------------*/

CREATE TABLE safety_cars (
    race_id INT REFERENCES races(race_id),
    cause VARCHAR(50),
    deployed INT,
    retreated INT,
    full_laps INT
);

/*---------------------------------------------------
RED FLAGS
---------------------------------------------------*/

CREATE TABLE red_flags (
    race_id INT REFERENCES races(race_id),
    lap INT,
    resumed CHAR(1),
    incident TEXT,
    excluded TEXT
);


