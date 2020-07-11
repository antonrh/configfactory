from pydantic import BaseModel

from configfactory.models import EnvironmentIdent


class EnvironmentCreate(BaseModel):
    ident: EnvironmentIdent
    name: str
