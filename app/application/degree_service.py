from sqlalchemy.orm import Session
from app.domain.schemas.degree import DegreeCreate
from app.domain.models.degree import Degree

def create_degree_service(db: Session, department: DegreeCreate):
    new_degree = Degree(
        nombre=department.nombre,
        codigo=department.codigo,
        descripcion=department.descripcion,
        correo_contacto=department.correo_contacto
    )
    db.add(new_degree)
    db.commit()
    db.refresh(new_degree)
    return new_degree