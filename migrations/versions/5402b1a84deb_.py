"""empty message

Revision ID: 5402b1a84deb
Revises: b94042b76f6f
Create Date: 2020-04-20 17:12:32.498329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5402b1a84deb'
down_revision = 'b94042b76f6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('showname', sa.String(length=64), nullable=True),
    sa.Column('shwonameen', sa.String(length=128), nullable=True),
    sa.Column('director', sa.String(length=64), nullable=True),
    sa.Column('leadingRole', sa.String(length=256), nullable=True),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('language', sa.String(length=64), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('screeningmodel', sa.String(length=32), nullable=True),
    sa.Column('openday', sa.DateTime(), nullable=True),
    sa.Column('backgroundpicture', sa.String(length=256), nullable=True),
    sa.Column('flag', sa.Boolean(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    # ### end Alembic commands ###