from sqlalchemy.orm import Session

from app.domain.models.associations import role_facility_association
from app.domain.models.instalacion import Facility
from app.domain.models.role import Role
from app.domain.schemas.rol import RoleCreate

def get_roles_service(db: Session):
    return db.query(Role).all()

async def create_role_service(db: Session, rol: RoleCreate):
    nuevo_rol = Role(name=rol.name)
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
        .join(role_facility_association, Facility.id == role_facility_association.c.instalacion_id)
        .filter(role_facility_association.c.rol_id == role_id)
        .all()
    )