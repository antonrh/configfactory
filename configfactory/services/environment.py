from fastapi import Depends

from configfactory.models import Environment
from configfactory.repositories.environment import EnvironmentRepository


class EnvironmentService:
    def __init__(self, environment_repository: EnvironmentRepository = Depends()):
        self.environment_repository = environment_repository

    async def create_environment(self, environment: Environment) -> Environment:
        # Add validation
        await self.environment_repository.save(environment)
        return environment
