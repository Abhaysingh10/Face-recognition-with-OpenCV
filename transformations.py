s
import cv2 as cv
from cv2 import line
from cv2 import resize
from cv2 import imshow
import numpy as np
from cv2 import dilate
from cv2 import erode


img = cv.imread('Images/cat1.jpg')


cv.imshow('Output', img)


# Transformation
def transform(img, x, y):
    transMat = np.float32([[1,0,x], [1,0,y]] )
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)


# translated = cv.translate(img, -100)
# cv.imshow('Translated', translated)

def rotate(image, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)    
# Rotate
rotatedImage = rotate(img, -90)
# cv.imshow('Translated', rotatedImage)

# resizegit revert --no-commit <commit>
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Translated', resized)

# Flip
flipped = cv.flip(img, 0)
#cv.imshow('Translated', flipped)

# Cropping
croppeed = img[0:50, 100:200]
cv.imshow('output', croppeed)

cv.waitKey(0)