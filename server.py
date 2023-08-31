#!/usr/bin/env python

import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        print(message)
        await websocket.send("Hi Arun Welcome!!!!")

async def main():
    async with serve(echo, "localhost", 6000):
        await asyncio.Future()

asyncio.run(main())
