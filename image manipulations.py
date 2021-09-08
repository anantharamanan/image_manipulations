import cv2
import numpy as np

img=cv2.imread('image1.png')
ima=cv2.imread('new image.png')
img1=cv2.resize(img,(100,200),interpolation=cv2.INTER_AREA)
cv2.imshow('nature',img1)
img2=cv2.rotate(img,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('nature',img2)
img3=img[10:100,10:150]
cv2.imshow('nature',img3)
And=cv2.bitwise_and(img,ima,mask=None)
img4=cv2.add(img,ima)#add the images
cv2.imshow('and operator',And)
Add=cv2.add(img,ima)
cv2.imshow('add',Add)
fl=cv2.flip(img,1)#if 0 flip vertically if >0 flip horizontally if <0 flip vertically and horizongtally
cv2.imshow('flip',fl)
scale=cv2.pyrDown(img)
cv2.imshow('scaling down',scale)
scale1=cv2.pyrUp(img)
cv2.imshow('scaling up',scale1)
Sub=cv2.subtract(img,ima)
cv2.imshow('subtract',Sub)
shape=img.shape
print(shape)
cv2.waitKey(0)