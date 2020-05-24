import cv2
import numpy as np

img_path = "images/coins.jpg"
image = cv2.imread(img_path)
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#! changing the blur kernel size affects the detection
#! like with >>>  coins.webp
blurred = cv2.GaussianBlur(gray, (15, 15), 0)
edged = cv2.Canny(blurred, 30, 180)
cv2.imshow("Edged", edged)

#? Finding Contours #

# ! opencv فى قائمة المخرجات وفقا لاصدار مكتبة contours ترتيب ال
if (cv2.__version__)[0] in '24':
    contours, _ = cv2.findContours(edged,
                                   cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
else:
    _, contours, _ = cv2.findContours(edged,
                                      cv2.RETR_EXTERNAL,
                                      cv2.CHAIN_APPROX_SIMPLE)
print('=' * 30)
print("{} objects found".format(len(contours)).title())
print('=' * 30)

cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.imshow("Objects Found", image)

#? Extracting Objects One By One #

# * we used the mask in full size of the original image
# * so we can use x and y of the bounding triangele
# * and also so we can draw a circle
mask = np.zeros(image.shape[:2], np.uint8)

for i, c in enumerate(contours):
    # ? if taken with PhotoShop
    x, y, w, h = cv2.boundingRect(c)
    coin = image[y:y+h, x:x+w]

    # ? Original Coin
    (cX, cY), r = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(cX), int(cY)), int(r), 255, -1)
    cv2.imshow('Mask', mask)

    coin_mask = mask[y:y+h, x:x+w]
    masked = cv2.bitwise_and(coin, coin, mask=coin_mask)
    cv2.imshow("Original & Masked", np.hstack((coin, masked)))
    print('Object #{}'.format(i+1))
    cv2.waitKey(0)
