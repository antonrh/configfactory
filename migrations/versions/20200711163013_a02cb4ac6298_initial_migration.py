"""Initial migration

Revision ID: a02cb4ac6298
Revises: 
Create Date: 2020-07-11 16:30:13.051187

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy_utils.types.uuid import UUIDType

# revision identifiers, used by Alembic.
revision = "a02cb4ac6298"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "environment",
        sa.Column("ident", sa.String(length=32), nullable=False),
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("ident"),
    )
    op.create_table(
        "user",
        sa.Column("id", UUIDType(binary=False), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password", sa.String(length=255), server_default="", nullable=False),
        sa.Column("active", sa.Boolean(), server_default="1", nullable=False),
        sa.Column("superuser", sa.Boolean(), server_default="0", nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade():
    op.drop_table("user")
    op.drop_table("environment")
