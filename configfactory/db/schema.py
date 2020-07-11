import sqlalchemy as sa

metadata = sa.MetaData()

user_tbl = sa.Table("configfactory_user", metadata)

environment_tbl = sa.Table(
    "configfactory_environment",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String(10), nullable=False),
)

component_tbl = sa.Table("configfactory_component", metadata)
