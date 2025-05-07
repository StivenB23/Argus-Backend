from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import role_routes, user_routes, department_routes, facility_routes, auth_routes, degree_routes, template_routes, websocktes
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
        "name": "Stiven Ospina",
        "url": "https://keyospina.dev",
        "email": "stiven23ospi@keyospina.dev",
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
            Department(code="FIS", name="Facultad de Ingeniería y Sistemas", description="Facultad dedicada a la ingeniería y tecnologías de la información.", contact_email="ingenieria@universidad.edu"),
            Department(code="FCB", name="Facultad de Ciencias Biológicas", description="Facultad enfocada en estudios biológicos y ambientales.", contact_email="biologia@universidad.edu"),
            Department(code="FCH", name="Facultad de Ciencias Humanas", description="Facultad dedicada a la educación, sociología y humanidades.", contact_email="humanidades@universidad.edu"),
            Department(code="FCM", name="Facultad de Ciencias Médicas", description="Facultad de medicina y ciencias de la salud.", contact_email="medicina@universidad.edu"),
            Department(code="FCE", name="Facultad de Ciencias Económicas", description="Facultad especializada en economía, administración y contaduría.", contact_email="economia@universidad.edu")
        ]
        db.add_all(departments)
        db.commit()
    db.close()

def insert_initial_instalation():
    db = SessionLocal()
    existing = db.query(Facility).first()
    if not existing:
        facilities = [
            Facility(name="Sede Principal", type="Sede", address="Cra 10"),
            Facility(name="Sede Financiera", type="Sede", address="Cra 10"),
            Facility(name="Sede Ingenieria", type="Sede", address="Cra 10"),
            Facility(name="Laboratorio", type="Sede", address="Cra 10")
        ]
        db.add_all(facilities)
        db.commit()
    db.close()

# Llamar a la función después de crear las tablas
insert_initial_departments()
insert_initial_instalation()

origins = [
    "http://localhost:5173",
]

# Configurar CORS (Permitir peticiones desde frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
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
app.include_router(facility_routes.router)

#Websockets
app.include_router(websocktes.router)

# Ruta de prueba
@app.get("/test")
def health_check():
    return {"message": "¡FastAPI está funcionando!"}
