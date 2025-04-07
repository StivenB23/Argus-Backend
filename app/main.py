from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import role_routes, user_routes, department_routes, auth_routes, degree_routes, template_routes
from app.adapters.database.mysql import engine, SessionLocal

from app.domain.models.base import Base
from app.domain.models.department import Department
from app.domain.models.instalacion import Facility

# Inicializar FastAPI
app = FastAPI(
    title="Argus🌌",
    description="Un sistema de monitoreo avanzado basado en inteligencia artificial.",
    version="1.0.0",
    terms_of_service="https://example.com/terms/",
    contact={
        "name": "Key Ospina",
        "url": "https://keyospina.dev",
        "email": "contacto@keyospina.dev",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

Base.metadata.create_all(bind=engine)

# Función para insertar datos iniciales en la tabla "departments"
def insert_initial_departments():
    db = SessionLocal()
    existing = db.query(Department).first()  # Verificar si hay datos
    if not existing:
        departments = [
            Department(codigo="FIS", nombre="Facultad de Ingeniería y Sistemas", descripcion="Facultad dedicada a la ingeniería y tecnologías de la información.", correo_contacto="ingenieria@universidad.edu"),
            Department(codigo="FCB", nombre="Facultad de Ciencias Biológicas", descripcion="Facultad enfocada en estudios biológicos y ambientales.", correo_contacto="biologia@universidad.edu"),
            Department(codigo="FCH", nombre="Facultad de Ciencias Humanas", descripcion="Facultad dedicada a la educación, sociología y humanidades.", correo_contacto="humanidades@universidad.edu"),
            Department(codigo="FCM", nombre="Facultad de Ciencias Médicas", descripcion="Facultad de medicina y ciencias de la salud.", correo_contacto="medicina@universidad.edu"),
            Department(codigo="FCE", nombre="Facultad de Ciencias Económicas", descripcion="Facultad especializada en economía, administración y contaduría.", correo_contacto="economia@universidad.edu")
        ]
        db.add_all(departments)
        db.commit()
    db.close()

def insert_initial_instalation():
    db = SessionLocal()
    existing = db.query(Facility).first()
    if not existing:
        facilities = [
            Facility(nombre="Sede Principal", tipo="Sede", direccion="Cra 10"),
            Facility(nombre="Sede Financiera", tipo="Sede", direccion="Cra 10"),
            Facility(nombre="Sede Ingenieria", tipo="Sede", direccion="Cra 10"),
            Facility(nombre="Laboratorio", tipo="Sede", direccion="Cra 10")
        ]
        db.add_all(facilities)
        db.commit()
    db.close()

# Llamar a la función después de crear las tablas
insert_initial_departments()
insert_initial_instalation()

# Configurar CORS (Permitir peticiones desde frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(user_routes.router)
app.include_router(role_routes.router)
app.include_router(department_routes.router)
app.include_router(auth_routes.router)
app.include_router(degree_routes.router)
app.include_router(template_routes.router)

# Ruta de prueba
@app.get("/test")
def health_check():
    return {"message": "¡FastAPI está funcionando!"}
