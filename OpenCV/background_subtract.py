import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

i = 0
x = [0]
y = [0]

backSub = cv.createBackgroundSubtractorMOG2()
#backSub = cv.createBackgroundSubtractorKNN()

# Open up the video
capture = cv.VideoCapture(0)
if not capture.isOpened():
    print('Unable to open.')
    exit(0)

# create a variable for frame subtraction
prev_frame = np.zeros((640, 480))

while True:
    # Read a frame from video
    ret, frame = capture.read()
    if frame is None:
        break
    # Convert video to grayscale, apply bluring
    (rows,cols,_) = frame.shape
    frame_rz = cv.resize(cv.cvtColor(frame, cv.COLOR_BGR2GRAY), (480, 640))
    frame_blur = cv.GaussianBlur(frame_rz, (1, 1), 0)
    
    # Use background subtractor to get the forground
    fgMask = backSub.apply(frame_blur)
    
    # Use simple frame subtraction to get forground
    prev_frame = frame_blur
    # Show result    
    cv.imshow('Frame', frame_rz)
    cv.imshow('FG Mask', fgMask)

    x.append(x[-1]+1)
    y.append(np.sum(fgMask))

    if np.sum(fgMask) > 250000 and i>=30:
        print("movement!!!" + str(np.sum(fgMask)))
        i = 0
    
    i += 1

    keyboard = cv.waitKey(30)
    if keyboard == 27:
        plt.plot(x,y,color='b',label='hi')
        plt.show()
        break