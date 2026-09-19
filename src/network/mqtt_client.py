import paho.mqtt.client as mqtt
import json

class MQTTDispatcher:
    def __init__(self, broker, port, topic):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client(client_id="SmokeDetectorX")
        self.client.on_connect = self._on_connect
        
    def _on_connect(self, client, userdata, flags, rc):
        print(f"Connected to MQTT Broker {self.broker} with result code {rc}")

    def connect(self):
        try:
            self.client.connect(self.broker, self.port, 60)
            self.client.loop_start()
        except Exception as e:
            print(f"MQTT Connection failed: {e}")

    def publish_alert(self, status, confidence=0):
        payload = {
            "device": "Smoke-Detector-X",
            "status": status,
            "confidence": round(confidence, 2)
        }
        self.client.publish(self.topic, json.dumps(payload), qos=1)
