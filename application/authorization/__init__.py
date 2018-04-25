import sqlalchemy as sa

from passlib.hash import sha256_crypt


async def check_password(db, email, password):
    async with db as conn:
        query = db.users.select().where(sa.and_(db.users.c.email == email, sa.not_(db.users.c.disabled)))
        user = await conn.execute(query).fetchone()
        if user is not None:
            return sha256_crypt.verify(password, user[2])
    return False