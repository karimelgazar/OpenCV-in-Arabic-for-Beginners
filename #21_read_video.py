import cv2


# ? can be used with:
# 1- webcam
# 2- local video File
# 3- ip camera

# **  1- webcam  **
# video = cv2.VideoCapture(0)
# while True:
#     grabbed, frame = video.read()
#     frame = cv2.resize(frame, (800, 500))

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#     cv2.imshow('video', frame)

# video.release()
# cv2.destroyAllWindows()

# * ============================================

# **  2- local video File  **
video = cv2.VideoCapture("images/road.webm")

# Video Properties : #? CAP_PROP_*
#!READ THIS:
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get


print('============================================')
fps = int(video.get(cv2.CAP_PROP_FPS))
frames_num = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(fps, "FPS")
print(frames_num, "Frames")
print("Width:",  w)
print("Height:", h)
print('Duration: {} seconds'.format(frames_num // fps))
print('============================================')


# ? another way
while video.isOpened():
    graped, frame = video.read()
    key = cv2.waitKey(1)
    if (key & 0xFF) == ord('q') or not graped:
        break

    if (key & 0xFF) == ord('0'):
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)

    cv2.imshow("video", frame)

    cv2.waitKey(fps)  # ? 30 FPS ==> 1 frame per 0.033 second ==> 30 ms


# * ============================================


# **  3- ip camera  **
# video = cv2.VideoCapture(
#     "http://217.126.89.102:8010/axis-cgi/mjpg/video.cgi")
