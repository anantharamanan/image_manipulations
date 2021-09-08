import cv2 as cv
import numpy as np
img=cv.imread('image1.png')
cam=cv.Canny(img,120,255)
cv.imshow('canny',cam)
cv.waitKey(0)

