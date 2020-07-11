import sqlalchemy as sa

metadata = sa.MetaData()

environment_tbl = sa.Table(
    "configfactory_environment",
    metadata,
    sa.Column("ident", sa.String(32), primary_key=True),
    sa.Column("name", sa.String(32), nullable=False),
)
