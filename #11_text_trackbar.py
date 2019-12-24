import numpy as np
import cv2

Win_NAME = "The Image"
TB_NAME = "Scale"
TEXT_NAME = "AL-Khwarizmy"
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLUE = (255, 0, 0)
BLACK = (0, 0, 0)
V = (188, 56, 188)

image = cv2.imread("images/khwarizmy.jpg")
img_h = image.shape[0]
img_w = image.shape[1]


def do_nothing(x):
    pass


#? TrackBar #
cv2.namedWindow(Win_NAME)
cv2.createTrackbar(TB_NAME, Win_NAME, 1, 10, do_nothing)


while(True):
    scale = cv2.getTrackbarPos(TB_NAME, Win_NAME)
    copy = image.copy()

    key = cv2.waitKey(1)
    if key == 27:
        break

    #? Text #
    #* EXERCISE #
    # * Put the text inside a filled rectangle
    cv2.putText(copy, TEXT_NAME,
                (50, 100)  # The beginning of the line we write on.
                ,
                cv2.FONT_ITALIC, scale, V, 5)

    cv2.imshow(Win_NAME, copy)
