from configfactory.models import EnvironmentIdent
from pydantic import BaseModel


class EnvironmentCreate(BaseModel):
    ident: EnvironmentIdent
    name: str
