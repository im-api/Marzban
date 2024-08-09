"""add UserUsageResetLogs Model and data_limit_strategy field to user

Revision ID: d02dcfbf1517
Revises: 671621870b02
Create Date: 2023-02-01 21:10:49.830928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd02dcfbf1517'
down_revision = '671621870b02'
branch_labels = None
depends_on = None


def upgrade() -> None:
    userdatalimitresetstrategy = sa.Enum('no_reset', 'day', 'week', 'month', 'year', name='userdatalimitresetstrategy')
    userdatalimitresetstrategy.create(op.get_bind())

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_usage_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('used_traffic_at_reset', sa.BigInteger(), nullable=False),
    sa.Column('reset_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_usage_logs_id'), 'user_usage_logs', ['id'], unique=False)
    op.add_column('users', sa.Column('data_limit_reset_strategy', sa.Enum("no_reset", "day","week", "month", "year", name="userdatalimitresetstrategy"), nullable=False, server_default="no_reset"))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'data_limit_reset_strategy')
    op.drop_index(op.f('ix_user_usage_logs_id'), table_name='user_usage_logs')
    op.drop_table('user_usage_logs')
    # ### end Alembic commands ###
