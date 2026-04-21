import psycopg2
import os
import time
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    retries = 5
    while retries > 0:
        try:
            connection = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD")
            )
            return connection
        except Exception as e:
            print(f"DB not ready, retrying... ({e})")
            retries -= 1
            time.sleep(3)
    raise Exception("Could not connect to database after retries")