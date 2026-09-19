import unittest
import numpy as np
from unittest.mock import patch, MagicMock

# Mock ultralytics YOLO to avoid downloading weights during unit tests
class MockBox:
    def __init__(self, cls, conf, xyxy):
        self.cls = [cls]
        self.conf = [conf]
        self.xyxy = [xyxy]

class MockResult:
    def __init__(self, boxes):
        self.boxes = boxes

class MockYOLO:
    def __init__(self, path):
        pass
    def __call__(self, frame, verbose):
        # Simulate detecting a fire with 85% confidence
        box1 = MockBox(cls=0, conf=0.85, xyxy=[100, 100, 200, 200])
        return [MockResult(boxes=[box1])]

import sys
sys.modules['ultralytics'] = MagicMock()
sys.modules['ultralytics.YOLO'] = MockYOLO

from src.ai.fire_inference import FireDetector

class TestAIInference(unittest.TestCase):
    def test_fire_detection(self):
        detector = FireDetector(model_path="dummy.pt", confidence_threshold=0.6)
        dummy_frame = np.zeros((640, 640, 3), dtype=np.uint8)
        
        is_fire, conf, bbox = detector.detect(dummy_frame)
        
        self.assertTrue(is_fire)
        self.assertEqual(conf, 0.85)
        self.assertEqual(bbox, [100, 100, 200, 200])

if __name__ == '__main__':
    unittest.main()
