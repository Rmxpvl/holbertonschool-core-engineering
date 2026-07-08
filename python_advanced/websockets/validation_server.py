#!/usr/bin/env python3

async def main(connection):
    message = await connection.recv()

    response = "OK:" + message
    
    await connection.send(response)

if clean_message == "":
    await connection.send("ERR:EMPTY")

    else:
        await connection.send("OK:" + message)
