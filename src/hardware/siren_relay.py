import RPi.GPIO as GPIO

class SirenRelay:
    def __init__(self, pin):
        self.pin = pin
        self.is_active = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def turn_on(self):
        if not self.is_active:
            GPIO.output(self.pin, GPIO.HIGH)
            self.is_active = True

    def turn_off(self):
        if self.is_active:
            GPIO.output(self.pin, GPIO.LOW)
            self.is_active = False

    def cleanup(self):
        GPIO.cleanup(self.pin)
