import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('image1.png')
img1=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hist=cv.calcHist([img1],[0],None,[256],[0,256])
cv.imshow('new image',img1)
plt.plot(hist)
plt.show()
cv.waitKey(0)
