"""user model update

Revision ID: 0f9febd87ad5
Revises: 87b2f43ce7d6
Create Date: 2020-08-10 10:57:09.524359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f9febd87ad5'
down_revision = '87b2f43ce7d6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('username', sa.String(), nullable=True))
    op.add_column('users', sa.Column('image', sa.String(), nullable=True))
    pass


def downgrade():
    op.drop_column('users', 'username')
    op.drop_column('users', 'image')
    pass
