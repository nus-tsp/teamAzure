__author__ = 'yananliu'

import cv2

image=cv2.imread('20131126215223234.jpg')
cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
#cascade=cv2.CascadeClassifier("haarcascade_eyes.xml")
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray=cv2.equalizeHist(gray)
faces=cascade.detectMultiScale(image,scaleFactor=1.05,minNeighbors=8,minSize=(4,4))

number_of_faces = len(faces)
strTotalNum = "Total number of people: %d" %(number_of_faces)
print strTotalNum

for x,y,width,height in faces:
    cv2.rectangle(image, (x,y), (x+width,y+height), (255,0,0),2)
    #cv2.circle(image, (x+width/2,y+height/2), 20,(0,255,255), 2)
    cv2.imshow('facedetect', image)
    cv2.imwrite('facedect.jpg',image)
cv2.waitKey(0)