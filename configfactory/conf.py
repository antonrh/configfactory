from pathlib import Path
from typing import cast

from lazy_object_proxy import Proxy
from pydantic import BaseSettings, Field

base_dir = Path(__file__).resolve(strict=True).parent
root_dir = base_dir.parent


class Settings(BaseSettings):
    debug: bool = Field(False, env="APP_DEBUG")
    database_url: str = Field("sqlite://", env="DATABASE_URL")

    class Config:
        env_file = ".env"


def load_settings() -> Settings:
    return Settings()


settings = cast(Settings, Proxy(load_settings))
