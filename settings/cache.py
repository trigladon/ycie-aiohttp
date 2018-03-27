from aioredis import create_pool


async def init_redis_pool(app):
    conf = app['config']['CACHE']
    return await create_pool(
        (conf['HOST'], conf['PORT']),
        # encoding=conf['ENCODING'],
        db=conf['DB'],
        # password=conf['PASSWORD'],
        # ssl=conf['SSL'],
        # timeout=conf['TIMEOUT']
    )


async def close_redis(app):
    app['cache'].close()
    await app['cache'].wait_closed()
