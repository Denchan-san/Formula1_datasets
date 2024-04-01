from config import env
import psycopg2

connection = psycopg2.connect(
    database=env.DB_NAME,
    user=env.DB_USER,
    password=env.DB_PASSWORD,
    host=env.DB_HOST,
    port=env.DB_PORT,
    client_encoding=env.CLIENT_ENCODING
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM drivers;")

record = cursor.fetchall()

print(record)