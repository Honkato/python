import RPi.GPIO as GPIO
import time
class brila():
    def __init__(self):
        self.LED_PIN_RED = 26
        self.LED_PIN_GREEN = 16
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED_PIN_RED, GPIO.OUT)
        GPIO.setup(self.LED_PIN_GREEN, GPIO.OUT)
    def onGreen(self):
        GPIO.output(self.LED_PIN_GREEN, GPIO.HIGH)
    def onRed(self):
        GPIO.output(self.LED_PIN_RED, GPIO.HIGH)
    def offRed(self):
        GPIO.output(self.LED_PIN_RED, GPIO.LOW)
    def offGreen(self):
        GPIO.output(self.LED_PIN_GREEN, GPIO.LOW)
    def finish(self):
        GPIO.cleanup()
