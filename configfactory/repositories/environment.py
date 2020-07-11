from typing import List

from configfactory.models import Environment

from .base import DatabaseRepository


class EnvironmentRepository(DatabaseRepository):
    async def find_all(self) -> List[Environment]:
        return []

    async def save(self, environment: Environment) -> None:
        pass
