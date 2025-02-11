# app/adapters/database/mysql.py
from sqlalchemy.ext.declarative import declarative_base
from databases import Database
from sqlalchemy import create_engine, MetaData

# Configuración de conexión
DATABASE_URL = "mysql+pymysql://root:admin123@localhost:3307/nombre_base_datos"

# Crear conexión asíncrona
database = Database(DATABASE_URL)

# Crear motor de base de datos
engine = create_engine(DATABASE_URL)

# Metadata para los modelos
metadata = MetaData()

# Declaración de base para los modelos
Base = declarative_base()
