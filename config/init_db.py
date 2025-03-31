import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def ensure_database_exists(config):
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user=config['DB_USER'],
            password=config['DB_PASSWORD'],
            host=config['DB_HOST'],
            port=config['DB_PORT']
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{config['DB_NAME']}'")
        if not cursor.fetchone():
            cursor.execute(f"CREATE DATABASE {config['DB_NAME']}")
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error al verificar o crear la base de datos:", e)
