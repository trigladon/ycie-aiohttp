import sqlalchemy as sa

from aiohttp_security.abc import AbstractAuthorizationPolicy

from application import tables


class AuthorizationPolicy(AbstractAuthorizationPolicy):

    def __init__(self, db):
        self.db = db

    async def permits(self, identity, permission, context=None):
        if identity is None:
            return False

        async with self.db as conn:
            query = tables.users.select().where(
                sa.and_(tables.users.c.email == identity, sa.not_(tables.users.c.is_active))
            )
            user = await conn.execute(query).fetchone()

            if user is not None:
                # check is superuser
                if user[5]:
                    return True

                # permissions.c.user_id == user_id
                query = tables.permissions.select().where(tables.permissions.c.user_id == user[0])
                result = await conn.execute(query)
                permissions_result = await result.fetchall()

                if result is not None:
                    for record in permissions_result:
                        if record.permission_name == permission:
                            return True

            return False

    async def authorized_userid(self, identity):
        async with self.db as conn:
            query = tables.users.select().where(
                sa.and_(tables.users.c.email == identity, sa.not_(tables.users.c.is_active))
            )
            result = await conn.scalar(query)
            return identity if result else None

