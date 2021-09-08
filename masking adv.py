import cv2 as cv
import numpy as np

def nothing(x):
    pass
cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",700,800)

cv.createTrackbar("LowerHue","TrackBars",0,179,nothing)
cv.createTrackbar("LowerSaturation","TrackBars",0,255,nothing)
cv.createTrackbar("LowerValue","TrackBars",0,255,nothing)
cv.createTrackbar("UpperHue","TrackBars",179,179,nothing)
cv.createTrackbar("UpperSaturation","TrackBars",255,255,nothing)
cv.createTrackbar("UpperValue","TrackBars",255,255,nothing)
cam=cv.VideoCapture(0)
while True:
    ret,img=cam.read()
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    l_h = cv.getTrackbarPos("LowerHue","TrackBars")
    l_s = cv.getTrackbarPos("LowerSaturation","TrackBars")
    l_v = cv.getTrackbarPos("LowerValue","TrackBars")
    u_h = cv.getTrackbarPos("UpperHue","TrackBars")
    u_s = cv.getTrackbarPos("UpperSaturation","TrackBars")
    u_v = cv.getTrackbarPos("UpperValue","TrackBars")
    print(l_h,l_s,l_v,u_h,u_s,u_v)
    lower_blue=np.array([l_h,l_s,l_v])
    upper_blue=np.array([u_h,u_s,u_v])
    mask=cv.inRange(hsv,lower_blue,upper_blue)
    res=cv.bitwise_and(img,img,mask=mask)
    cv.imshow('input',img)
    cv.imshow('result',res)
    if cv.waitKey(1)==ord('q'):
         break

cv.destroyAllWindows()
cam.release()