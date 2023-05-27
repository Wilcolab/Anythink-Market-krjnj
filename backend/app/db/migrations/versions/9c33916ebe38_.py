"""empty message

Revision ID: 9c33916ebe38
Revises: ca3650a75ce6
Create Date: 2023-05-27 10:27:36.874690

"""
from alembic import op
import sqlalchemy as sa


revision = '9c33916ebe38'
down_revision = 'ca3650a75ce6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'users', sa.Column(
            'is_verified',
            sa.Boolean,
            nullable=False,
            server_default="false"
        )
    )


def downgrade() -> None:
    op.drop_column('users', 'is_verified')