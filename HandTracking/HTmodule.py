# start: aug 22

# packages
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math

# basic parameters
capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

# detects hands
detector = HandDetector(maxHands=2, detectionCon=0.8)
while True:

    success, image = capture.read()
    # Get Hands
    hands, img = detector.findHands(image)
    cv2.imshow('Video', image)
    cv2.waitKey(1)