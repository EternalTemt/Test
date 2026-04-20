import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 5, 25, 17, 27, 23, 22, 24]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(leds, 0)

num = 1

def dec2bin(value):
    return list(int(i) for i in bin(value)[2:].zfill(8))
sleep_time = 0.4
i = 0
while True:
    if num <= 128:
        while num > 1:
            num = int(num / 2)
            print(num, dec2bin(num))
            time.sleep(sleep_time)
            GPIO.output(leds, dec2bin(num))
            i += 1

    if num == 1:
        while num < 128:
            num = int(num * 2)
            print(num, dec2bin(num))
            time.sleep(sleep_time)
            GPIO.output(leds, dec2bin(num))
            i -= 1

