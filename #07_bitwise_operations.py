import numpy as np
import cv2


square = np.zeros((300, 300), dtype="uint8")
color = 255  # ! Why I used only one integer instead of a tuple?
cv2.rectangle(square, (25, 25), (275, 275), color, -1)
cv2.imshow("Square", square)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)

#? And #
bitwiseAnd = cv2.bitwise_and(square, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

#? Or #
bitwiseOr = cv2.bitwise_or(square, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

#? Xor #
bitwiseXor = cv2.bitwise_xor(square, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

#? Truthy and Falsy Values #
v = 1
if v:
    print("it wasn't zero.".title())
else:
    print("it was zero.".title())

#? Not #
bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)
