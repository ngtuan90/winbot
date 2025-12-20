import asyncio
import json
import websockets
from winbot import Winbot

HOST = "0.0.0.0"
PORT = 8765

robot = Winbot()


async def handle_client(websocket):
    print("✅ Client connected")

    try:
        async for message in websocket:
            data = json.loads(message)

            # New differential-drive protocol
            if "linear" in data and "angular" in data:
                linear = float(data.get("linear", 0))
                angular = float(data.get("angular", 0))
                speed = int(data.get("speed", 60))

                robot.drive(
                    linear=linear,
                    angular=angular,
                    max_speed=speed
                )

            # Optional backward compatibility
            elif "cmd" in data:
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
        print("❌ Client disconnected")

    finally:
        robot.stop()


async def main():
    async with websockets.serve(handle_client, HOST, PORT):
        print(f"🚀 WebSocket server running on port {PORT}")
        await asyncio.Future()  # run forever


asyncio.run(main())
