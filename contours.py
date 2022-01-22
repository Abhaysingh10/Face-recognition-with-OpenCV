
import cv2 as cv
from cv2 import Canny
import numpy as np


img = cv.imread('Images/cat1.jpg')
blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', blank)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Output', gray)

canny = cv.Canny(img, 125, 175)
# cv.imshow('Output', canny)


ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, heirarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

contourDrawn = cv.drawContours(blank, contours, -1, (0,0,255), thickness=2)
cv.imshow('Counter Drawn', contourDrawn)


cv.waitKey(0)