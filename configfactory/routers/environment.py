from typing import List

from fastapi import APIRouter, Depends

from configfactory.models import Environment
from configfactory.repositories import EnvironmentRepository
from configfactory.services.environment import EnvironmentService

router = APIRouter()


@router.get("/", summary="Find available environment", response_model=List[Environment])
async def get_environments(environment_repository: EnvironmentRepository = Depends()):
    return await environment_repository.find_all()


@router.post("/", summary="Create environment", response_model=Environment)
async def create_environment(
    environment: Environment, environment_service: EnvironmentService = Depends()
):
    return await environment_service.create_environment(environment)
