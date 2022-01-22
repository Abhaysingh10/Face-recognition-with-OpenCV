from pyexpat import features
import cv2 as cv
import numpy as np


haar_cascade = cv.CascadeClassifier('haar_face.xml')
people = ['Henry Cavil', 'Jennifer Lawrence', 'RDJ', 'Tom Holland', 'Zendaya']


# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yaml')

img = cv.imread(r'D:\Opencvseries\opencvseries\Faces\Henry Cavil\henry19.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('output', gray)



face_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)
for (x,y,w,h) in face_rect:
    faces_roi = gray[y:y+h, x: x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20) ,cv.FONT_HERSHEY_COMPLEX, 1.0, color=(0,255,0), thickness=2 )
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2  )

cv.imshow('Detected Face', img)


cv.waitKey(0)