import asyncio
import json
import websockets
from winbot import Winbot

HOST = "0.0.0.0"
PORT = 8765
robot=Winbot()

async def handle_client(websocket):
    print("Client connected")

    try:
        async for message in websocket:
            data = json.loads(message)
            cmd = data.get("cmd")

            if cmd == "forward":
                robot.forward()
            elif cmd == "backward":
                robot.backward()
            elif cmd == "left":
                robot.left()
            elif cmd == "right":
                robot.right()
            elif cmd == "stop":
                robot.stop()

    except websockets.ConnectionClosed:
        print("Client disconnected")
    finally:
        robot.stop()

async def main():
    async with websockets.serve(handle_client, HOST, PORT):
        print(f"WebSocket server running on {PORT}")
        await asyncio.Future()

asyncio.run(main())
