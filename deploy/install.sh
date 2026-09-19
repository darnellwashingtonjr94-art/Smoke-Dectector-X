#!/bin/bash
# System provisioning script for Smoke-Detector-X

echo "Starting Smoke-Detector-X Provisioning..."

# Ensure system is up to date
sudo apt-get update && sudo apt-get upgrade -y

# Install prerequisites
sudo apt-get install -y python3-pip python3-dev libgl1-mesa-glx git v4l-utils

# Copy systemd service
sudo cp deploy/smoke-detector.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable smoke-detector.service

# Setup Python environment
pip3 install -r requirements.txt

echo "Installation complete. Please edit config.yaml with your network details."
echo "To start the service manually: sudo systemctl start smoke-detector.service"
