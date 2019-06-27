import logging
import threading

from videotime.indexer import search_video
from videotime.video_processor import VideoProcessor


class VideoManager:
    VIDEO_MARKERS_DIR = ".data/markers"

    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    def process_video(self, url: str):
        if self.is_processed(url):
            self.log.info("Video already processed (%s). Skipping..." % url)
            return

        processor = VideoProcessor(url)
        t = threading.Thread(target=processor.process)
        t.start()

    def is_processed(self, url: str) -> bool:
        res = search_video(url)
        return len(res.hits) > 0


manager = VideoManager()
