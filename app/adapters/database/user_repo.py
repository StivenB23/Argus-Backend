from app.domain.user import User
from app.adapters.database.mongodb import db
from typing import Optional

class UserRepository:
    collection = db["users"]

    async def create(self, user: User) -> User:
        user_data = user.dict()
        await self.collection.insert_one(user_data)
        return user

    async def get_by_email(self, email: str) -> Optional[User]:
        user_data = await self.collection.find_one({"email": email})
        return User(**user_data) if user_data else None
    

    
