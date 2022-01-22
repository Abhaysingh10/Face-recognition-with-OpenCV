import cv2 as cv
from cv2 import rectangle
from cv2 import bitwise_or
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1 )

circle = cv.circle(blank.copy(), (200,200), 200 , 255, -1 )

cv.imshow('Rectangle', rectangle);
cv.imshow('Cirlcle', circle)

# biwise and
bitwise_and = cv.bitwise_and(rectangle, circle )
cv.imshow('Bitwise and', bitwise_and)

# biwise and
bitwise_or = cv.bitwise_or(rectangle, circle )
cv.imshow('Bitwise or', bitwise_or)

# bitwise xor
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

#bitwise not

bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise not', bitwise_not)

cv.waitKey(0)