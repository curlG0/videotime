import unittest
from videotime.video_downloader import download_video
from videotime.video_splitter import Splitter

TMP_DIR = '.tmp'


class TestVideoDownloader(unittest.TestCase):
    def test_download_and_split(self):
        video_file = "%s/video.mp4" % TMP_DIR
        download_video("https://www.youtube.com/watch?v=9ntcGWP_oN4", video_file)
        splitter = Splitter()
        splitter.split(video_file, TMP_DIR)
