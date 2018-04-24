import uvloop
import asyncio
from aiohttp import web

from application.settings import create_app


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    web.run_app(app=create_app(asyncio.get_event_loop()), host='0.0.0.0', port=8000)
