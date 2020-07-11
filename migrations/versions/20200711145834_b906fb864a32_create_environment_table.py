"""Create environment table

Revision ID: b906fb864a32
Revises: 
Create Date: 2020-07-11 14:58:34.806112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b906fb864a32"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "configfactory_environment",
        sa.Column("ident", sa.String(length=32), nullable=False),
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.PrimaryKeyConstraint("ident"),
    )


def downgrade():
    op.drop_table("configfactory_environment")
