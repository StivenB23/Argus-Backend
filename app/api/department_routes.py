from sqlalchemy.orm import Session
from app.adapters.database.mysql import SessionLocal
from fastapi import APIRouter, Depends, UploadFile, File, Form
from fastapi.responses import JSONResponse
import shutil
import os
from app.domain.schemas.department import DepartmentCreate
from app.application.department_service import create_department_service

router = APIRouter(tags=["department"], prefix="/department")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def create_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    create_department_service(db, department)
    return JSONResponse(
        content={
            "Facultad Creada": department.nombre
        }
    )