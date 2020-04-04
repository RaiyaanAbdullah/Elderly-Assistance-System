# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:00:22 2020

@author: User
"""


import cv2

image = cv2.imread('napa.jpg')

alpha = 1.5 # Contrast control (1.0-3.0)
beta = 0 # Brightness control (0-100)

adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
gray = cv2.cvtColor(adjusted, cv2.COLOR_BGR2GRAY)
cv2.imshow('original', image)
cv2.imshow('adjusted', adjusted)
cv2.imshow('gray', gray)
cv2.waitKey()