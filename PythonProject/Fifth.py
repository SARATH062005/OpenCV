import cv2 as cv
import numpy as np

img=cv.imread("Images/cat2.jpg")
cv.imshow("Original",img)

#Translate
def translate(img,x,y):
    transMat=np.float64([[1,0,x],[0,1,y]])
    dim=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dim)
translate=translate(img,100,50)
cv.imshow("translate",translate)

#rotate
def rotate(img,angle,rotpoint=None):
    (h,w)=img.shape[:2]
    if rotpoint is None:
        rotpoint=(w//2,h//2)

    rotMat=cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dim=(w,h)
    return cv.warpAffine(img,rotMat,dim)
rotate=rotate(img,45)
cv.imshow("rotate",rotate)

#flip
flip=cv.flip(img,1)
cv.imshow("flip",flip)

cv.waitKey(0)