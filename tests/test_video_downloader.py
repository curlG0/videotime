import unittest
from videotime.video_downloader import download_video


class TestVideoDownloader(unittest.TestCase):
    def test_download(self):
        download_video("https://www.youtube.com/watch?v=De8vZW8ws6o")
