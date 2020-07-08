import numpy as np
import cv2

from local_modules.process import *

g_input_image_path = './res/tmp/input.jpg'
g_output_image_path = './res/tmp/output.jpg'
g_frame = None

def load():
    global g_frame
    g_frame = cv2.imread(g_input_image_path)

def process():
    global g_frame

    frame = cv2.cvtColor(g_frame, cv2.COLOR_BGR2HSV)
    frame = frame[:,:,0] # HSV
    ddepth = 5
    sobelX = cv2.Sobel(frame, ddepth, 1, 0)
    sobelY = cv2.Sobel(frame, ddepth, 0, 1)
    sobel = cv2.add(sobelX, sobelY)

    g_frame = cv2.convertScaleAbs(sobel)

def save():
    global g_frame
    cv2.imwrite(g_output_image_path, g_frame)


print('Load Image')
load()
print('Start Process')
process()
print('Save Image')
save()
print('Done')