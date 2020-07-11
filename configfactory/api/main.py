from fastapi import FastAPI

from configfactory.api.router import router


def setup(app: FastAPI):
    app.include_router(router, prefix="/api", tags=["API"])
