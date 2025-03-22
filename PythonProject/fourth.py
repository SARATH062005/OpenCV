import cv2 as cv

img=cv.imread("Images/cat.jpg")
cv.imshow("Original",img)
#gray color
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#blur
blur=cv.blur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

#Edge cascading
canny=cv.Canny(img,125,175)
cv.imshow("Canny",canny)

#Dilating
dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow("dilated",dilated)

#Eroding
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow("eroded",eroded)

#Resize
resize=cv.resize(img,(600,400),interpolation=cv.INTER_CUBIC)
cv.imshow("resize",resize)

#cropped
crop=img[100:200,300:450]
cv.imshow("cropped",crop)



cv.waitKey(0)

