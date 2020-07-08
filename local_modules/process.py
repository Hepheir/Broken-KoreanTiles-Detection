import numpy as np
import cv2

class Edge:
    def sobel(frame):
        sobelX = cv2.Sobel(frame, 3, 1, 0)
        sobelY = cv2.Sobel(frame, 3, 0, 1)
        sobel = cv2.add(sobelX, sobelY)
        frame = cv2.convertScaleAbs(sobel)
        return frame

    def canny(frame):
        frame = cv2.Canny(frame, 24, 128)
        return frame
