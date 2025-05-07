from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.domain.models.associations import role_facility_association
from app.domain.models.instalacion import Facility
from app.domain.models.role import Role
from app.domain.schemas.rol import RoleCreate, RoleFacilityResponse, RoleUpdate
from app.domain.schemas.facility import FacilityResponse


async def get_roles_service(db: Session):
    roles = db.query(Role).all()
    return roles

async def get_roles_with_facilities_service(db: Session):
    roles = db.query(Role).all()
    roles_mapper = [
        RoleFacilityResponse(
            id=role.id,
            name=role.name,
            is_active=role.is_active,
            facilities=[
                FacilityResponse.from_orm(facility) for facility in role.facilities
            ]
        )
        for role in roles
    ]
    return roles_mapper


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

async def update_role_service(db:Session, id:int, role_update: RoleUpdate):
    # 1. Buscar el rol
    role = db.query(Role).filter(Role.id == id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Rol no encontrado")

    # 2. Actualizar el nombre
    role.name = role_update.name

    # 3. Cargar las instalaciones con los IDs dados
    facilities = db.query(Facility).filter(Facility.id.in_(role_update.facilities)).all()

    if len(facilities) != len(role_update.facilities):
        raise HTTPException(status_code=400, detail="Una o más instalaciones no existen")

    # 4. Reemplazar relaciones muchos-a-muchos
    role.facilities = facilities

    # 5. Guardar cambios
    db.commit()
    db.refresh(role)

    return {"message": "Rol actualizado correctamente", "id": role.id}