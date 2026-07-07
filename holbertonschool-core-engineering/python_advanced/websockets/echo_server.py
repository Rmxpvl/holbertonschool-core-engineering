#!/usr/bin/env python3

import websockets
import asyncio

async def connection_handler(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()  # Garde le serveur actif

if __name__ == "__main__":
    asyncio.run(main())