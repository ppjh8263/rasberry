from imutils.video import VideoStream
import imutils
import time
import cv2

#vs = VideoStream(src=0).start() #0: first cam, 1: second cam
vs = VideoStream(usePiCamera=True, resolution=(640, 480),vflip=True).start()
time.sleep(2.0)

while True:
    # grab the frame
    frame = vs.read()
    # codes for image processing
#     frame =cv2.GaussianBlur(frame,(11,11),0)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     frame = cv2.Canny(frame,100,200)
    
    th,frame=cv2.threshold(frame,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    K=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    frame = cv2.morphologyEx(frame,cv2.MORPH_OPEN,K)
    frame = cv2.morphologyEx(frame,cv2.MORPH_CLOSE,K)
    
    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    
cv2.destroyAllWindows()
vs.stop()