from http.client import HTTPException

from fastapi import APIRouter, Depends, Form, UploadFile, File
from starlette.responses import JSONResponse, FileResponse
from sqlalchemy.orm import Session
import json

from app.adapters.database.mysql import SessionLocal
from app.application.template_service import create_template_service, get_templates_service
from app.domain.schemas.template import TemplateCreateDTO
from app.infraestructure.manageStorage.LocalStorage import LocalStorage

router = APIRouter(tags=["template"], prefix="/templates")
localStorage = LocalStorage(base_path="files/templates/")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_templates(db:Session = Depends(get_db)):
    templates = await get_templates_service(db)
    return templates

@router.get("/archivos/{filename}")
async def get_templates(filename:str):
    file_path = await localStorage.get_file(filename=filename)
    return FileResponse(path=file_path, filename=filename)



@router.post("/")
async def create_template(data:str = Form(...), file:UploadFile = File(), db: Session = Depends(get_db)):
    try:
        if not file or file.filename == "":
            raise HTTPException(status_code=400, detail="No se ha enviado ningún archivo")
        templateCreateDTO = TemplateCreateDTO(**json.loads(data))
        print(f"file: {file}")
        print(f"Recibido archivo: {file.filename}")
        file_saved = await localStorage.save(file=file, filename=file.filename)
        templateCreateDTO.background = file_saved["filename"]
        template_new = await create_template_service(db,templateCreateDTO)
        return template_new
    except Exception as e:
        return JSONResponse(
            content={"error": f"Ocurrió un error: {str(e)}"},
            status_code=500  # Código 500 indica error interno del servidor
        )