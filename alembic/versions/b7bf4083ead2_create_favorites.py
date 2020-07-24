"""Create Favorites

Revision ID: b7bf4083ead2
Revises: 
Create Date: 2020-07-23 09:03:54.018285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7bf4083ead2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('markets',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='market_pkey'),
    sa.Column('market_id', sa.INTEGER(), autoincrement=False, nullable=False)
    )

    op.create_table('favorites',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER, autoincrement=False, nullable=False),
    sa.Column('market_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='favorite_pkey'),
    sa.ForeignKeyConstraint(['market_id'], ['markets.id'], name='market_id'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='user_id')
    )

def downgrade():
    op.drop_table('favorites')
    op.drop_table('markets')
