from sqlalchemy.orm import Session
from app.domain.models.role import Role
from app.domain.schemas.rol import RolCreate

def create_role_service(db: Session, rol: RolCreate):
    nuevo_rol = Role(nombre=rol.nombre)
    db.add(nuevo_rol)
    db.commit()
    db.refresh(nuevo_rol)
    return nuevo_rol