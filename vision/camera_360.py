import cv2

class Camera360:
    def __init__(self, source=0):
        self.source = source
        self.cap = cv2.VideoCapture(self.source)
        # Set to highest supported resolution for dual fisheye
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    def get_frame(self):
        if not self.cap.isOpened():
            self.cap.open(self.source)
        
        ret, frame = self.cap.read()
        if ret:
            return frame
        return None

    def release(self):
        self.cap.release()
