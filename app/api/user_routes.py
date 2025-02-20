from app.application.user_service import create_user_service
from app.domain.user import User
from app.application.file_service import cut_out_image, delete_image_upload
from app.domain.schemas.user import UserCreate
from fastapi import APIRouter, Depends, UploadFile, File, Form
from fastapi.responses import JSONResponse
import shutil
import os
from sqlalchemy.orm import Session
from app.adapters.database.mysql import SessionLocal
from app.api.auth_routes import decode_token
from typing import Annotated

router = APIRouter(tags=["users"], prefix="/users")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/message")
def show_message(user:Annotated[dict, Depends(decode_token)]):
    return {"message":"Hello"}

@router.post("/upload-photo")
async def create_user(file: UploadFile = File(...)):
    
    # Definir el directorio de destino
    save_path = "uploads/"
    os.makedirs(save_path, exist_ok=True)

    # Guardar el archivo en el directorio
    file_location = os.path.join(save_path, file.filename)
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    cut_out_image(file.filename)

    # delete_image_upload(file.filename)

    # Devolver la respuesta con los datos y la ubicación del archivo
    return JSONResponse(
        content={
            "info": f"Archivo guardado en {file_location}"
        }
    )

@router.post("/register")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
  
    create_user_service(db, user)
    # Devolver la respuesta con los datos y la ubicación del archivo
    return JSONResponse(
        content={
            "info": f"Archivo guardado en "
        }
    )
