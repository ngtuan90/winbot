import asyncio
import json
import websockets
import keyboard  # pip install keyboard

PI_IP = "192.168.1.185"   # change this
PORT = 8765

async def send_commands():
    uri = f"ws://{PI_IP}:{PORT}"

    async with websockets.connect(uri) as ws:
        print("Connected to robot")

        last_cmd = None

        while True:
            if keyboard.is_pressed("w"):
                cmd = "forward"
            elif keyboard.is_pressed("s"):
                cmd = "backward"
            elif keyboard.is_pressed("a"):
                cmd = "left"
            elif keyboard.is_pressed("d"):
                cmd = "right"
            else:
                cmd = "stop"

            if cmd != last_cmd:
                msg = json.dumps({"cmd": cmd})
                await ws.send(msg)
                last_cmd = cmd

            await asyncio.sleep(0.05)  # 20 Hz update

asyncio.run(send_commands())
