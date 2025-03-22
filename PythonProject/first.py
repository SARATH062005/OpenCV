import cv2 as cv
#
# img=cv.imread('Images/cat.jpg')
# cv.imshow('Cat',img)
# cv.waitKey(0)
#
cap=cv.VideoCapture('Videos/cat.mp4')

while True:
    istrue , frame = cap.read()
    cv.imshow("videos",frame)
    if cv.waitKey(20) & 0xFF==ord('c'):
        break
cap.release()
cv.destroyAllWindows()