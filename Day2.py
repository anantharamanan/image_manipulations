import cv2 as cv
import numpy as np

img=cv.imread('image1.png',cv.IMREAD_GRAYSCALE)
ret,img1=cv.threshold(img,128,255,cv.THRESH_BINARY)
thresh1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 5, 2)#wecan use only binary and binary_inv
ret,thresh2=cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print(ret)#threshold value taken by otsu
cv.imshow('threshold',img1)
cv.imshow(' Adaptive threshold',thresh1)
cv.imshow('otsu thresholding',thresh2)
cv.waitKey(0)