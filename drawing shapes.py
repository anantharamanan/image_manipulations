import cv2 as cv
import numpy as np

img=cv.imread('image1.png')
print(img.shape)
cv.circle(img,(95,120),25,(0,255,0),-1)
cv.rectangle(img,(0,100),(100,184),(255,0,0),10)

pts=np.array(([10,20],[20,50],[5,10],[10,15]),np.int32)
cv.polylines(img,[pts],True,(255,0,255))
cv.imshow('image',img)
cv.waitKey(0)