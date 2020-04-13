import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

interval = .25

while(True):
    print("LED On")
    GPIO.output(18, GPIO.HIGH)
    time.sleep(interval)

    print("LED Off")
    GPIO.output(18, GPIO.LOW)
    time.sleep(interval)
