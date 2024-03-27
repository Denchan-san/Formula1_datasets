import os

def join(*args):
    return os.path.join(*args)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_CSV_DIR = os.path.join(BASE_DIR, 'input_csv')
OUTPUT_CSV_DIR = os.path.join(BASE_DIR, 'output_csv')