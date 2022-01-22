import cv2 as cv
from cv2 import Sobel
import numpy as np

img = cv.imread('Images/wall.jpg')
cv.imshow('Main', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Lacplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# sobel
Sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
Sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined = cv.bitwise_and(Sobelx, Sobely)
cv.imshow('SobelX', Sobelx)
cv.imshow('SobelY', Sobely)
cv.imshow('Combined', combined)

#canny
canny = cv.Canny(gray, 150,175)
cv.imshow('Canny', canny)







cv.waitKey(0)