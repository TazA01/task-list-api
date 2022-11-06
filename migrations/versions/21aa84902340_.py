"""empty message

Revision ID: 21aa84902340
Revises: 
Create Date: 2022-11-05 21:49:43.799637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21aa84902340'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'title')
    # ### end Alembic commands ###
