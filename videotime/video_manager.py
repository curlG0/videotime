import os.path
from os import path
import logging
import tempfile
from os.path import join

from videotime.indexer import YoutubeVideo
from videotime.semantic_extractors.image_extractor import extract
from videotime.video_downloader import download_video, get_info
from videotime.video_splitter import split


class VideoManager:
    VIDEO_MARKERS_DIR = ".data/markers"

    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    def process_video(self, url: str):
        info = get_info(url)

        if self.is_processed(info['id']):
            self.log.info("Video already processed (%s). Skipping..." % url)
            return

        with tempfile.TemporaryDirectory() as tmp_dir:
            self.log.info("Processing video (%s) into: %s..." % (url, tmp_dir))
            video_file = "%s/video" % tmp_dir
            download_video(url, video_file)
            self.log.info("Splitting video frames...")
            frame_dir = "%s/frames" % tmp_dir
            os.makedirs(frame_dir)
            split(video_file, frame_dir)
            self.log.info("Extracting semantic from video frames...")
            total_semantic = ""
            for image in os.listdir(frame_dir):
                semantic = extract(join(frame_dir, image))
                total_semantic += "%s \n" % semantic

            video = YoutubeVideo(
                title=info['title'],
                url=url,
                semantic=total_semantic,
                description=info['description'])
            video.save()
            self.log.info("Indexed video: %s" % info['title'])

        self.mark_as_processed(info['id'])

    def mark_as_processed(self, id: str):
        filename = "%s/%s" % (self.VIDEO_MARKERS_DIR, id)
        os.makedirs(self.VIDEO_MARKERS_DIR, exist_ok=True)
        with open(filename, 'a'):
            os.utime(filename, None)

    def is_processed(self, id: str) -> bool:
        return path.exists("%s/%s" % (self.VIDEO_MARKERS_DIR, id))
