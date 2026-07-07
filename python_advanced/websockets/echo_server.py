#!/usr/bin/env python3

import asyncio
import websockets


async def connect_and_send(uri, message):
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)

        reponse = await websocket.recv()

        print(reponse)


if __name__ == "__main__":
    asyncio.run(connect_and_send("ws://localhost:8765", "Hello WebSocket"))
