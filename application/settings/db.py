from aiopg.sa import create_engine


async def init_pg(app):
    conf = app['config']['DATABASE']
    engine = await create_engine(
        database=conf['DATABASE'],
        user=conf['USERNAME'],
        password=conf['PASSWORD'],
        host=conf['HOST'],
        port=conf['PORT'],
        pool_recycle=4 * 60 * 60,
    )
    return engine


async def close_pg(app):
    app.db.close()
    await app.db.wait_closed()
