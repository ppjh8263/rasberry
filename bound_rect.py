import cv2

image = cv2.imread('image12.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(image_gray, 175, 255, 0)
thresh = cv2.bitwise_not(thresh)
# cv2.imshow('Image', thresh)
# cv2.waitKey(0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 2)
# cv2.imshow('Image', image)
# cv2.waitKey(0)
contour = contours[0]
x, y, w, h = cv2.boundingRect(contour)
image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
cv2.imshow('Image', image)
cv2.waitKey(0)