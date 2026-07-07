import websockets
import asyncio

async def connection_handler(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()  # Garde le serveur actif

asyncio.run(main())