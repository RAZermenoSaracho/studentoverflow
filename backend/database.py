import json
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Cargar configuración
with open("config/config.json") as config_file:
    config = json.load(config_file)

DB_USER = config['DB_USER']
DB_PASSWORD = config['DB_PASSWORD']
DB_HOST = config['DB_HOST']
DB_PORT = config['DB_PORT']
DB_NAME = config['DB_NAME']
SECRET_KEY = config['SECRET_KEY']

# Intentar conectarse a PostgreSQL y crear la base de datos si no existe
try:
    conn = psycopg2.connect(
        dbname='postgres',
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
    cursor.close()
    conn.close()
except Exception as e:
    print("Error al verificar o crear la base de datos:", e)

project_root = os.path.abspath(os.path.dirname(__file__))
template_path = os.path.join(project_root, "..", "templates")
static_path = os.path.join(project_root, "..", "static")

app = Flask(__name__, template_folder=template_path, static_folder=static_path)

# Configurar la clave secreta para sesiones
app.secret_key = SECRET_KEY

# Configurar SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
db = SQLAlchemy(app)

# Inicializar Flask-Login
from backend.login_manager import login_manager
login_manager.init_app(app)
