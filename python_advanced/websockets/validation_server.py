#!/usr/bin/env python3

import asyncio
import websockets

async def main(connection):
    
    async for message in connection:

        clean_message = message.strip()

        if clean_message == "":
            await connection.send("ERR:EMPTY")

        else:
            await connection.send("OK:" + clean_message)

async def start_server():
    async with websockets.serve(main, "localhost", 8765):
        await asyncio.Future()  # Garde le serveur actif

asyncio.run(start_server())
