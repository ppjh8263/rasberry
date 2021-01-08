from imutils.video import VideoStream
import imutils
import time
import cv2

#vs = VideoStream(src=0).start() #0: first cam, 1: second cam
vs = VideoStream(usePiCamera=True, resolution=(640, 480)).start()
time.sleep(2.0)

while True:
    # grab the frame
    frame = vs.read()
    # codes for image processing
    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    
cv2.destroyAllWindows()
vs.stop()