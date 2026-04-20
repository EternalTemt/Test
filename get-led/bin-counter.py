import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 5, 25, 17, 27, 23, 22, 24]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(leds, 0)

up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
num = 120

def dec2bin(value):
    return list(int(i) for i in bin(value)[2:].zfill(8))
sleep_time = 0.2

while True:
    if GPIO.input(up):
        if num > 127:
            num = 255
        else: num += 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(down):
        if num > 128:
            num == 128
        if num < 0:
            num = 0
        else: num -= 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)

    GPIO.output(leds, dec2bin(num))