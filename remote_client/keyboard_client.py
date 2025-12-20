import asyncio
import json
import websockets
import pygame

PI_IP = "192.168.4.179"    # CHANGE THIS
PORT = 8765

SPEED_MIN = 20
SPEED_MAX = 90
SPEED_STEP = 5

SEND_RATE = 0.05  # 20 Hz


async def main():
    pygame.init()
    screen = pygame.display.set_mode((200, 200))
    pygame.display.set_caption("Winbot Keyboard Control")

    speed = 50  # default speed

    uri = f"ws://{PI_IP}:{PORT}"

    async with websockets.connect(uri) as ws:
        print("⌨️ Keyboard control connected")

        while True:
            linear = 0
            angular = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        speed = min(SPEED_MAX, speed + SPEED_STEP)
                        print(f"⬆ Speed: {speed}")

                    if event.key == pygame.K_y:
                        speed = max(SPEED_MIN, speed - SPEED_STEP)
                        print(f"⬇ Speed: {speed}")

            keys = pygame.key.get_pressed()

            # Movement
            if keys[pygame.K_w]:
                linear = 1.0
            elif keys[pygame.K_s]:
                linear = -1.0

            if keys[pygame.K_a]:
                angular = -1.0
            elif keys[pygame.K_d]:
                angular = 1.0

            msg = {
                "linear": linear,
                "angular": angular,
                "speed": speed
            }

            await ws.send(json.dumps(msg))
            await asyncio.sleep(SEND_RATE)


asyncio.run(main())
