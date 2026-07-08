#!/usr/bin/env python3

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    try:
        async for message in websocket:

            clean_message = message.strip()

            if clean_message == "":
                await websocket.send("ERR:EMPTY")

            else:
                await websocket.send("OK:" + clean_message)

    except ConnectionClosed:
        pass


async def start_server():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()  # Garde le serveur actif


if __name__ == "__main__":
    asyncio.run(start_server())
