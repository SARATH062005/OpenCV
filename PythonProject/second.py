import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    width= int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)

    dim= (width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)

cap=cv.VideoCapture('Videos/cat.mp4')

while True:
    istrue , frame = cap.read()
    resized_frame=rescaleFrame(frame,scale=0.75)
    cv.imshow("videos",frame)
    cv.imshow("Resized",resized_frame)
    if cv.waitKey(20) & 0xFF==ord('c'):
        break
cap.release()
cv.destroyAllWindows()