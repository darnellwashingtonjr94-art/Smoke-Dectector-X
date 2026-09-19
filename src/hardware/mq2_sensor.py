import RPi.GPIO as GPIO

class MQ2Sensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def detect_smoke(self):
        # MQ2 digital output goes HIGH when gas/smoke threshold is crossed
        return GPIO.input(self.pin) == GPIO.HIGH

    def cleanup(self):
        GPIO.cleanup(self.pin)
