# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:19:23 2020

@author: User
"""


import cv2
import pytesseract
from east_detector import text_boundary,imcrop
img_cv = cv2.imread('croped monas.jpg')



alpha = 1.5 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)
# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# we need to convert from BGR to RGB format/mode:
adjusted = cv2.convertScaleAbs(img_cv, alpha=alpha, beta=beta)
bound_box=text_boundary(adjusted)
med=''
for b in bound_box:
        crop=imcrop(adjusted, b)
        med+=pytesseract.image_to_string(crop) #text for processing 1
if 'MONAS' in med:
    print("Monas 10")
else:
    print("Nothing")
