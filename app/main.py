from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.api.user_routes import router
from adapters.database.mysql import database
# Inicializar FastAPI
app = FastAPI(title=settings.PROJECT_NAME)
# Eventos para iniciar y cerrar la conexión a MySQL
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
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
