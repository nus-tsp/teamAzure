__author__ = 'yananliu'

import cv2.cv as cv

image = cv.LoadImage("20131126215223234.jpg")
image_size = cv.GetSize(image)
grayscale = cv.CreateImage(image_size, 8, 1)
cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)
storage = cv.CreateMemStorage(0)
cv.EqualizeHist(grayscale, grayscale)

cascade=cv.Load("haarcascade_frontalface_alt.xml")
#cascade=cv.Load("haarcascade_eyes.xml")
faces = cv.HaarDetectObjects(grayscale, cascade, storage, 1.08, 5, cv.CV_HAAR_DO_CANNY_PRUNING,(12,12))

number_of_faces = len(faces)
strTotalNum = "Total number of people: %d" %(number_of_faces)
print strTotalNum

if faces:
    for num in faces:
        i,j,width,height=num[0]
        cv.Rectangle(image,(i,j), (i + width, j + height),cv.CV_RGB(0, 255, 0), 1, 8, 0)


cv.NamedWindow ('camera', cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('camera', image)
cv.SaveImage('new_im.jpg', image)
cv.WaitKey(0)
cv.destroyWindow("camera")