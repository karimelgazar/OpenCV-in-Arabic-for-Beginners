import cv2
import numpy as np
import os
from tkinter import Tk, filedialog

LINE_SEP = '-'*50
COLORS = [
    # BGR
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255)
]


def make_video(video_path='./images/', width=320, height=320, video_length_in_seconds=10):
    """
        أزرق  |  أحمر   |  أخضر
        ------|---------|---------
         1    |    2    |   3
         4    |    5    |   6
         7    |    8    |   9
         10   |    -    |   -
        ------|---------|---------
         4    |    3    |   3
    """
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 30
    colored_video = True
    video = cv2.VideoWriter(
        os.path.join(video_path, 'video.mp4'), codec, fps, (width, height), colored_video)
    pixels = np.ones((width, height, 3), dtype=np.uint8)

    print('\nCreating Video...')
    for time in range(1, video_length_in_seconds+1):
        img = pixels*COLORS[time % 3]
        for _ in range(fps):
            video.write(img.astype(np.uint8))

    video.release()
    print('\nVideo Created.', LINE_SEP, sep='\n')


def calc_hist(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.calcHist(gray, [0], None, [128], [0, 256])


def are_the_same_images(h1, h2, acceptance_ratio=0.65):
    """
     ======================
     |   😁 الزيادة حلوة  |
     ====================== 

        #! cv2.HISTCMP_CORREL: الترابط 
        [-1, 1] ترجع قيمة بين 
        بــحــيـــث
        1: تطابق تام
        -1: لا يوجد تطابق اطلاقا

        #! cv2.HISTCMP_INTERSECT: التقاطع
        [0, 1] ترجع قيمة بين
        بــحــيـــث
        1: تطابق تام
        0: لا يوجد تطابق اطلاقا


     ======================
     |   😞 الزيادة وحشة  |
     ====================== 
        #! cv2.HISTCMP_CHISQR: chi-squared مسافة
        [0, unbounded] ترجع قيمة بين
        بــحــيـــث
        0: تطابق تام
        unbounded: لا يوجد تطابق اطلاقا
        unbounded: قيمة بعيدة عن الصفر مثلا 10 فما فوق

        #! cv2.HISTCMP_BHATTACHARYYA: Bhattacharyya مسافة between the two
        [0, 1] ترجع قيمة بين
        بــحــيـــث
        0: تطابق تام
        1: لا يوجد تطابق اطلاقا
    """

    ratio = cv2.compareHist(h1, h2, cv2.HISTCMP_INTERSECT)

    return ratio >= acceptance_ratio


def count_occurancec_of_frame(video_path, first_apperance_in_second=0.5):

    video = cv2.VideoCapture(video_path)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    occurance = 0

    video.set(cv2.CAP_PROP_POS_FRAMES, int(fps * first_apperance_in_second))
    fetched, requested_frame = video.read()
    requested_hist = calc_hist(requested_frame)

    if not fetched:
        print('INVALID TIME OR VIDEO!')
        return

    print('\nWorking...')
    while True:
        ret, frame = video.read()
        if not ret:
            break

        hist = calc_hist(frame)
        if are_the_same_images(hist, requested_hist):
            occurance += 1

    
    print("The Frame Appeared {} Times".format((occurance // fps) + 1))
    print(LINE_SEP)


make_video()
count_occurancec_of_frame('./images/video.mp4', 1.5)
