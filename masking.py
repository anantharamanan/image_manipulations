import cv2 as cv
import numpy as np

cam=cv.VideoCapture(0)
while True:
    ret,img=cam.read()
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    lower_blue=np.array([90,50,50])
    upper_blue=np.array([155,255,255])
    mask=cv.inRange(hsv,lower_blue,upper_blue)
    res=cv.bitwise_and(img,img,mask=mask)
    if cv.waitKey(1)==ord('q'):
         cv.destroyAllWindows()
         break
    cv.imshow('result',res)
