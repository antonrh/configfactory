from configfactory.models import Project, ProjectIdent


class ProjectService:
    async def create_project(self, _id: ProjectIdent, name: str) -> Project:
        return Project(ident=_id, name=name)
