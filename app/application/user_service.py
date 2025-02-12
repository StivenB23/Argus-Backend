from sqlalchemy.orm import Session
from app.domain.models.user import User
from app.domain.schemas.user import UserCreate
from app.application.encrypt import hash_password

def create_user_service(db: Session, user: UserCreate):
    password_encrypt = hash_password(user.clave)
    new_user = User(nombre=user.nombre, apellido=user.apellido, correo=user.correo, tip_documento=user.tipo_documento, num_documento=user.num_documento, clave=password_encrypt, rol_id=user.rol_id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user