#!/usr/bin/env python3

from pathlib import Path

from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route, WebSocketRoute

BASE_DIR = Path(__file__).resolve().parent


async def homepage(request):
    return FileResponse(BASE_DIR / "index.html")


async def chat_js(request):
    return FileResponse(BASE_DIR / "chat.js", media_type="application/javascript")


async def styles_css(request):
    return FileResponse(BASE_DIR / "styles.css", media_type="text/css")


async def websocket_endpoint(websocket):
    await websocket.accept()

    while True:
        message = await websocket.receive_text()
        await websocket.send_text(message)


app = Starlette(
    routes=[
        Route("/", homepage),
        Route("/chat.js", chat_js),
        Route("/styles.css", styles_css),
        WebSocketRoute("/ws", websocket_endpoint),
    ]
)
