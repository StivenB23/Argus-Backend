from sqlalchemy.orm import Session
from app.adapters.database.mysql import SessionLocal
from fastapi import APIRouter, Depends, UploadFile, File, Form
from fastapi.responses import JSONResponse
import shutil
import os

from app.application.card_identity_service import get_identity_card_by_uuid_service
from app.infraestructure.util.uuid import is_valid_uuid_format

router = APIRouter(tags=["auth"], prefix="/auth")
from fastapi import APIRouter
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from jose import jwt, JWTError

from app.application.user_service import get_user_by_email
from app.application.encrypt import check_password
from app.application.encrypt import encrypt_text, decrypt_text

from dotenv import load_dotenv
import os

load_dotenv()

key_encrypt = os.getenv("ENCRYPTION_KEY")

# Configuraciones de JWT
SECRET_KEY = "tu_clave_secreta"  # Reemplaza con una clave secreta fuerte
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def encode_token(payload:dict)->str:
    token = jwt.encode(payload, "my-secret", algorithm="HS256")
    return token

def decode_token(token: Annotated[str, Depends(oauth2_scheme)])->dict:
    try:
        data = jwt.decode(token, "my-secret", algorithms=["HS256"])
        return data
    except JWTError:
        # Error genérico si el token no es válido o ha expirado
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token no válido o ha expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )

@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    try:
        print(form_data.username)
        # Verificar si el usuario existe y la contraseña es correcta
        user = await get_user_by_email(db, form_data.username)
        print(user.nombre)
        if user is None:
            raise Exception("Usuario no Existe")
        if not check_password(form_data.password, user.clave):
            raise Exception("Usuario o Contraseña Incorrectos")
        
        token= encode_token({"id":encrypt_text(str(user.id), key_encrypt.encode('utf-8'))})
        return {"access_token": token}
    except Exception as e:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=e.__str__()
            )

@router.post("/verify/identities-cards")
async def authorization_verify_identity_card(code:str = Form(...), db = Depends(get_db)):
    is_valid_uuid = is_valid_uuid_format(code)
    print(f"is valid: {is_valid_uuid}")
    if is_valid_uuid is False:
        raise HTTPException(status_code=400, detail="Código de Carné Invalido")

    identity_card_exist = await get_identity_card_by_uuid_service(uuid=code, db=db)
    if identity_card_exist is None:
        raise HTTPException(status_code=400, detail="Código de Carné no encontrado")

    return JSONResponse(
        content={
            "code": code,
            "access": True
        }
    )