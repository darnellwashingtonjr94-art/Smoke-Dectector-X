# Smoke-Detector-X
Edge-AI smart home safety device combining traditional smoke detection with 360-degree YOLOv8 visual fire verification.

## Hardware Setup
1. Connect MQ-2 sensor's DOUT to GPIO 17.
2. Connect 5V Siren Relay to GPIO 27.
3. Plug in dual-fisheye 360 USB camera.

## Installation
```bash
pip install -r requirements.txt
python scripts/calibrate_camera.py  # Generate 360 dewarp matrices
sudo systemctl enable smoke-detector.service
