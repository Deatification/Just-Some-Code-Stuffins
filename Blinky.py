#Makes an LED circuit hooked to the Pi blike really fast
import time
import RPi.GPIO as GPIO
while True:
#Makes an infinite loop
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
#Pin number 7 but GPIO pin number 4
    GPIO.output(4, True)
    time.sleep(.05)
    GPIO.output(4, False)
    time.sleep(.05)
