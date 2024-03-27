import subprocess
import os
from scripts.config import BASE_DIR, join

scripts_dir = join(BASE_DIR, 'scripts')

python_files = [file for file in os.listdir(scripts_dir) if file.endswith('.py') and file not in ['config.py', 'main.py']]

order = ['accidents.py', 'seasons.py', 'drivers.py', 'events.py', 'event_facts.py', 'safety_cars.py', 'red_flags.py', 'standings.py']

python_files_sorted = sorted(python_files, key=lambda x: order.index(x) if x in order else float('inf'))

for file in python_files_sorted:
    print(f'Executing file: {file}')
    file_path = join(scripts_dir, file)
    subprocess.run(['python', file_path])