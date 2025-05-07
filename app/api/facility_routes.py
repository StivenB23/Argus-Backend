from fastapi import APIRouter, Depends

from app.adapters.database.mysql import SessionLocal
from sqlalchemy.orm import Session

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