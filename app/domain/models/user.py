from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.adapters.database.mysql import Base

# Define tu modelo User
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    tip_documento = Column(String(10))
    num_documento = Column(String(20))
    nombre = Column(String(255))
    apellido = Column(String(255))
    correo = Column(String(255), unique=True, index=True)
    clave = Column(String(255))

    # Relación con el modelo Post
    rol_id = Column(Integer, ForeignKey("roles.id"))

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"