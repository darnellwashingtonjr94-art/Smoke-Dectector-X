# “Smoke-Detector-X”

## 💻 Tech Stack

**Core Programming Languages, Core Systems**
*   ![Python](https://img.shields.io/badge/Python_3.x-3776AB?style=flat&logo=python&logoColor=white) Primary application logic and inference scripts[span_0](start_span)[span_0](end_span).
*   ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black) ![Systemd](https://img.shields.io/badge/Systemd-E34F26?style=flat) Background service management and deployment execution[span_1](start_span)[span_1](end_span)[span_2](start_span)[span_2](end_span).
*   ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat&logo=gnu-bash&logoColor=white) Shell scripting for installation (`install.sh`) and deployment (`docker_publish.sh`)[span_3](start_span)[span_3](end_span).

**Platform Support & Hardware Architecture**
*   ![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-C51A4A?style=flat&logo=raspberry-pi&logoColor=white) ![NVIDIA Jetson](https://img.shields.io/badge/NVIDIA_Jetson-76B900?style=flat&logo=nvidia&logoColor=white) Target edge hardware platforms[span_4](start_span)[span_4](end_span).
*   ![ARM64](https://img.shields.io/badge/ARM64-000000?style=flat&logo=arm&logoColor=white) ![AMD64](https://img.shields.io/badge/AMD64-000000?style=flat&logo=amd&logoColor=white) Supported multi-architecture builds[span_5](start_span)[span_5](end_span).
*   ![MQ-2 Sensor](https://img.shields.io/badge/Sensor-MQ--2-lightgray) ![5V Relay](https://img.shields.io/badge/Relay-5V-lightgray) ![360 Camera](https://img.shields.io/badge/Camera-Dual--Fisheye_360-lightgray) Hardware components for triggers and vision[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span).
*   ![GPIO](https://img.shields.io/badge/Raspberry_Pi-GPIO-C51A4A?style=flat&logo=raspberry-pi&logoColor=white) Direct hardware interfacing for triggers and alerts[span_8](start_span)[span_8](end_span).

**Low-Level Infrastructure & Performance**
*   ![TensorRT](https://img.shields.io/badge/TensorRT-76B900?style=flat&logo=nvidia&logoColor=white) Used for generating high-speed edge inference engines with FP16 precision[span_9](start_span)[span_9](end_span).
*   ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white) Hardware-accelerated video capture and image dewarping[span_10](start_span)[span_10](end_span).
*   ![MQTT](https://img.shields.io/badge/MQTT-660066?style=flat&logo=mqtt&logoColor=white) ![Webhooks](https://img.shields.io/badge/Webhooks-0073BB?style=flat&logo=webhooks&logoColor=white) Lightweight local network payload dispatching[span_11](start_span)[span_11](end_span).

**Cybersecurity & Offensive Auditing**
*   *N/A - This project is designed as a privacy-first, 100% local edge-AI device without external attack surfaces[span_12](start_span)[span_12](end_span).*

**DevOps & Build Tools**
*   ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white) ![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=flat&logo=docker&logoColor=white) Containerization and local network access mapping[span_13](start_span)[span_13](end_span).
*   ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white) CI/CD pipelines for automated Python package and Docker image publishing (`docker-publish.yml`, `python-publish.yml`)[span_14](start_span)[span_14](end_span).
*   ![Makefile](https://img.shields.io/badge/Makefile-000000?style=flat&logo=gnu&logoColor=white) Streamlined build, test, run, and clean commands[span_15](start_span)[span_15](end_span).
*   ![Unittest](https://img.shields.io/badge/Python-Unittest-3776AB?style=flat&logo=python&logoColor=white) ![Mock](https://img.shields.io/badge/Python-Mock-3776AB?style=flat&logo=python&logoColor=white) Automated testing for hardware, network, and inference modules[span_16](start_span)[span_16](end_span).

**Artificial Intelligence & Quantum**
*   ![YOLOv8](https://img.shields.io/badge/YOLOv8-FF7F00?style=flat&logo=ultralytics&logoColor=white) Custom-trained object detection model for visual fire verification[span_17](start_span)[span_17](end_span)[span_18](start_span)[span_18](end_span).
*   ![Computer Vision](https://img.shields.io/badge/AI-Computer_Vision-8A2BE2?style=flat) Real-time 360-degree frame processing and confidence thresholding[span_19](start_span)[span_19](end_span).

**Cloud Providers**
*   *N/A - Operates entirely on the edge. Dispatches alerts directly to local network endpoints (e.g., local Home Assistant) without relying on cloud providers[span_20](start_span)[span_20](end_span).*

![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Supported-2496ED.svg?logo=docker&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Edge%20Hardware-C51A4A.svg?logo=raspberry-pi&logoColor=white)
![YOLOv8](https://img.shields.io/badge/AI-YOLOv8-FF7F00.svg?logo=ultralytics&logoColor=white)
![OpenCV](https://img.shields.io/badge/Vision-OpenCV-5C3EE8.svg?logo=opencv&logoColor=white)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/darnellwashingtonjr94-art/smoke-detector-x/docker-publish.yml?logo=github&label=CI%2FCD%20Pipeline)

Edge-AI smart home safety device combining traditional smoke detection with 360-degree YOLOv8 visual fire verification[span_0](start_span)[span_0](end_span).

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
