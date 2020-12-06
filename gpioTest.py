#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
pinNum = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinNum, GPIO.OUT)
for i in range(15):
    GPIO.output(pinNum, True)
    time.sleep(0.1)
    GPIO.output(pinNum, False)
    time.sleep(0.1)

GPIO.cleanup()