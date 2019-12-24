import numpy as np
import argparse
import cv2

"""
How to solve this problem?
==========================
1- use if statement
2- use moduls %255
"""

"""
THE SOLUTION:
===============
1-NumPy will perform arithmetic and “wrap around”.

2-OpenCV will perform clipping stop if exceeded 255 or less than zero.
"""

print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8
                                      ([100]))))
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8
                                         ([100]))))

print("wrap around: {}".format(np.uint8([200]) + np.uint8([56])))

print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))


IMG_PATH = "images\khwarizmy.jpg"

image = cv2.imread(IMG_PATH)
cv2.imshow("Original", image)

M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)

M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)
