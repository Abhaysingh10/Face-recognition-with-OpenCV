import cv2 as cv
from cv2 import merge
from cv2 import bilateralFilter
import numpy as np


img = cv.imread('Images/ball.jpg')
blank = np.zeros(img.shape[:2], dtype = 'uint8')
 

# Averaging
average = cv.blur(img, (7,7))
cv.imshow('Average', average)

# Gaussion blur
g_blur = cv.GaussianBlur(img ,(7,7), 0)
cv.imshow('Gaussian Blur', g_blur)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

#Bilateral
bilateral = cv.bilateralFilter(img,5, 15, 15)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)