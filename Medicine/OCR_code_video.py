# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 23:13:17 2020

@author: User
"""


import numpy as np
import cv2
import pytesseract
from east_detector import text_boundary,imcrop  #this is for getting the text box in image which coded manually
cap = cv2.VideoCapture(0)
alpha = 1.1 # Contrast control (1.3.0)
beta = 0 # Brightness control (0-100)


def unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    """Return a sharpened version of the image, using an unsharp mask."""
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened
def process(img):
    img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cv2.adaptiveThreshold(cv2.GaussianBlur(img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    cv2.adaptiveThreshold(cv2.medianBlur(img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    return img

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    med=''
    # Our operations on the frame come here
    adjusted = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    bound_box=text_boundary(adjusted)
    for b in bound_box:
        crop=imcrop(adjusted, b)
        sharpened_image = unsharp_mask(crop)
        pr=process(crop)
        gray = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2GRAY)
        ret,pr_b = cv2.threshold(pr,127,255,cv2.THRESH_BINARY)
        ret,thresh4 = cv2.threshold(pr,180,255,cv2.THRESH_TOZERO)
        ret,thresh3 = cv2.threshold(pr,180,255,cv2.THRESH_TRUNC)
        med=pytesseract.image_to_string(thresh3) #text for processing 1
        med+=pytesseract.image_to_string(gray)   #text for processing 1
        med+=pytesseract.image_to_string(thresh4) #text for processing 1
        med+=pytesseract.image_to_string(thresh3) #text for processing 1
    #gray = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2GRAY)
        if (med):
            # Fenat, Acetin-R, Ace, Onium.... are some test medicine
            if 'fenat' in med or 'Fenat' in med:
                print("fenat found")
                break
                print("Fenat found")
            if 'Doxy' in med or 'DOXY' in med:
                print("Doxycycline found")
                break
            if 'Aceptin-R' in med or 'Aceptin' in med:
                print("Aceptin-R found")
                break
            if 'Ace' in med:
                print("Ace found")
                break
            if 'Onium' in med or 'onium' in med:
                print("Onium found")
                break
            if 'Aeron' in med:
                print("Aeron found")
                break
            if 'Artigo' in med:
                print("Artigo found")
                break
            if 'M-kast' in med or 'Kast' in med:
                print("M_kast found")
                break
            if 'Metro' in med:
                print("Metro-400 found")
                break
            if 'Doxo' in med:
                print("Doxoven-200 found")
                break
            if 'Napa' in med:
                print("Napa found")
                break
            if 'Virdon' in med:
                print("Virdon found")
                break
        
        #print(med)
        else:
            #print("Show any english text..")
            pass
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()