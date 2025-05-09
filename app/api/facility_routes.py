from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from app.adapters.database.mysql import SessionLocal
from sqlalchemy.orm import Session

from app.application.card_identity_service import get_role_from_identity_by_uuid_service
from app.application.facilities_service import get_facilities_service

router = APIRouter(tags=["facilities"], prefix="/facilities")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_department(db: Session = Depends(get_db)):
    departments = await get_facilities_service(db)
    return departments

@router.get("/validate/{id_institucion}")
async def get_validate_role(id_institucion:int, db: Session = Depends(get_db)):
   role = await get_role_from_identity_by_uuid_service(db=db, uuid="3-2025-4654-204537")
   has_access = any(facility.id == id_institucion for facility in role.facilities)

   if not has_access:
       raise HTTPException(status_code=403, detail="No tienes acceso a esta institución")

   return {"Access":"True"}
