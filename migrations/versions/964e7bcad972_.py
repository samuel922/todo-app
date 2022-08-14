"""empty message

Revision ID: 964e7bcad972
Revises: 22fe28ce85d8
Create Date: 2022-08-13 09:56:59.328258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '964e7bcad972'
down_revision = '22fe28ce85d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###
