import numpy as np
import cv2


def detect_face():
    """
    This method let the user to freely move the rectangle
    until he is satisfied with the result.

    Returns:
        (h_distance, v_distance, sq_length)
        h_distance : the horizontal distace for the top left corner of the square
        v_distance : the vertical distace for the top left corner of the square
        sq_length : the side length of the the the square
    """
    while(True):
        sq_length = cv2.getTrackbarPos(TB_SQUARE, Win_NAME)
        h_distance = cv2.getTrackbarPos(TB_HORIZONTAL, Win_NAME)
        v_distance = cv2.getTrackbarPos(TB_VERTICAL, Win_NAME)

        copy = image.copy()

        key = cv2.waitKey(1)
        if key == 27:
            return (h_distance, v_distance, sq_length)

        if sq_length > 0:
            cv2.rectangle(copy,
                          (h_distance, v_distance),
                          (h_distance + sq_length, v_distance + sq_length), GREEN, 3)

        cv2.imshow(Win_NAME, copy)


#? Text #
def recognize_face(name, start):
    """
    write the @param name inside a filled rectangle
    with the @param start as the bottom left corner of the rectangle 

    Arguments:
        name {string} -- [the name to show iside the rectangle]
        start {tuple} -- [ the bottom left corner of the rectangle]
    """
    width = len(name) * 19
    height = 40
    cv2.rectangle(image, (start[0], start[1] - height), (start[0] + width,
                                                         start[1]), GREEN, -1)
    cv2.putText(image, name, (start[0], start[1] - 10),
                cv2.FONT_ITALIC, 0.75, BLACK, 1)


Win_NAME = "The Image"
TB_SQUARE = "Square Length"
TB_HORIZONTAL = "Horizontal Distance"
TB_VERTICAL = "Vertical Distance"
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

image = cv2.imread("images/khwarizmy.jpg")
img_h = image.shape[0]
img_w = image.shape[1]


#? TrackBar #
cv2.namedWindow(Win_NAME)
cv2.createTrackbar(TB_SQUARE, Win_NAME, 100, 400, lambda x: x)
cv2.createTrackbar(TB_HORIZONTAL, Win_NAME, 0, img_w, lambda x: x)
cv2.createTrackbar(TB_VERTICAL, Win_NAME, 0, img_h, lambda x: x)


h_distance, v_distance, sq_length = detect_face()
cv2.rectangle(image,
              (h_distance, v_distance),
              (h_distance + sq_length, v_distance + sq_length), GREEN, 3)
recognize_face("Al-Khwarizmy", (h_distance, v_distance))
cv2.imshow(Win_NAME, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
