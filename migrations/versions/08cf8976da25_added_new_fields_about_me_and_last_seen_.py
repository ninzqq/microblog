"""Added new fields about_me and last_seen to user model / database

Revision ID: 08cf8976da25
Revises: 5fdab8305698
Create Date: 2019-02-14 06:49:28.830106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08cf8976da25'
down_revision = '5fdab8305698'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=149), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###