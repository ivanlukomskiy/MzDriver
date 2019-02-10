# This gives us control of the Raspberry Pi's pins.
# This is only used for time delays... standard Python stuff.

import RPi.GPIO as GPIO

pin_number = 35
frequency_hertz = 50
left_position = 0.40
right_position = 2.5
ms_per_cycle = 1000 / frequency_hertz


class ServoControl:

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.pwm = GPIO.PWM(pin_number, frequency_hertz)
        GPIO.setup(pin_number, GPIO.OUT)

    def set(self, value):
        position = left_position + (right_position - left_position) * (value + 100) / 200
        self.pwm.start(position / ms_per_cycle)

    def shutdown(self):
        self.pwm.stop()
        GPIO.cleanup()


SERVO_CONTROL = ServoControl()
