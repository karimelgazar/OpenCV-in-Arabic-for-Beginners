import numpy as np
import cv2

image = cv2.imread("images/khwarizmy.jpg")

###? Color Spaces ###
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
cv2.imshow("L*a*b", lab)
