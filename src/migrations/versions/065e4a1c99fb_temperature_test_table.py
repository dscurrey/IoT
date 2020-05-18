"""temperature test table

Revision ID: 065e4a1c99fb
Revises: 
Create Date: 2020-05-18 14:21:25.875997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '065e4a1c99fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sensor_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('temperature', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sensor_data')
    # ### end Alembic commands ###
