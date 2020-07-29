"""Add password to users

Revision ID: 87b2f43ce7d6
Revises: b7bf4083ead2
Create Date: 2020-07-25 19:17:24.514186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87b2f43ce7d6'
down_revision = 'b7bf4083ead2'
branch_labels = None
depends_on = None


def upgrade():
   op.add_column('users', sa.Column('hashed_password', sa.String(), nullable=False))

def downgrade():
    op.drop_column('users', 'hashed_password')
   