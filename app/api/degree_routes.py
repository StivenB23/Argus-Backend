from sqlalchemy.orm import Session
from app.adapters.database.mysql import SessionLocal
from fastapi import APIRouter, Depends, UploadFile, File, Form
from fastapi.responses import JSONResponse
from app.application.degree_service import create_degree_service
from app.domain.schemas.degree import DegreeCreate
import shutil
import os

router = APIRouter(tags=["degree"], prefix="/degrees")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def create_degree(degree: DegreeCreate, db: Session = Depends(get_db)):
    create_degree_service(db, degree)
    return JSONResponse(
        content={
            "Facultad Creada": degree.nombre
        }
    )