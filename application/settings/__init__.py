import os

import yaml
import jinja2

import aiohttp_jinja2
from aiohttp.web import Application

from . import db, routes


def add_config(app):
    with open('/'.join([os.path.dirname(__file__), 'config.yaml']), 'r') as f:
        app['config'] = yaml.load(f)


def setup(app):
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(
        '/'.join([os.path.dirname(os.path.dirname(__file__)), app['config']['TEMPLATES']])
    ))


def create_app(loop):
    app = Application(loop=loop, middlewares=[])
    add_config(app)
    setup(app)
    routes.setup_routes(app)

    app.on_startup.append(db.init_pg)
    app.on_cleanup.append(db.close_pg)

    return app
