import time
import cv2

class CameraInterface:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise Exception("Could not open the camera.")
        time.sleep(1)

    def capture_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Failed to grab frame.")
        return frame

    def release(self):
        self.cap.release

    