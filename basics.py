import cv2
import numpy as np

#img=cv2.imread('image1.png',0)
#cv2.imshow('NATURE',img)
#cv2.imwrite('new image.png',img)

#cv2.waitKey(0)
a=np.array([1,1,3,4])
b=np.array([[1,2,3,4],[5,6,7,8]])
c=np.zeros((2,3))
d=np.ones((2,3))
e=np.random.rand(2,3)
g=np.arange(2,10,2)
h=np.put(a,[2],[50])
print(h)
print(g)
print(a)
print(b)
print(c)
print(d)
print(e)
f=np.insert(a,3,[5,6],axis=0)
print(f)

