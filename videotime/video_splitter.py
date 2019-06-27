import cv2
import math


class Splitter:
    def __init__(self):
        self.listener = None

    def split(self, video_file: str, frame_dir: str, frame_period_sec=10):
        count = 0
        cap = cv2.VideoCapture(video_file)  # capturing the video from the given path
        fps = cap.get(cv2.CAP_PROP_FPS)

        success = True
        while success:
            success, frame = cap.read()

            time = count / fps

            if count % math.floor(frame_period_sec * fps) == 0:
                filename = "%s/frame%d.jpg" % (frame_dir, count)
                cv2.imwrite(filename, frame)
                if self.listener is not None:
                    self.listener(count, time, filename)
            count += 1

        cap.release()

    def set_listener(self, listener):
        self.listener = listener
