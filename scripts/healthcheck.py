import sys
import os
import cv2

def check_hardware():
    """
    Docker healthcheck script to verify camera is accessible.
    """
    video_device = os.getenv("CAMERA_SOURCE", "/dev/video0")
    
    if not os.path.exists(video_device):
        print(f"Healthcheck failed: Camera {video_device} not found.")
        sys.exit(1)
        
    # Quick probe of the video interface
    cap = cv2.VideoCapture(int(video_device.replace('/dev/video', '')))
    if not cap.isOpened():
        print("Healthcheck failed: Cannot open video stream.")
        sys.exit(1)
        
    cap.release()
    print("Healthcheck passed: Hardware accessible.")
    sys.exit(0)

if __name__ == "__main__":
    check_hardware()
