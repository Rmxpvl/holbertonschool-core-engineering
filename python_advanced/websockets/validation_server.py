#!/usr/bin/env python3

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

async def main(connection):
    try:
        async for message in connection:

            clean_message = message.strip()

            if clean_message == "":
                await connection.send("ERR:EMPTY")

            else:
                await connection.send("OK:" + clean_message)

    except ConnectionClosed:
        pass


async def start_server():
    async with websockets.serve(main, "localhost", 8765):
        await asyncio.Future()  # Garde le serveur actif

asyncio.run(start_server())
