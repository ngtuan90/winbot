from gpiozero import Motor
from time import sleep

motor_left = Motor(forward=4 , backward =14)
motor_right = Motor(forward=17 , backward=18)

def forward():
    motor_left.forward
    motor_right.forward

def backward():
    motor_left.backward()
    motor_right.backward()

for i in range(4):
    forward()
    sleep(10)
    backward()
    sleep(10)
