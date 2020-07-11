from configfactory.models import Component, ComponentName


class ComponentService:
    async def create_component(self, name: ComponentName) -> Component:
        return Component(name=name)
