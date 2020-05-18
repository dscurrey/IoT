"""Added timestamp

Revision ID: b1d68de88462
Revises: 3d257bbc7096
Create Date: 2020-05-18 17:33:17.737261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1d68de88462'
down_revision = '3d257bbc7096'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sensor_data', sa.Column('timestamp', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sensor_data', 'timestamp')
    # ### end Alembic commands ###
