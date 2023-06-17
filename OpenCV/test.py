import cv2 as cv
import numpy as np
import sys
#img = np.zeros((720,1280,3), np.uint8)
img = cv.imread('Sunflower.jpg',0)
cv.imshow("Display window", img)
k = cv.waitKey(0)