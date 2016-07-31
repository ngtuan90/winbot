from gpiozero import Motor
from time import sleep
import Rpi.GPIO as GPIO
motor = Motor(forward=26, backward=20)

counter = 0

try:
        while counter < 10:
                motor.forward()
                sleep(5)
                motor.backward()
                sleep(5)
                counter +=1

finally:
        GPIO.cleanup()
