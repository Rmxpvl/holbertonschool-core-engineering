#!/usr/bin/env python3

import asyncio
import websockets

clients = set()

async def connection_handler(websocket):
    clients.add(websocket)
    try:
        async for message in websocket :
            for client in clients:
                await client.send("B:" + message)
    finally:
        clients.remove(websocket)



async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
