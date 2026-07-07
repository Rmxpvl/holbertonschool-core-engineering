#!/usr/bin/env python3

import websockets
import asyncio

async def connect_and_send(uri, message):
    async for message in message:
        await 

async def main():
    async with websockets.serve(connect_and_send, "localhost", 8765):
        await asyncio.Future()