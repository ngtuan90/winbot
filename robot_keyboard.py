#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
import curses

#left motor
ENABLE_LEFT=5
FORWARD_LEFT=7
BACKWARD_LEFT=8

#right motor
ENABLE_RIGHT=36
FORWARD_RIGHT=38
BACKWARD_RIGHT=37
MOTOR = [ENABLE_LEFT,FORWARD_LEFT,BACKWARD_LEFT,ENABLE_RIGHT,FORWARD_RIGHT,BACKWARD_RIGHT]


 
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

actions = {
    curses.KEY_UP: forward,
    curses.KEY_DOWN: backward,
    curses.KEY_LEFT: left,
    curses.KEY_RIGHT: right,
    }

def quit():
    curses.endwin()

def main(window):
    next_key = None
    
    window.clear()
    window.addstr("Winbot Keyboard Control")
    try:
      while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            #KEY DOWN
            curses.halfdelay(3)
            action = actions.get(key)
            
            window.addstr("¬n")
            window.addstr(action.__name__)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            #KEY UP
            stop()
        
    finally:
        GPIO.cleanup()

curses.wrapper(main)
#End
