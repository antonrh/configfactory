import sqlalchemy as sa
from sqlalchemy_utils.types import UUIDType

metadata = sa.MetaData()

user_tbl = sa.Table(
    "user",
    metadata,
    sa.Column("id", UUIDType(binary=False), primary_key=True),
    sa.Column("email", sa.String(255), nullable=False, unique=True),
    sa.Column("password", sa.String(255), nullable=False, server_default=""),
    sa.Column("active", sa.Boolean, nullable=False, server_default="1"),
    sa.Column("superuser", sa.Boolean, nullable=False, server_default="0"),
    sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    sa.Column("updated_at", sa.DateTime(timezone=True), onupdate=sa.func.now()),
)

environment_tbl = sa.Table(
    "environment",
    metadata,
    sa.Column("ident", sa.String(32), primary_key=True),
    sa.Column("name", sa.String(32), nullable=False),
    sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    sa.Column("updated_at", sa.DateTime(timezone=True), onupdate=sa.func.now()),
)
