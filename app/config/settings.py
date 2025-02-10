from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "My FastAPI Project"
    DEBUG: bool = True
    SECRET_KEY: str = "supersecretkey"
    
    # Configuración de MongoDB
    MONGO_URI: str = "mongodb://localhost:27017"
    DB_NAME: str = "Argus"

    class Config:
        env_file = ".env"  # Carga variables desde un archivo .env

settings = Settings()
