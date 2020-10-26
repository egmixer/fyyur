"""empty message

Revision ID: 9696b2dd0696
Revises: dccf111505fb
Create Date: 2020-10-26 20:41:46.243126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9696b2dd0696'
down_revision = 'dccf111505fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Show', 'id')
    # ### end Alembic commands ###
