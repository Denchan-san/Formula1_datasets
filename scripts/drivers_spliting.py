import csv
import os

# Define the input and output file paths
input_file = 'drivers.csv'
output_file = 'drivers2.csv'

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

# Read the CSV file and write the modified data to a new CSV file
with open(input_file, 'r') as csv_in, open(output_file, 'w', newline='') as csv_out:
    reader = csv.DictReader(csv_in)
    fieldnames = [field for field in reader.fieldnames if field != 'Driver'] + ['Name', 'Surname']
    writer = csv.DictWriter(csv_out, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        # Split the Driver column into Name and Surname
        name, surname = split_name(row['Driver'])
        # Update the row with Name and Surname
        row['Name'] = name
        row['Surname'] = surname
        # Write the updated row to the output CSV file without the 'Driver' column
        del row['Driver']
        writer.writerow(row)

print("Splitting of Driver names into Name and Surname is done!")
