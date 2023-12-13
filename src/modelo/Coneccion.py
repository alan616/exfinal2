import psycopg2
from decouple import config

def conexion2023():
    try:
        connection = psycopg2.connect(
            dbname=config('BD_DB'),
            user=config('BD_USER'),
            password=config('BD_PASSWORD'),
            host=config('BD_HOST'),
            port=config('BD_PORT')
        )
        return connection
    except psycopg2.Error as e:
        print("Error al conectar a PostgreSQL:", e)
        return None
