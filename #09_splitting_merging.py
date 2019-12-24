import numpy as np
import cv2

image = cv2.imread("images/boat.jpg")

###? Splitting ###
b, g, r = cv2.split(image)
cv2.imshow("Red Channel", r)
cv2.imshow("Green Channel", g)
cv2.imshow("Blue Channel", b)
cv2.waitKey(0)

###? Merging ###
zero = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.imshow("Red", cv2.merge([zero, zero, r]))
cv2.imshow("Green", cv2.merge([zero, g, zero]))
cv2.imshow("Blue", cv2.merge([b, zero, zero]))
cv2.waitKey(0)

merged = cv2.merge([b, g, r])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
