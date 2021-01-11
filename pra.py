import cv2
img = cv2.imread('./hand.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_resize = cv2.resize(gray, (20, 20))
cv2.imshow('Image', gray_resize)
cv2.waitKey(0)
cv2.imshow('Image', ~gray_resize)
cv2.waitKey(0)


th, frame = cv2.threshold(gray_resize, 0, 255, cv2.THRESH_BINARY +cv2.THRESH_OTSU)

K = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, K)
frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, K)

cv2.imshow('Image', frame)
cv2.waitKey(0)
