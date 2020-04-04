# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:19:23 2020

@author: User
"""


import cv2
import pytesseract
img = cv2.imread('new.jpg')


# resize image
width = 1000
scale = img.shape[1] / width
height = int(img.shape[0] / scale) # keep original height
dim = (width, height)
 img = cv2.resize(img, dim)



alpha = 1.5 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)
# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# we need to convert from BGR to RGB format/mode:



adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
gray = cv2.cvtColor(adjusted, cv2.COLOR_BGR2GRAY)

print(pytesseract.image_to_string(gray))

cv2.imshow("Output image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
# OR
'''img_rgb = Image.frombytes('RGB', img_cv.shape[:2], img_cv, 'raw', 'BGR', 0, 0)
print(pytesseract.image_to_string(img_rgb))'''