import cv2

# preparing OpenCV
IMG_PATH = "images\khwarizmy.jpg"
Win_NAME = "The Image"
TB_NAME = "Pixel Size"
GREEN = (0, 255, 0)
RED = (0, 0, 255)

image = cv2.imread(IMG_PATH)
cv2.namedWindow(Win_NAME)
cv2.createTrackbar(TB_NAME, Win_NAME, 0, 35, lambda x: x)


def show_pixels():
    while(True):
        pixel = cv2.getTrackbarPos(TB_NAME, Win_NAME)
        copy = image.copy()

        key = cv2.waitKey(1)
        if key == 27:
            break

        img_h = copy.shape[0]
        img_w = copy.shape[1]

        if pixel > 0:
            cv2.rectangle(copy, (0, 0), (pixel, pixel), RED, -1)
            for h in range(pixel, img_h, pixel):  # ? Drawing Horizontal Lines
                cv2.line(copy, (0, h), (img_w, h), GREEN, 1)

            for v in range(pixel, img_w, pixel):  # ? Drawing Vertical Lines
                cv2.line(copy, (v, 0), (v, img_h), GREEN, 1)

        cv2.imshow(Win_NAME, copy)
        print("Pixel at (0, 0):", copy[0, 0], end='\r')


show_pixels()

# image[300:350, 300:350] = [255, 0, 0]
# cv2.imshow(Win_NAME, image)
# cv2.waitKey(0)

cv2.destroyAllWindows()

# print(cv2.imwrite('E:\l.jpg', image))
