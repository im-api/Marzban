"""proxy table

Revision ID: 8e849e06f131
Revises: 9b60be6cd0a2
Create Date: 2022-12-26 05:47:14.745622

"""
import json
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = '8e849e06f131'
down_revision = '9b60be6cd0a2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    proxies_table = op.create_table('proxies', sa.Column('id', sa.Integer(),
                                                         nullable=False),
                                    sa.Column('user_id', sa.Integer(),
                                              nullable=True),
                                    sa.Column(
                                        'type', sa.Enum(
                                            'VMess', 'VLESS', 'Trojan', 'Shadowsocks', name='proxytypes'),
                                        nullable=False),
                                    sa.Column('settings', sa.JSON(),
                                              nullable=False),
                                    sa.ForeignKeyConstraint(['user_id'],
                                                            ['users.id'],),
                                    sa.PrimaryKeyConstraint('id'))

    conn = op.get_bind()
    q = conn.execute('SELECT id, proxy_type, settings FROM users')
    results = q.fetchall()
    op.bulk_insert(proxies_table, [{"user_id": p[0], "type": p[1], "settings": json.loads(p[2])} for p in results])

    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('created_at',
                              existing_type=sa.DATETIME(),
                              nullable=True,
                              existing_server_default=sa.text('(CURRENT_TIMESTAMP)'))
        batch_op.drop_column('proxy_type')
        batch_op.drop_column('settings')
    op.create_index(op.f('ix_proxies_id'), 'proxies', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    raise NotImplemented

    with op.batch_alter_table('users') as batch_op:
        batch_op.add_column(sa.Column('settings', sqlite.JSON(), nullable=False))
        batch_op.add_column(sa.Column('proxy_type', sa.VARCHAR(length=11), nullable=False))
        batch_op.alter_column('created_at',
                              existing_type=sa.DATETIME(),
                              nullable=False,
                              existing_server_default=sa.text('(CURRENT_TIMESTAMP)'))
    op.drop_index(op.f('ix_proxies_id'), table_name='proxies')
    op.drop_table('proxies')
    # ### end Alembic commands ###
