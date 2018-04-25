import os

import yaml
import jinja2

import aiohttp_jinja2
from aiohttp.web import Application
from aiohttp_session import setup as setup_session
from aiohttp_security import SessionIdentityPolicy
from aiohttp_security import setup as setup_security
from aiohttp_session.redis_storage import RedisStorage

from application.authorization.policy import AuthorizationPolicy
from . import db, routes, cache


def add_config(app):
    with open('/'.join([os.path.dirname(__file__), 'config.yaml']), 'r') as f:
        app['config'] = yaml.load(f)


async def create_app(loop):

    app = Application(loop=loop)
    add_config(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(
        '/'.join([os.path.dirname(os.path.dirname(__file__)), app['config']['TEMPLATES']])
    ))

    app.db = await db.init_pg(app)
    redis_pool = await cache.redis_pool(app)

    setup_session(app, RedisStorage(redis_pool))
    setup_security(app, SessionIdentityPolicy(), AuthorizationPolicy(app.db))

    app.on_cleanup.append(db.close_pg)

    routes.setup_routes(app)

    return app
