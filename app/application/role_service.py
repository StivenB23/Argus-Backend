from sqlalchemy.orm import Session

from app.domain.models.associations import rol_instalacion
from app.domain.models.instalacion import Facility
from app.domain.models.role import Role
from app.domain.schemas.rol import RolCreate

def get_roles_service(db: Session):
    return db.query(Role).all()

def create_role_service(db: Session, rol: RolCreate):
    nuevo_rol = Role(nombre=rol.nombre)
    db.add(nuevo_rol)
    db.commit()
    db.refresh(nuevo_rol)
    return nuevo_rol

def add_access_facility_to_role_service(db: Session, id_role:str, id_facility:str):
    role = db.query(Role).filter(Role.id == id_role).first()
    facility = db.query(Facility).filter(Facility.id == id_facility).first()

    if role and facility:
        role.instalaciones.append(facility)  # Agrega la instalación al rol
        db.commit()
    else:
        print("Rol o Instalación no encontrados")

def get_access_facility_rol_by_id_service(db: Session, role_id: int):
    return (
        db.query(Facility)
        .join(rol_instalacion, Facility.id == rol_instalacion.c.instalacion_id)
        .filter(rol_instalacion.c.rol_id == role_id)
        .all()
    )