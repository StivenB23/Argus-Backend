from fastapi import APIRouter, Depends, UploadFile, File
from app.application.user_service import UserService
from app.domain.user import User
from app.adapters.database.user_repo import UserRepository

router = APIRouter(tags=["users"], prefix="/users")
service = UserService(repository=UserRepository())


@router.get("/message")
def show_message():
    return {"message":"Hello"}

@router.post("/register")
async def create_user(file: UploadFile = File(...),):
    return await service.register_user(user)
