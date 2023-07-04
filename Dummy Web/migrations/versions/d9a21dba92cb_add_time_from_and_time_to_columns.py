"""Add time_from and time_to columns

Revision ID: d9a21dba92cb
Revises: 
Create Date: 2023-07-03 13:20:16.600514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9a21dba92cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('time_from', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('time_to', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.drop_column('time_to')
        batch_op.drop_column('time_from')

    # ### end Alembic commands ###