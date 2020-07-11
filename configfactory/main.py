from fastapi import FastAPI

from configfactory import api, db, auth
from configfactory.conf import settings

from configfactory.routers.environment import router as environment_routers


def get_application() -> FastAPI:
    app = FastAPI(debug=settings.debug, title="ConfigFactory")

    # Setup components
    db.setup(app)
    auth.setup(app)

    # Include routers
    app.include_router(
        environment_routers, prefix="/environments", tags=["Environments"]
    )

    # Setup public API
    api.setup(app)

    return app
