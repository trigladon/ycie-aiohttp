import sqlalchemy as sa
from sqlalchemy.sql import func

metadata = sa.MetaData()

users = sa.Table(
    'users', metadata,
    sa.Column('id', sa.BigInteger, primary_key=True),
    sa.Column('email', sa.String(256), nullable=False),
    sa.Column('password', sa.String(128), nullable=False),
    sa.Column('first_name', sa.String(256), nullable=False),
    sa.Column('last_name', sa.String(256), nullable=False),
    sa.Column('is_superuser', sa.Boolean, nullable=False, server_default='FALSE'),
    sa.Column('is_active', sa.Boolean, nullable=False, server_default='TRUE'),
    sa.Column('create_date', sa.DateTime(timezone=True), server_default=func.now()),

    # indices
    sa.UniqueConstraint('email', name='user_email_key'),
)

permissions = sa.Table(
    'permissions', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('user_id', sa.Integer, nullable=False),
    sa.Column('permission_name', sa.String(64), nullable=False),

    # indices
    sa.ForeignKeyConstraint(['user_id'], [users.c.id], name='user_permission_fkey', ondelete='CASCADE'),
)
