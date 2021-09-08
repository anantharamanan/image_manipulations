import cv2 as cv


img=cv.imread('image1.png')
gray=cv.imread('image1.png',0)
ret,thresh=cv.threshold(gray,120,255,cv.THRESH_BINARY)
con,heirachy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img,con,-1,(255,0,0),5)
cnt=con[1]
area=cv.contourArea(cnt)
perimeter = cv.arcLength(cnt,True)
delta=0.1*perimeter
approx=cv.approxPolyDP(cnt,delta,True)
print(approx)
print(perimeter)
print(area)

cv.imshow('image',img)
cv.waitKey(0)