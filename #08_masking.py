import numpy as np
import cv2

image = cv2.imread("images/khwarizmy.jpg")
cv2.imshow("Original", image)

###? Masking ###
mask = np.zeros(image.shape[:2], dtype=np.uint8)
center = (image.shape[1] // 2, image.shape[0] // 2)

cv2.circle(mask, tuple(center), 200, 255, -1)
cv2.imshow("Mask", mask)

selected = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('With Mask', selected)
cv2.waitKey(0)
