
# check first if the PIL is installed
#! press (ctrl + z) to exit python

# ? python -m pip install Pillow
# ? conda install -c anaconda pillow

from PIL import Image, ImageFont, ImageDraw
import numpy as np
import random
import cv2
import os

img_w = 1920
img_h = 1080
coordination = (400, 300)
color = (67, 195, 244)  # BGR
size = 50  # font size

image = np.zeros((img_h, img_w, 3), dtype='uint8')

# Make into PIL Image
im_p = Image.fromarray(image)
draw = ImageDraw.Draw(im_p)

# Get a drawing context ==> #? shell:fonts

fonts = [x for x in os.listdir("C:/Windows/Fonts")
         if x.endswith('.ttf')]
random.shuffle(fonts)

# ? FOR specific font
# nirmala_bold = ImageFont.truetype(
#     "‪C:/Windows/Fonts/BRLNSB.TTF", size)

# draw.text(coordination,
#           "Allah",
#           color,
#           font=nirmala_bold)

x, y = 1, 50
for index, font in enumerate(fonts[:180]):
    if (index + 1) % 20 == 0:
        x += 1
        y = 50

    draw.text((200 * x, y),
              "Allah",
              color,
              font=ImageFont.truetype(font, size))
    y += 50

# Convert back to OpenCV image and save
# BECAUSE ITS TYPE IS :
# <PIL.Image.Image image mode=RGB size=1000x800 at 0x17E183CC888>

result = np.array(im_p)
cv2.imshow('image', result)
# cv2.imwrite('e:/captures/photo.png', result)
cv2.waitKey(0)
