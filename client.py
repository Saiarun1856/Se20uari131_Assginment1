import asyncio
from websockets.sync.client import connect

def servers():
    with connect("ws://localhost:6000") as websocket:
        websocket.send("Hello message from server !")
        message = websocket.recv()
        print(f"Received: {message}")
        msg2 = websocket.recv()

servers()
