from app.domain.schemas.rol import RolCreate
from app.application.role_service import create_role_service, get_roles_service


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
    return roles;

@router.post("/register")
async def create_role(rol: RolCreate, db: Session = Depends(get_db)):
    create_role_service(db, rol)
    # Devolver la respuesta con los datos y la ubicación del archivo
    return JSONResponse(
        content={
            "Rol Creado": rol.nombre
        }
    )
