from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

rol_instalacion = Table(
    "rol_instalacion",
    Base.metadata,
    Column("rol_id", Integer, ForeignKey("rol.id"), primary_key=True),
    Column("instalacion_id", Integer, ForeignKey("instalacion.id"), primary_key=True)
)
