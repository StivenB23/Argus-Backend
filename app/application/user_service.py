from sqlalchemy.orm import Session
from app.domain.models.user import User
from app.domain.schemas.identityCard import IdentityCardWithTemplateResponse
from app.domain.schemas.template import TemplateBase
from app.domain.schemas.user import UserCreate, UserResponse, UsersResponse, UserCreated, UserResponseIdentity
from app.application.encrypt import hash_password
from fastapi.exceptions import HTTPException

async def get_users_count_service(db:Session):
    users_count = db.query(User).filter(User.status == "active").count()
    return users_count

async def get_users_service(db:Session):
    users = db.query(User).all()
    usersMappers = [
        UsersResponse(
            id=user.id,
            document_type=user.document_type,
            document_number=user.document_number,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            status=user.status,
            role=user.role.name if user.role else None
        )
        for user in users
    ]
    return usersMappers

async def get_user_by_email(db: Session, email:str):
    user = db.query(User).filter_by(email=email).first();
    if not user:
        raise Exception("Usuario no encontrado")
    return user

async def get_user_by_id(db: Session, id:int):
    user = db.query(User).filter_by(id=id).first()
    if not user:
        raise Exception("Usuario no encontrado")
    user_response = UserResponse(id=user.id, first_name=user.first_name, last_name=user.last_name, email=user.email, role=user.role.name)
    return user_response

async def get_user_by_id_template_service(db: Session, id:int):
    user = db.query(User).filter_by(id=id).first()
    if not user:s
        raise Exception("Usuario no encontrado")

    template = user.identity_card.template
    identity_card = user.identity_card

    template_data = TemplateBase(
        template_name=template.template_name,
        unit=template.unit,
        width=template.width,
        height=template.height,
        photo_width=template.photo_width,
        photo_height=template.photo_height,
        labels=template.labels,
        photo_x=template.photo_x,
        photo_y=template.photo_y,
        background=template.background,
        code_type=template.code_type,
        code_type_y=template.code_type_y,
        code_type_x=template.code_type_x,
    )

    card = IdentityCardWithTemplateResponse(uuid=identity_card.uuid, issue_date=identity_card.issue_date, template=template_data)

    return UserResponseIdentity(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        photo=user.photo,
        document_type=user.document_type,
        document_number=user.document_number,
        role=user.role.name,
        identity_card=card
    )

async def create_user_service(db: Session, user: UserCreate):
    password_encrypt = hash_password(user.password)
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=password_encrypt,
        document_type=user.document_type,
        document_number=user.document_number,
        photo=user.photo,
        role_id=user.role_id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

async def delete_user_by_id_service(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"mensaje": "Usuario eliminado correctamente"}
    else:
        return {"error": "Usuario no encontrado"}

async def update_user_status_by_id(db: Session, id: int, new_status: str):
    user = db.query(User).filter(User.id == id).first()
    if user:
        user.status = new_status
        db.commit()
        db.refresh(user)
        return {"mensaje": "Estado actualizado correctamente"}
    else:
        return {"error": "Usuario no encontrado"}