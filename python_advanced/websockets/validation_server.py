#!/usr/bin/env python3

import asyncio
import os
import sys
import websockets

async def main(connection):
    
    async for message in connection:

        clean_message = message.strip()

        if clean_message == "":
            await connection.send("ERR:EMPTY")

        else:
            await connection.send("OK:" + message)
