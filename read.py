import cv2 as cv

img = cv.imread('Images/cat.jpg')
cv.imshow('Cats', img)

cv.waitKey(0)

# # Reading Videos
# capture = cv.VideoCapture('Videos/cat.mp4')

capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()