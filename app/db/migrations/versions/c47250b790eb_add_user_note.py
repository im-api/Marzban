"""add user note

Revision ID: c47250b790eb
Revises: 35f7f8fa9cf2
Create Date: 2023-07-16 15:26:51.350468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c47250b790eb'
down_revision = '35f7f8fa9cf2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('note', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'note')
    # ### end Alembic commands ###
