import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Images/cat1.jpg')
# cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale',  gray)

#Grayscale histogram
# gray_histo = cv.calcHist([gray], [0], None, [256],[0,256] )
# plt.figure()
# plt.title('Gray')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_histo)
# plt.xlim([0,256])
# plt.show()

# Color histogram
plt.figure()
plt.title('Color Histo')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color= col)
    plt.xlim([0,256])
    
plt.show()





cv.waitKey(0)