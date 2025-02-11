# app/models/__init__.py
from .user import User
from .rols import Rol

# Exportamos `Base` para Alembic
from app.adapters.database.mysql import Base
