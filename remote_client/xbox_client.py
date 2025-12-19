import asyncio
import json
import websockets
import pygame

PI_IP = "192.168.4.179"   # change this
PORT = 8765
DEADZONE = 0.4

async def main():
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        print("No controller detected")
        return

    joy = pygame.joystick.Joystick(0)
    joy.init()
    print("Xbox controller connected")

    uri = f"ws://{PI_IP}:{PORT}"

    async with websockets.connect(uri) as ws:
        print("Connected to robot")

        last_cmd = None

        while True:
            pygame.event.pump()

            x = joy.get_axis(0)   # left stick X
            y = joy.get_axis(1)   # left stick Y

            if y < -DEADZONE:
                cmd = "forward"
            elif y > DEADZONE:
                cmd = "backward"
            elif x < -DEADZONE:
                cmd = "left"
            elif x > DEADZONE:
                cmd = "right"
            else:
                cmd = "stop"

            if cmd != last_cmd:
                await ws.send(json.dumps({"cmd": cmd}))
                last_cmd = cmd

            await asyncio.sleep(0.05)

asyncio.run(main())
