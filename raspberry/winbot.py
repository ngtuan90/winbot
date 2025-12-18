#!/usr/bin/python

import RPi.GPIO as GPIO

#left motor
ENABLE_LEFT=13
FORWARD_LEFT=15
BACKWARD_LEFT=16

#right motor
ENABLE_RIGHT=36
FORWARD_RIGHT=38
BACKWARD_RIGHT=37
MOTOR = [ENABLE_LEFT,FORWARD_LEFT,BACKWARD_LEFT,ENABLE_RIGHT,FORWARD_RIGHT,BACKWARD_RIGHT]

class Winbot:
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

    def forward(self):
        self.left_forward()
        self.right_forward()

    def backward(self):
        self.left_backward()
        self.right_backward()

    def right(self):
        self.left_forward()
        self.right_backward()

    def left(self):
        self.left_backward()
        self.right_forward()

    def __init__(self):
        self.motor_setup()

