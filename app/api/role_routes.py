from app.domain.schemas.rol import RoleCreate
from app.application.role_service import create_role_service, get_roles_service, add_access_facility_to_role_service, \
    get_access_facility_rol_by_id_service

from sqlalchemy.orm import Session
from app.adapters.database.mysql import SessionLocal
from fastapi import APIRouter, Depends, UploadFile, File, Form
from fastapi.responses import JSONResponse
import shutil
import os

router = APIRouter(tags=["roles"], prefix="/roles")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_roles(db: Session = Depends(get_db)):
    roles = get_roles_service(db)
    # Devolver la respuesta con los datos y la ubicación del archivo
    return roles

@router.get("/{id_role}/facilities")
def get_facility_by_role(id_role:int, db: Session = Depends(get_db)):
    facilities = get_access_facility_rol_by_id_service(db=db, role_id=id_role)
    return facilities

@router.post("/register")
async def create_role(rol: RoleCreate, db: Session = Depends(get_db)):
    await create_role_service(db, rol)
    # Devolver la respuesta con los datos y la ubicación del archivo
    return JSONResponse(
        content={
            "Rol Creado": rol.name
        }
    )

@router.put("/{id_role}/facilities")
def add_instalation_to_role(id_role:str, id_instalation: str = Form(...), db: Session = Depends(get_db)):
    add_access_facility_to_role_service(db=db, id_role=id_role, id_facility=id_instalation)
    return JSONResponse(
        content={
            "role":id_role,
            "Instalacion": id_instalation
        }
    )
