import cv2
import numpy as np

image = cv2.imread("images/bug_noisy.jpg")


#? Average Blurring #
def avg_blur():
    #! The Kernel Side Length Must be Odd
    blured = np.hstack([image,
                        cv2.blur(image, (3, 3)),
                        cv2.blur(image, (5, 5)),
                        cv2.blur(image, (7, 7)),
                        cv2.blur(image, (13, 13))])
    cv2.imshow("Average Blur", blured)
    cv2.waitKey(0)


#? Gaussian Blurring #
def gauss_blur():
    # By setting the third parameter to 0, we are instructing OpenCV
    # to automatically compute the weights based on our kernel size
    g_blured = np.hstack([image,
                          cv2.GaussianBlur(image, (3, 3), 0),
                          cv2.GaussianBlur(image, (5, 5), 0),
                          cv2.GaussianBlur(image, (7, 7), 0),
                          cv2.GaussianBlur(image, (13, 13), 0)])
    cv2.imshow("Gaussian Blur", g_blured)
    cv2.waitKey(0)


#? Median Blurring #
def median_blur():
    m_blured = np.hstack([image,
                          cv2.medianBlur(image, 3),
                          cv2.medianBlur(image, 5),
                          cv2.medianBlur(image, 7),
                          cv2.medianBlur(image, 13)])
    cv2.imshow("Median Blur", m_blured)
    cv2.waitKey(0)


#? Bilateral Blurring #
def bilateral():
    filtered = np.hstack([image,
                          cv2.bilateralFilter(image, 5, 21, 21),
                          cv2.bilateralFilter(image, 7, 31, 31),
                          cv2.bilateralFilter(image, 9, 41, 41),
                          cv2.bilateralFilter(image, 12, 51, 51)])
    cv2.imshow("Bilateral", filtered)
    cv2.waitKey(0)


avg_blur()
gauss_blur()
median_blur()
bilateral()
