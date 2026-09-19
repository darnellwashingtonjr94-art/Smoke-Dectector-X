import unittest
from unittest.mock import patch, MagicMock
import sys

# Mock RPi.GPIO to allow testing on non-Raspberry Pi devices
sys.modules['RPi'] = MagicMock()
sys.modules['RPi.GPIO'] = MagicMock()

from src.hardware.siren_relay import SirenRelay
from src.hardware.mq2_sensor import MQ2Sensor

class TestHardwareLogic(unittest.TestCase):
    
    @patch('RPi.GPIO.output')
    def test_siren_activation(self, mock_output):
        siren = SirenRelay(pin=27)
        self.assertFalse(siren.is_active)
        
        siren.turn_on()
        self.assertTrue(siren.is_active)
        mock_output.assert_called_with(27, sys.modules['RPi.GPIO'].HIGH)
        
    @patch('RPi.GPIO.input')
    def test_smoke_detection(self, mock_input):
        mock_input.return_value = sys.modules['RPi.GPIO'].HIGH
        sensor = MQ2Sensor(pin=17)
        self.assertTrue(sensor.detect_smoke())

if __name__ == '__main__':
    unittest.main()
