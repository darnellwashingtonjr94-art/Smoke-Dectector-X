import requests
import cv2
import base64
import json

class AlertDispatcher:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def send_alert(self, message, confidence, frame=None):
        payload = {
            "device_id": "Smoke-Detector-X-01",
            "alert_type": message,
            "confidence": confidence,
            "timestamp": requests.utils.default_timer()
        }

        if frame is not None:
            # Compress image to base64 for network transmission
            _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
            payload["image_data"] = base64.b64encode(buffer).decode('utf-8')

        try:
            response = requests.post(
                self.endpoint, 
                data=json.dumps(payload),
                headers={'Content-Type': 'application/json'},
                timeout=5
            )
            return response.status_code == 200
        except requests.exceptions.RequestException as e:
            print(f"Failed to dispatch alert: {e}")
            return False
