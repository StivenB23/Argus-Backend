from sqlalchemy.orm import Session
from app.domain.models.user import User
from app.domain.schemas.user import UserCreate
from app.application.encrypt import hash_password
from fastapi.exceptions import HTTPException

def get_user_by_email(db: Session, email:str):
    user = db.query(User).filter_by(email=email).first();
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

def create_user_service(db: Session, user: UserCreate):
    password_encrypt = hash_password(user.clave)
    new_user = User(nombre=user.nombre, apellido=user.apellido, correo=user.correo, tip_documento=user.tipo_documento, num_documento=user.num_documento, clave=password_encrypt, rol_id=user.rol_id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user