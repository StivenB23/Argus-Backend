from http.client import HTTPException

from fastapi import APIRouter, Depends, Form, UploadFile, File
from starlette.responses import JSONResponse
from sqlalchemy.orm import Session
import json

from app.adapters.database.mysql import SessionLocal
from app.application.template_service import create_template_service
from app.domain.schemas.template import TemplateCreateDTO
from app.infraestructure.LocalStorage import LocalStorage
from app.infraestructure.StorageInterface import StorageInterface

router = APIRouter(tags=["template"], prefix="/templates")
localStorage = LocalStorage(base_path="../files/templates/")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def create_template(data:str = Form(...), file:UploadFile = File(), db: Session = Depends(get_db)):
    try:
        if not file or file.filename == "":
            raise HTTPException(status_code=400, detail="No se ha enviado ningún archivo")
        templateCreateDTO = TemplateCreateDTO(**json.loads(data))
        print(f"file: {file}")
        l = await localStorage.save(file=file, filename=templateCreateDTO.nombre_plantilla+".jpg")
        print(l)

        template_new = await create_template_service(db,templateCreateDTO)
        return template_new
    except Exception as e:
        return JSONResponse(
            content={"error": f"Ocurrió un error: {str(e)}"},
            status_code=500  # Código 500 indica error interno del servidor
        )