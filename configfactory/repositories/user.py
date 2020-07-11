import sqlalchemy as sa

from configfactory.db.schema import user_tbl
from configfactory.models import User
from configfactory.repositories.base import DatabaseRepository


class UserRepository(DatabaseRepository):
    async def exists_by_email(self, email: str) -> bool:
        return await self.database.fetch_val(
            sa.select([sa.exists([1]).where(user_tbl.c.email == email)])
        )

    async def create(self, user: User) -> None:
        await self.database.execute(
            user_tbl.insert().values(**user.dict(exclude={"created_at", "updated_at"}))
        )
