import asyncio

from configfactory.models import EnvironmentIdent, ComponentIdent
from configfactory.services.component import ComponentService
from configfactory.services.environment import EnvironmentService


async def main():
    environment_service = EnvironmentService()
    component_service = ComponentService()

    environment = await environment_service.create_environment(
        ident=EnvironmentIdent("development"), name="Development"
    )

    component = await component_service.create_component(
        name=ComponentIdent("database")
    )


asyncio.run(main())
