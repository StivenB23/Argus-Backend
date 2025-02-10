from app.domain.user import User
from app.adapters.database.user_repo import UserRepository
from typing import Optional

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def register_user(self, user: User) -> User:
        existing_user = await self.repository.get_by_email(user.email)
        if existing_user:
            raise ValueError("User already exists")
        return await self.repository.create(user)
