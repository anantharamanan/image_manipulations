import cv2 as cv
import numpy as np

img=cv.imread('image1.png')
fi=cv.blur(img,(5,5))#cv.blur(src,filter size)
cv.imshow('blurring',fi)
gfi=cv.GaussianBlur(img,(5,5),0)#random noise
cv.imshow('gaussian blur',gfi)
me=cv.medianBlur(img,5)#salt and pepper noise
cv.imshow('median',me)
bi=cv.bilateralFilter(img, 9 , 75, 75)#src,ksize,color_space,sigma_space
cv.imshow('bilateral',bi)
cv.waitKey(0)
