from sqlalchemy.orm import Session
from app.domain.models.department import Department
from app.domain.schemas.department import DepartmentCreate

def create_department_service(db: Session, department: DepartmentCreate):
    new_department = Department(nombre=department.nombre, codigo = department.codigo, descripcion = department.descripcion, correo_contacto = department.correo_contacto)
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return new_department

def search_departments_by_name(db: Session, search_term: str):
    search_pattern = f"%{search_term}%"  # Patrón para buscar coincidencias parciales
    results = db.query(Department).filter(Department.nombre.like(search_pattern)).all()
    return results
