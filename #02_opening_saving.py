"""
First look at openCv and starting by:
1- opening the image
2- exploring other methods 
3- saving image in other format
"""

import cv2

###? preparing OpenCV ###

#! Don't use single quote (') in the image path
IMG_PATH = "images\khwarizmy.jpg"

image = cv2.imread(IMG_PATH)

print("Shape: {}".format(image.shape))  # (height, width, 3)
print("height: {} pixels".format(image.shape[0]))
print("width: {} pixels".format(image.shape[1]))
print("channels: {}".format(image.shape[2]))

cv2.imshow('The Image', image)
cv2.waitKey(0)

print(cv2.imwrite('images/modified.png', image))
