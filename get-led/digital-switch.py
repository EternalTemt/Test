import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)

state = True
button = 13
period = 0.2
GPIO.setup(button, GPIO.IN)
while True:
    if GPIO.input(button):
        state = not state
        GPIO.output(led, state)    
        time.sleep(period)
        while GPIO.input(button):
            time.sleep(period)