from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.api.routes import router

# Inicializar FastAPI
app = FastAPI(title=settings.PROJECT_NAME)

# Configurar CORS (Permitir peticiones desde frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(router)

# Ruta de prueba
@app.get("/test")
def health_check():
    return {"message": "¡FastAPI está funcionando!"}
