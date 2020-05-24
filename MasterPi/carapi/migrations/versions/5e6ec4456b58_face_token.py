"""face token

Revision ID: 5e6ec4456b58
Revises: bb0f3918102c
Create Date: 2020-05-24 16:15:10.812703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e6ec4456b58'
down_revision = 'bb0f3918102c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_user_face_token'), 'user', ['face_token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_face_token'), table_name='user')
    # ### end Alembic commands ###
