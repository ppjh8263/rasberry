import numpy as np
import cv2
import picamera
import time

camera = picamera.PiCamera()

# camera.hflip = True
# camera.vflip = True

camera.start_preview()
time.sleep(1)
camera.stop_preview()

camera.capture('./pic.jpg')


def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect



imgfile = "./pic.jpg"
image = cv2.imread(imgfile)
orig = image.copy()

r = 800.0 / image.shape[0]
dim = (int(image.shape[1] * r), 800)
img = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 75, 200)

contour, hierarcy = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contour = sorted(contour, key=cv2.contourArea, reverse=True)[:5]

for c in contour:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, peri * 0.02, True)
    
    if len(approx) == 4:
        screenCnt = approx
        print(screenCnt)

        break


cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 2)


rect = order_points(screenCnt.reshape(4, 2) / r)
(topLeft, topRight, bottomLeft, bottomRight) = rect

w1 = abs(bottomRight[0] - bottomLeft[0])
w2 = abs(topRight[0] - topLeft[0])
h1 = abs(topRight[1] - bottomRight[1])
h2 = abs(topLeft[1] - bottomLeft[1])

maxWidth = max([w1, w2])
maxHeight = max([h1, h2])

dst = np.float32([[0,0], [maxWidth-1, 0], [maxWidth-1, maxHeight-1], [0, maxHeight-1]])

M = cv2.getPerspectiveTransform(rect, dst)
warped = cv2.warpPerspective(orig, M, (maxWidth, maxHeight)) #Perspective를 적용을 할떄에는 원본 이미지로?

warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
warped = cv2.adaptiveThreshold(warped, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10)

cv2.imshow("Original",orig)
cv2.imshow("Scanning", warped)
cv2.imwrite("scannedImage.png", warped)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)