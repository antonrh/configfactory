import uuid
from enum import Enum
from typing import NewType

from pydantic import BaseModel, EmailStr, Field

ProjectIdent = NewType("ProjectIdent", str)
EnvironmentIdent = NewType("EnvironmentIdent", str)
ComponentIdent = NewType("ComponentIdent", str)


class User(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    email: EmailStr
    active: bool = True
    superuser: bool = False


class Project(BaseModel):
    ident: ProjectIdent
    name: str


class Environment(BaseModel):
    ident: EnvironmentIdent
    name: str


class Component(BaseModel):
    ident: ComponentIdent
    name: str


class Config(BaseModel):
    environment: EnvironmentIdent = Field(..., alias="environment_id")
    component: ComponentIdent = Field(..., alias="component_id")


class SettingType(str, Enum):
    str = "str"
    int = "int"


class Setting(BaseModel):
    config: Config
    name: str
    description: str = ""
    type: SettingType = SettingType.str


class SettingValue(BaseModel):
    setting: Setting
