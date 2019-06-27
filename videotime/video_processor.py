import logging
import os
import tempfile

from videotime.indexer import YoutubeVideo, YoutubeVideoFrame
from videotime.semantic_extractors.image_extractor import extract
from videotime.video_downloader import get_info, download_video
from videotime.video_splitter import Splitter


class VideoProcessor:
    def __init__(self, url):
        self.log = logging.getLogger(self.__class__.__name__)
        self.url = url
        self.info = get_info(self.url)
        self.video_semantic = ""

    def process(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            self.log.info("Processing video (%s) into: %s..." % (self.url, tmp_dir))
            video_file = "%s/video" % tmp_dir
            download_video(self.url, video_file)
            self.log.info("Splitting video frames...")
            frame_dir = "%s/frames" % tmp_dir
            os.makedirs(frame_dir)

            self.log.info("Extracting semantic from video frames...")
            splitter = Splitter()
            splitter.set_listener(self.process_frame)
            splitter.split(video_file, frame_dir)
            video = YoutubeVideo(
                title=self.info['title'],
                url=self.url,
                semantic=self.video_semantic,
                description=self.info['description'])
            video.save()
            self.log.info("Indexed video: %s" % self.info['title'])

    def process_frame(self, count, time, filename):
        semantic = extract(filename)
        self.video_semantic += "%s \n" % semantic

        frame = YoutubeVideoFrame(
            title=self.info['title'],
            url=self.url + "&t=%s" % round(time),
            semantic=semantic,
            description=self.info['description'],
            frame_number=count)
        frame.save()
