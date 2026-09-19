# 🚨 Smoke-Detector-X

![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Supported-2496ED.svg?logo=docker&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Edge%20Hardware-C51A4A.svg?logo=raspberry-pi&logoColor=white)
![YOLOv8](https://img.shields.io/badge/AI-YOLOv8-FF7F00.svg?logo=ultralytics&logoColor=white)
![OpenCV](https://img.shields.io/badge/Vision-OpenCV-5C3EE8.svg?logo=opencv&logoColor=white)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/yourusername/smoke-detector-x/docker-publish.yml?logo=github&label=CI%2FCD%20Pipeline)

Edge-AI smart home safety device combining traditional smoke detection with 360-degree YOLOv8 visual fire verification[span_0](start_span)[span_0](end_span).

## 🧒 In 5th Grade English...
Imagine a regular smoke detector that beeps when you burn toast. That's annoying, right? This project fixes that! It is a super smart smoke detector with "eyes" (a 360-degree camera) and a "brain" (AI). 

When it smells smoke, it doesn't just beep right away. Instead, it quickly opens its eyes, looks around the whole room, and asks its brain, *"Do I see actual fire?"* 
*   If **YES**: It rings a loud siren and sends an alert to your phone. 
*   If **NO** (it's just steam or burnt toast): It stays quiet. 

## 📖 What is this about?
**Smoke-Detector-X** is an Edge-AI smart home safety device. It modernizes the traditional smoke alarm by combining a standard hardware smoke sensor (MQ-2) with advanced computer vision. Using a dual-fisheye 360-degree USB camera and an onboard YOLOv8 machine learning model, it visually verifies fire emergencies in real-time. 

## ⚙️ What this does?
This system actively monitors a room for fire hazards. When the hardware sensor detects smoke, the software wakes up the camera, flattens (dewarps) the 360-degree image so a computer can read it, and scans the image for visible flames. If it confirms a fire, it triggers a physical siren relay and dispatches network alerts (via MQTT or HTTP) to your smart home hub or phone. 

## 🧠 How does this work?
1.  **Smell (Hardware):** An MQ-2 gas/smoke sensor monitors the air.
2.  **Trigger (Interrupt):** When smoke goes above a safe level, it sends a signal to the main computer.
3.  **Look (Vision):** The 360-degree camera snaps a picture of the entire room.
4.  **Think (AI Inference):** A custom YOLOv8 model runs locally to detect the visual signature of flames.
5.  **Act (Alert):** If the AI sees fire with high confidence, it turns on a 5V siren and sends an emergency payload over Wi-Fi. 

## 🧊 Why is this cool?
*   **100% Local (Edge AI):** It processes everything locally without needing internet access to make a critical safety decision.
*   **Privacy-First:** Video feeds of your home are *never* sent to a cloud server. 
*   **Zero Blind Spots:** Using a 360-degree camera means one sensor can see an entire room.

## 🛠️ What problems this solves?
*   **False Alarms:** Eliminates the "boy who cried wolf" effect caused by burnt food, shower steam, or dust. 
*   **Delayed Responses:** Cross-verifying smoke with visual fire ensures that when the alarm rings, it is a genuine emergency requiring immediate action.
*   **Cloud Dependency:** Traditional smart cameras fail if your internet goes down. This system triggers the physical siren locally.

## 🚀 How to install this?

### 1. Hardware Setup
1.  Connect MQ-2 sensor's DOUT to GPIO 17[span_1](start_span)[span_1](end_span).
2.  Connect 5V Siren Relay to GPIO 27[span_2](start_span)[span_2](end_span).
3.  Plug in dual-fisheye 360 USB camera[span_3](start_span)[span_3](end_span).

### 2. Software Installation
Run the following commands to install dependencies, calibrate the camera, and start the system service[span_4](start_span)[span_4](end_span):
```bash
pip install -r requirements.txt
python scripts/calibrate_camera.py # Generate calibration matrices
sudo systemctl enable smoke-detector.service
sudo systemctl start smoke-detector.service
