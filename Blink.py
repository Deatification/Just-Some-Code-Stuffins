#Blink.py
import time
import RPi.GPIO as GPIO
while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.output(4, True)
    time.sleep(.05)
    GPIO.output(4, False)
    time.sleep(.05)
