import asyncio
import json
import websockets
import pygame

PI_IP = "192.168.4.179"   # CHANGE THIS
PORT = 8765

DEADZONE = 0.15

SPEED_MIN = 20
SPEED_MAX = 90
SPEED_STEP = 5

SEND_RATE = 0.05  # seconds (20 Hz)


def dz(v):
    return 0 if abs(v) < DEADZONE else v


async def main():
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        print("❌ No Xbox controller found")
        return

    joy = pygame.joystick.Joystick(0)
    joy.init()
    print("🎮 Xbox controller connected")

    speed = 50  # default speed
    x_prev = 0
    y_prev = 0

    uri = f"ws://{PI_IP}:{PORT}"

    async with websockets.connect(uri) as ws:
        print("🔗 Connected to robot")

        while True:
            pygame.event.pump()

            # Direction (left stick)
            linear = -dz(joy.get_axis(1))   # forward/back
            angular = dz(joy.get_axis(0))   # left/right

            # Buttons
            x_btn = joy.get_button(2)  # X
            y_btn = joy.get_button(3)  # Y

            # Edge detection (press once)
            if x_btn and not x_prev:
                speed = min(SPEED_MAX, speed + SPEED_STEP)
                print(f"⬆ Speed: {speed}")

            if y_btn and not y_prev:
                speed = max(SPEED_MIN, speed - SPEED_STEP)
                print(f"⬇ Speed: {speed}")

            x_prev = x_btn
            y_prev = y_btn

            msg = {
                "linear": round(linear, 2),
                "angular": round(angular, 2),
                "speed": speed
            }

            await ws.send(json.dumps(msg))
            await asyncio.sleep(SEND_RATE)


asyncio.run(main())
