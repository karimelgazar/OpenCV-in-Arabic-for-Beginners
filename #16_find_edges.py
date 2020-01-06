import cv2
import numpy as np

img_path = "images/coins.jpg"
# img_path = "images/brain.jpg"
image = cv2.imread(img_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)


#? Laplacian #
lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

#? Sobel #
# sobel_x = np.uint8(np.absolute(cv2.Sobel(image, cv2.CV_64F, 1, 0)))
# sobel_y = np.uint8(np.absolute(cv2.Sobel(image, cv2.CV_64F, 0, 1)))
# sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)

# cv2.imshow("Sobel X", sobel_x)
# cv2.imshow("Sobel Y", sobel_y)
# cv2.imshow("Sobel Combined", sobel_combined)
# cv2.waitKey(0)

#? Canny Edge Detector #
# blur = cv2.GaussianBlur(image, (7, 7), 0)
# canny = cv2.Canny(blur, 30, 160)
# cv2.imshow("Canny", canny)
# cv2.waitKey(0)

#? Canny With TrackBar #
# WIN_NAME = "Detection"
# TB_Kernel_Size = "Kernel Size"
# cv2.namedWindow(WIN_NAME)
# cv2.createTrackbar(TB_Kernel_Size, WIN_NAME, 11, 50, lambda x: x)
# cv2.setTrackbarMin(TB_Kernel_Size, WIN_NAME, 3)

# while(True):
#     k_size = cv2.getTrackbarPos(TB_Kernel_Size, WIN_NAME)
#     if k_size % 2 == 0:
#         k_size += 1
#         cv2.setTrackbarPos(TB_Kernel_Size, WIN_NAME, k_size)

#     copy = image.copy()

#     blurred = cv2.GaussianBlur(copy, (k_size, k_size), 0)
#     edges = cv2.Canny(blurred, 30, 160)

#     key = cv2.waitKey(1)
#     if key == 27:
#         break

#     cv2.imshow(WIN_NAME, edges)
