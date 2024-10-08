"""add notification reminders

Revision ID: a6e3fff39291
Revises: 015cf1dc6eca
Create Date: 2023-08-21 18:04:37.096599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6e3fff39291'
down_revision = '015cf1dc6eca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notification_reminders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.Enum('expiration_date', 'data_usage', name='remindertype'), nullable=False),
    sa.Column('expires_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notification_reminders_id'), 'notification_reminders', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_notification_reminders_id'), table_name='notification_reminders')
    op.drop_table('notification_reminders')
    # ### end Alembic commands ###
