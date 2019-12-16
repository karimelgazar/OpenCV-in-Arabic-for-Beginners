import numpy as np
import cv2

RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

image = cv2.imread("images\khwarizmy.jpg")
cv2.imshow("Croped", image[200:300, 200:500])
cv2.waitKey(0)

###? Image ###
canvas = np.zeros((300, 300, 3), dtype="uint8")
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

###? Lines ###
cv2.line(canvas, (0, 0), (300, 100), RED, 1)
cv2.imshow('Red Line Canvas', canvas)
cv2.waitKey(0)

cv2.line(canvas, (300, 0), (0, 300),  GREEN, 30)
cv2.imshow('Red X Green Lines Canvas', canvas)
cv2.waitKey(0)

###? Rectangle ###
cv2.rectangle(canvas, (100, 100), (200, 200),  BLUE, -1)
cv2.imshow('Blue Regtangle Canvas', canvas)
cv2.waitKey(0)

###? Circle ###
center = canvas.shape[1] // 2, canvas.shape[0] // 2
cv2.circle(canvas, center, 55, GREEN, -1)
cv2.imshow('Circle Canvas', canvas)
cv2.waitKey(0)

###? Bullseye ###
for r in range(25, 151, 25):
    cv2.circle(canvas, center, r, (255, 100, 255))
cv2.imshow('BullEyes Canvas', canvas)
cv2.waitKey(0)


print(type(np.random.randint(0, high=256, size=(3,)).tolist()[0]))
print(type(np.random.randint(0, high=256, size=(3,))[0]))

for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=3).tolist()
    pt = np.random.randint(0, high=300, size=(2,)).tolist()
    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Random Circles Canvas", canvas)
cv2.waitKey(0)
