import aiohttp_jinja2
from aiohttp.web import View, json_response


class Index(View):

    @aiohttp_jinja2.template('application/index.html')
    async def get(self):
        return {"title": "Main page 1"}

    async def post(self):
        return json_response({"status": "done"})
