import json
from typing import Callable

from . import Transport

from aiohttp import web


class InvalidMessageError(Exception):
    pass


class Http(Transport):
    def __init__(self, host: str, port: int, message_router: Callable) -> None:
        self.host = host
        self.port = port
        self.message_router = message_router

    def setup(self) -> None:
        app = web.Application()
        app.add_routes([web.post("/", self.message_handler)])
        web.run_app(app, host=self.host, port=self.port)

    async def message_handler(self, request):
        body = await self.parse_message(request)
        self.message_router(body)
        return web.Response(text="OK", status=200)

    async def parse_message(self, request):
        try:
            body = await request.json()
        except json.JSONDecodeError:
            raise InvalidMessageError(
                "Request body must contain an application/json payload"
            )

