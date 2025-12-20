#!/usr/bin/python

import RPi.GPIO as GPIO

# ======================
# PIN DEFINITIONS (BOARD)
# ======================

# Left motor
ENABLE_LEFT = 13
FORWARD_LEFT = 18
BACKWARD_LEFT = 16

# Right motor
ENABLE_RIGHT = 36
FORWARD_RIGHT = 38
BACKWARD_RIGHT = 37

MOTOR = [
    ENABLE_LEFT, FORWARD_LEFT, BACKWARD_LEFT,
    ENABLE_RIGHT, FORWARD_RIGHT, BACKWARD_RIGHT
]

PWM_FREQ = 100  # Hz


class Winbot:

    def motor_setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        for pin in MOTOR:
            GPIO.setup(pin, GPIO.OUT)

        # Setup PWM on enable pins
        self.pwm_left = GPIO.PWM(ENABLE_LEFT, PWM_FREQ)
        self.pwm_right = GPIO.PWM(ENABLE_RIGHT, PWM_FREQ)

        self.pwm_left.start(0)
        self.pwm_right.start(0)

    # ======================
    # LOW LEVEL MOTOR CONTROL
    # ======================

    def _left_motor(self, direction, speed):
        if direction == "forward":
            GPIO.output(FORWARD_LEFT, 1)
            GPIO.output(BACKWARD_LEFT, 0)
        elif direction == "backward":
            GPIO.output(FORWARD_LEFT, 0)
            GPIO.output(BACKWARD_LEFT, 1)
        else:  # stop
            GPIO.output(FORWARD_LEFT, 0)
            GPIO.output(BACKWARD_LEFT, 0)
            speed = 0

        self.pwm_left.ChangeDutyCycle(speed)

    def _right_motor(self, direction, speed):
        if direction == "forward":
            GPIO.output(FORWARD_RIGHT, 1)
            GPIO.output(BACKWARD_RIGHT, 0)
        elif direction == "backward":
            GPIO.output(FORWARD_RIGHT, 0)
            GPIO.output(BACKWARD_RIGHT, 1)
        else:  # stop
            GPIO.output(FORWARD_RIGHT, 0)
            GPIO.output(BACKWARD_RIGHT, 0)
            speed = 0

        self.pwm_right.ChangeDutyCycle(speed)

    # ======================
    # SIMPLE MOVEMENTS
    # ======================

    def forward(self, speed=60):
        self._left_motor("forward", speed)
        self._right_motor("forward", speed)

    def backward(self, speed=60):
        self._left_motor("backward", speed)
        self._right_motor("backward", speed)

    def left(self, speed=60):
        self._left_motor("backward", speed)
        self._right_motor("forward", speed)

    def right(self, speed=60):
        self._left_motor("forward", speed)
        self._right_motor("backward", speed)

    def stop(self):
        self._left_motor("stop", 0)
        self._right_motor("stop", 0)

    # ======================
    # DIFFERENTIAL DRIVE
    # ======================

    def drive(self, linear, angular, max_speed=80):
        """
        linear  : -1.0 (backward) to +1.0 (forward)
        angular : -1.0 (left) to +1.0 (right)
        """

        left = linear + angular
        right = linear - angular

        # Clamp values
        left = max(-1.0, min(1.0, left))
        right = max(-1.0, min(1.0, right))

        left_speed = int(abs(left) * max_speed)
        right_speed = int(abs(right) * max_speed)

        if left > 0:
            self._left_motor("forward", left_speed)
        elif left < 0:
            self._left_motor("backward", left_speed)
        else:
            self._left_motor("stop", 0)

        if right > 0:
            self._right_motor("forward", right_speed)
        elif right < 0:
            self._right_motor("backward", right_speed)
        else:
            self._right_motor("stop", 0)

    # ======================
    # CLEANUP
    # ======================

    def cleanup(self):
        self.stop()
        self.pwm_left.stop()
        self.pwm_right.stop()
        GPIO.cleanup()

    def __init__(self):
        self.motor_setup()
