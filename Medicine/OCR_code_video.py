# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 23:13:17 2020

@author: User
"""


import numpy as np
import cv2
import pytesseract
cap = cv2.VideoCapture(0)
alpha = 1.5 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    adjusted = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    gray = cv2.cvtColor(adjusted, cv2.COLOR_BGR2GRAY)
    if (pytesseract.image_to_string(gray)):
        print(pytesseract.image_to_string(gray))
    else:
        print("Show any english text..")
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()