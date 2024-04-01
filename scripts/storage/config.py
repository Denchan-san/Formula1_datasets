import os
from dotenv import load_dotenv

class Environment:
    def __init__(self, env_file='.env') -> None:
        load_dotenv(env_file)
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_PORT = os.getenv("DB_PORT")
        self.CLIENT_ENCODING = os.getenv("CLIENT_ENCODING")

env = Environment()