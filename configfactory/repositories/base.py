from databases import Database

from configfactory.utils.dependencies import DependsState


class DatabaseRepository:
    def __init__(self, database: Database = DependsState("database")):
        self.database = database
