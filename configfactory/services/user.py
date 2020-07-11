from fastapi import Depends
from pydantic import EmailStr, ValidationError

from configfactory.exceptions import UserCreateError
from configfactory.models import User
from configfactory.repositories import UserRepository

_ = str


class UserService:
    def __init__(self, user_repository: UserRepository = Depends()):
        self.user_repository = user_repository

    async def create_user(
        self,
        email: EmailStr,
        *,
        password: str,
        active: bool = True,
        superuser: bool = False,
    ) -> User:
        if await self.user_repository.exists_by_email(email):
            raise UserCreateError(_("User with this email already exists."))

        try:
            user = User(email=email, active=active, superuser=superuser)
        except ValidationError as exc:
            raise UserCreateError(_(f"Invalid user: {exc.errors()}"))

        await self.user_repository.create(user)

        return user

    async def create_superuser(self, email: EmailStr, *, password: str) -> User:
        return await self.create_user(
            email, password=password, active=True, superuser=True
        )
