from xml.dom.expatbuilder import theDOMImplementation
import cv2 as cv
from cv2 import rectangle
from cv2 import bitwise_or
import numpy as np

img = cv.imread('Images/cat1.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

cv.imshow('Blank Image', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, thickness=-1)
cv.imshow('Masked image', mask)

masked_image = cv.bitwise_and(img, img,mask = mask)
cv.imshow('Maked image',masked_image)


cv.waitKey(0)