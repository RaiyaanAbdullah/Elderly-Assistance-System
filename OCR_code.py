# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:19:23 2020

@author: User
"""


import cv2
import pytesseract
img_cv = cv2.imread('new.jpg')

alpha = 1.5 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)
# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# we need to convert from BGR to RGB format/mode:

adjusted = cv2.convertScaleAbs(img_cv, alpha=alpha, beta=beta)
gray = cv2.cvtColor(adjusted, cv2.COLOR_BGR2GRAY)
print(pytesseract.image_to_string(gray))
# OR
'''img_rgb = Image.frombytes('RGB', img_cv.shape[:2], img_cv, 'raw', 'BGR', 0, 0)
print(pytesseract.image_to_string(img_rgb))'''