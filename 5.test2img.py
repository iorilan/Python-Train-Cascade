import numpy as np
import cv2
     
detected = cv2.CascadeClassifier('./data/cascade.xml')

img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

objs = detected.detectMultiScale(gray, 1.1,5,cv2.CASCADE_SCALE_IMAGE,(50,50),(100,100)) 
for (x,y,w,h) in objs: 
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2,8,0)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
cv2.waitKey(0)