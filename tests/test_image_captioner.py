import os
import unittest
from os import path

from videotime.self_critical.wrapper_single_image import analyze_image

TMP_DIR = '.tmp'
dir_path = os.path.dirname(os.path.realpath(__file__))


class TestImageCaptioner(unittest.TestCase):
    def test_image_captioning(self):
        test_image = path.join(dir_path, '../test_images/cat.jpg')

        caption = analyze_image(test_image)
        self.assertEqual(caption, 'a cat sitting on top of a field')
