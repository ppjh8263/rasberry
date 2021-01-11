import cv2
import time
image=cv2.imread('./image.jpg')

print(image.shape)
print(image.size)

px=image[100,100]

print(px)

print(px[2])


# 
# start_time = time.time()
# for i in range(0, 100):
#     for j in range(0, 100):
#         image[i, j] = [255, 255, 255]
#     print("--- %s seconds ---" % (time.time() - start_time))
# start_time = time.time()
# 
# image[0:100, 0:100] = [0, 0, 0]
# print("--- %s seconds ---" % (time.time() - start_time))


logo = image[20:150, 70:200]
# cv2.imshow('Image', logo)
image[0:130, 0:130] = logo

cv2.imshow('Image', image)
cv2.waitKey(0)