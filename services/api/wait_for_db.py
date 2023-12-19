import psycopg2
import time
import os

def wait_for_db():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="postgres",
                host="db",
                port=5432
            )
            conn.close()
            print("Database is ready!")
            return
        except psycopg2.OperationalError:
            retries -= 1
            print("Waiting for database... Retries left:", retries)
            time.sleep(5)

    raise Exception("Failed to connect to the database")

if __name__ == "__main__":
    wait_for_db()