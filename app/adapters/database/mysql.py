from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuración de conexión
DATABASE_URL  = "mysql+pymysql://root:@localhost:3306/Argus"

# Crear motor de base de datos
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
