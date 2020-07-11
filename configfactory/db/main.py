from databases import Database
from fastapi import FastAPI

from configfactory.conf import settings


def setup(app: FastAPI) -> None:
    """
    Setup database connection.
    """
    database = Database(url=settings.database_url)

    app.add_event_handler("startup", database.connect)
    app.add_event_handler("shutdown", database.disconnect)
    app.state.database = database
