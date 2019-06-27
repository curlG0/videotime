import logging

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
        processor.process()

    def is_processed(self, url: str) -> bool:
        search_video(url)
        return False
