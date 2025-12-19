#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep


#left motor
ENABLE_LEFT=5
FORWARD_LEFT=7
BACKWARD_LEFT=8

#right motor
ENABLE_RIGHT=36
FORWARD_RIGHT=38
BACKWARD_RIGHT=37
MOTOR = [ENABLE_LEFT,FORWARD_LEFT,BACKWARD_LEFT,ENABLE_RIGHT,FORWARD_RIGHT,BACKWARD_RIGHT]


def motor_setup():    
    #GPIO Config
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    for val in MOTOR:
         GPIO.setup(val, GPIO.OUT)


def left_forward():
    GPIO.output(ENABLE_LEFT,1)
    GPIO.output(FORWARD_LEFT,1)
    GPIO.output(BACKWARD_LEFT,0)

def right_forward():
    GPIO.output(ENABLE_RIGHT,1)
    GPIO.output(FORWARD_RIGHT,1)
    GPIO.output(BACKWARD_RIGHT,0)

def left_backward():
    GPIO.output(ENABLE_LEFT,1)
    GPIO.output(FORWARD_LEFT,0)
    GPIO.output(BACKWARD_LEFT,1)

def right_backward():
    GPIO.output(ENABLE_RIGHT,1)
    GPIO.output(FORWARD_RIGHT,0)
    GPIO.output(BACKWARD_RIGHT,1)

def stop():
    GPIO.output(ENABLE_LEFT,0)
    GPIO.output(FORWARD_LEFT,0)
    GPIO.output(BACKWARD_LEFT,0)
    
    GPIO.output(ENABLE_RIGHT,0)
    GPIO.output(FORWARD_RIGHT,0)
    GPIO.output(BACKWARD_RIGHT,0)

def forward():
    left_forward()
    right_forward()

def backward():
    left_backward()
    right_backward()

def right():
    left_forward()
    right_backward()

def left():
    left_backward()
    right_forward()

    
def main():
    motor_setup()
    try:
        for i in range(4):
          forward()
          sleep(5)
          backward()
          sleep(5)
          right()
          sleep(5)
          left()
          sleep(5)
          stop()
          sleep(5)
    finally:
        GPIO.cleanup()

main()
#End
