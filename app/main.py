from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import role_routes, user_routes, department_routes
from app.adapters.database.mysql import engine

from app.domain.models.base import Base

# Inicializar FastAPI
app = FastAPI(title="Argus🌌")

Base.metadata.create_all(bind=engine)


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

# Ruta de prueba
@app.get("/test")
def health_check():
    return {"message": "¡FastAPI está funcionando!"}
