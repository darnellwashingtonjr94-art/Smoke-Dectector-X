# Smoke-Detector-X

## 💻 Tech Stack

**Core Programming Languages, Core Systems**
*   ![Python](https://img.shields.io/badge/Python_3.x-3776AB?style=flat&logo=python&logoColor=white)
*
*   ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black) ![Systemd](https://img.shields.io/badge/Systemd-E34F26?style=flat)
*   
*   ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat&logo=gnu-bash&logoColor=white) 

**Platform Support & Hardware Architecture**
*   ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-C51A4A?style=flat&logo=raspberry-pi&logoColor=white)
*
*   ![NVIDIA Jetson](https://img.shields.io/badge/NVIDIA_Jetson-76B900?style=flat&logo=nvidia&logoColor=white) 
*   ![ARM64](https://img.shields.io/badge/ARM64-000000?style=flat&logo=arm&logoColor=white) ![AMD64](https://img.shields.io/badge/AMD64-000000?style=flat&logo=amd&logoColor=white) 
*   ![MQ-2 Sensor](https://img.shields.io/badge/Sensor-MQ--2-lightgray) ![5V Relay](https://img.shields.io/badge/Relay-5V-lightgray) ![360 Camera](https://img.shields.io/badge/Camera-Dual--Fisheye_360-lightgray) 
*   ![GPIO](https://img.shields.io/badge/Raspberry_Pi-GPIO-C51A4A?style=flat&logo=raspberry-pi&logoColor=white) 

**Low-Level Infrastructure & Performance**
*   ![TensorRT](https://img.shields.io/badge/TensorRT-76B900?style=flat&logo=nvidia&logoColor=white) 
*   ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white) 
*   ![MQTT](https://img.shields.io/badge/MQTT-660066?style=flat&logo=mqtt&logoColor=white) ![Webhooks](https://img.shields.io/badge/Webhooks-0073BB?style=flat&logo=webhooks&logoColor=white) 

**DevOps & Build Tools**
*   ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white) ![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=flat&logo=docker&logoColor=white) 
*   ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white) 

*   ![Makefile](https://img.shields.io/badge/Makefile-000000?style=flat&logo=gnu&logoColor=white) 
*   ![Unittest](https://img.shields.io/badge/Python-Unittest-3776AB?style=flat&logo=python&logoColor=white)
*    ![Mock](https://img.shields.io/badge/Python-Mock-3776AB?style=flat&logo=python&logoColor=white) 

**Artificial Intelligence & Quantum**
*   ![YOLOv8](https://img.shields.io/badge/YOLOv8-FF7F00?style=flat&logo=ultralytics&logoColor=white) 
*   ![Computer Vision](https://img.shields.io/badge/AI-Computer_Vision-8A2BE2?style=flat) 

Smoke-Detector-X is a privacy-first edge-AI safety device that upgrades traditional smoke alarms. Pairing an MQ-2 sensor with a 360-degree camera and onboard YOLOv8 machine learning, it visually verifies fire emergencies in real-time. It actively eliminates false alarms by locally confirming flames before triggering its siren and network alerts.

## BREAKING IT DOWN FOR THE PEOPLE IN THE BACK!!! LOL 
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
