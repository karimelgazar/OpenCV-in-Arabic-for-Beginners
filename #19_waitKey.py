import cv2

image = cv2.imread("images/khwarizmy.jpg")
cv2.imshow('Image', image)
cv2.waitKey(5000)
print('hi')


# while True:
#     cv2.imshow('Image', image)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# 1048675 when NumLock is activated
# 99 otherwise

# 11111111 & 100000000000001100011

# ?? Questions
# 1 - how to get the ascii of any key ==> ord
# 2 - what is 0xFF ==> 0b11111111
# 3 - what does the bitwise operator (&) do
