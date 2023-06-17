from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import matplotlib.pyplot as plt

x = [0]
y = [0]

# build command line UI
parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='vtest.mp4')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
parser.add_argument('--blur', type=int, help='Apply bluring to source', default=1)
args = parser.parse_args()

# Pick a Background subtractor
if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()
# elif args.algo == 'KNN':
else:
    backSub = cv.createBackgroundSubtractorKNN()

# Open up the video
capture = cv.VideoCapture(0)
if not capture.isOpened():
    print('Unable to open: ' + args.input)
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
    frame_blur = cv.GaussianBlur(frame_rz, (args.blur, args.blur), 0)
    
    # Use background subtractor to get the forground
    fgMask = backSub.apply(frame_blur)
    
    # Use simple frame subtraction to get forground
    prev_frame = frame_blur
    # Show result    
    cv.imshow('Frame', frame_rz)
    cv.imshow('FG Mask', fgMask)

    x.append(x[-1]+1)
    y.append(np.sum(fgMask))

    if np.sum(fgMask) > 250000:
        print("movement!!!" + str(np.sum(fgMask)))
    # if i>200:
    #     cv.imwrite(f"subtract_src{i}.png", fg)
    
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        plt.plot(x,y,color='b',label='hi')
        plt.show()
        break