import csv

# Define the input file path
input_file = 'drivers.csv'

# Define output file paths for the two tables
drivers_output_file = 'drivers_table.csv'
career_stats_output_file = 'driver_career_stats_table.csv'

# Function to split the Driver column into Name and Surname
def split_name(driver):
    parts = driver.split(' ')
    if len(parts) > 1:
        surname = parts[-1]
        name = ' '.join(parts[:-1])
    else:
        name = parts[0]
        surname = ''
    return name, surname

# Read the CSV file and split data into two tables
with open(input_file, 'r') as csv_in, \
     open(drivers_output_file, 'w', newline='') as drivers_out, \
     open(career_stats_output_file, 'w', newline='') as career_stats_out:
    
    # Create CSV writers for both output files
    drivers_writer = csv.writer(drivers_out)
    career_stats_writer = csv.writer(career_stats_out)
    
    # Write headers for both tables
    drivers_writer.writerow(['driverId', 'driverRef', 'number', 'code', 'name', 'surname', 'dob', 'nationality'])
    career_stats_writer.writerow(['driverId', 'Championships', 'Race_Entries', 'Race_Starts', 'Pole_Positions', 
                                  'Race_Wins', 'Podiums', 'Fastest_Laps', 'Points', 'Active', 'Decade', 'Pole_Rate', 
                                  'Start_Rate', 'Win_Rate', 'Podium_Rate', 'FastLap_Rate', 'Points_Per_Entry', 
                                  'Years_Active', 'Champion'])
    
    reader = csv.DictReader(csv_in)
    
    for row in reader:
        # Split the Driver column into Name and Surname
        name, surname = split_name(row['Driver'])
        
        # Write data to drivers table
        drivers_writer.writerow([row['driverId'], row['driverRef'], row['number'], row['code'], name, surname, 
                                 row['dob'], row['nationality']])
        
        # Write data to driver_career_stats table
        career_stats_writer.writerow([row['driverId'], row['Championships'], row['Race_Entries'], row['Race_Starts'], 
                                       row['Pole_Positions'], row['Race_Wins'], row['Podiums'], row['Fastest_Laps'], 
                                       row['Points'], row['Active'], row['Decade'], row['Pole_Rate'], row['Start_Rate'], 
                                       row['Win_Rate'], row['Podium_Rate'], row['FastLap_Rate'], row['Points_Per_Entry'], 
                                       row['Years_Active'], row['Champion']])
        
print("Splitting of drivers.csv into two tables is done!")
