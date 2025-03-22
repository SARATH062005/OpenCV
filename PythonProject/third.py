import cv2 as cv
import numpy as np
#rectangle
blank=np.zeros((500,500,3),dtype='uint8')
cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=2)
cv.imshow("rectngle",blank)

#circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)
cv.imshow("circle",blank)

#text
cv.putText(blank,"Hello",(255,255),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
cv.imshow("Text",blank)


cv.waitKey(0)
