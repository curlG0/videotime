import cv2
import math


def split(video_file: str, frame_dir: str):
    count = 0
    cap = cv2.VideoCapture(video_file)  # capturing the video from the given path
    frame_rate = cap.get(5)  # frame rate
    while cap.isOpened():
        frame_id = cap.get(1)  # current frame number
        ret, frame = cap.read()
        if ret != True:
            break
        if frame_id % math.floor(frame_rate) == 0:
            filename = "%s/frame%d.jpg" % (frame_dir, count)
            count += 1
            cv2.imwrite(filename, frame)
    cap.release()
    print("Done!")
