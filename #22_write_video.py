import cv2
import webbrowser


#! READ THIS:
# http://www.fourcc.org/codecs.php
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#cv2.VideoWriter.open


# video = cv2.VideoCapture('images/pepole.gif')

# ? Python: cv2.VideoWriter(filename, fourcc, fps, frameSize[, isColor])

# codec = cv2.VideoWriter_fourcc(*'mp4v')  # same as ('X', 'V', 'I', 'D')
# fps = int(video.get(cv2.CAP_PROP_FPS))
# frames_num = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
# w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
# h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# colored_video = True

# writer = cv2.VideoWriter('ped.mp4', codec, fps, (w, h), colored_video)

# # # ? another way
# while video.isOpened():
#     graped, frame = video.read()
#     key = cv2.waitKey(1)
#     if (key & 0xFF) == ord('0') or not graped:
#         break

#     writer.write(frame)
#     cv2.imshow("video", frame)

# #     #! I don't need to wait because I don't need to see the original video
# #     # cv2.waitKey(fps)


# writer.release()
# video.release()
# webbrowser.open('ped.mp4')


# ? Backward Video
original_video = cv2.VideoCapture('ped.mp4')

codec = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(original_video.get(cv2.CAP_PROP_FPS))
frames_num = int(original_video.get(cv2.CAP_PROP_FRAME_COUNT))
w = int(original_video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(original_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
colored_video = True

writer_backward = cv2.VideoWriter('ped_backward.mp4', codec, fps, (w, h), True)

frame_index = original_video.get(cv2.CAP_PROP_FRAME_COUNT) - 1

while frame_index > -1:
    original_video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    graped, frame = original_video.read()

    key = cv2.waitKey(1)
    if (key & 0xFF) == ord('q') or not graped:
        break

    writer_backward.write(frame)
    frame_index -= 1

writer_backward.release()
original_video.release()
webbrowser.open('ped_backward.mp4')
