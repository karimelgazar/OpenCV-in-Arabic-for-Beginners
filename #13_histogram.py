import cv2
import numpy as np
import matplotlib.pyplot as plt

# Original #
image = cv2.imread("images/boat.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#? Histogram #

#* Gray #
# hist = cv2.calcHist(image_gray, [0], None, [256], [0, 256])

# plt.title("Histogram for grayscale image".title())
# plt.xlabel("pixel value".title())
# plt.ylabel("number of pixels that have this value".title())

# plt.plot(hist)
# plt.xlim([0, 256])

# cv2.imshow("Grayscale", image_gray)
# plt.show()

#* Colored #


def hist_colored(pic, use_mask=False):
    channels = cv2.split(pic)
    colors = list('bgr')  # <<<<==>>>> ['b','g','r']

    plt.title("Histogram for Colored image".title())
    plt.xlabel("pixel value".title())
    plt.ylabel("number of pixels that have this value".title())

    mask = None
    if use_mask:
        plt.title("Histogram for Colored image (with mask)".title())
        mask = np.zeros(image.shape[:2], dtype="uint8")
        cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
        masked = cv2.bitwise_and(pic, pic, mask=mask)
        cv2.imshow("Mask", mask)
        cv2.imshow("Applying the Mask", masked)

    for ch, c in zip(channels, colors):
        #! you must put the image in a list if you used a mask
        hist = cv2.calcHist([ch], [0], mask, [256], [0, 256])
        plt.plot(hist, color=c)
        plt.xlim([0, 256])

    cv2.imshow("The Image", pic)
    plt.show()


# hist_colored(image)
# #* with mask #
hist_colored(image, use_mask=True)

# #? Histogram Equalization #
old = cv2.cvtColor(cv2.imread("images/old.jpg"), cv2.COLOR_BGR2GRAY)
eq = cv2.equalizeHist(old)
cv2.imshow('Histogram Equalization', np.hstack((old, eq)))
cv2.waitKey(0)


# # hist_eq = cv2.calcHist(eq, [0], None, [256], [0, 256])
# # plt.plot(hist)
# # plt.title("Histogram equalized image".title())
# # plt.xlim([0, 256])
# # plt.show()

# # hist_old = cv2.calcHist(old, [0], None, [256], [0, 256])
# # plt.plot(hist)
# # plt.title("Histogram for the original image".title())
# # plt.xlim([0, 256])
# # plt.show()
