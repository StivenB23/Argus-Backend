from app.application.user_service import UserService
from app.domain.user import User
from app.adapters.database.user_repo import UserRepository
from app.application.file_service import cut_out_image, delete_image_upload

from fastapi import APIRouter, Depends, UploadFile, File, Form
from fastapi.responses import JSONResponse
import shutil
import os

router = APIRouter(tags=["users"], prefix="/users")
service = UserService(repository=UserRepository())


@router.get("/message")
def show_message():
    return {"message":"Hello"}

@router.post("/register")
async def create_user(file: UploadFile = File(...), name: str = Form(...), surname: str = Form(...)):
    
    # Definir el directorio de destino
    save_path = "uploads/"
    os.makedirs(save_path, exist_ok=True)

    # Guardar el archivo en el directorio
    file_location = os.path.join(save_path, file.filename)
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    cut_out_image(file.filename)

    delete_image_upload(file.filename)

    # Devolver la respuesta con los datos y la ubicación del archivo
    return JSONResponse(
        content={
            "info": f"Archivo guardado en {file_location}",
            "name": name,
            "surname": surname,
        }
    )
