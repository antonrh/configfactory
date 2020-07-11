from configfactory.models import Component


class ComponentService:
    async def create_component(self, component: Component) -> Component:
        return component
