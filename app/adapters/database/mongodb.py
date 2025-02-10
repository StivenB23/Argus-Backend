from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DB_NAME]
