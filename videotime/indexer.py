import logging
import os

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Text, Document, Search, Long, Keyword
from elasticsearch_dsl.connections import connections
from urllib3.exceptions import NewConnectionError

host = os.getenv('elasticsearch_host', 'localhost')

print("Connecting to %s" % host)
connections.create_connection(hosts=[host])

logging.getLogger('elasticsearch').setLevel(logging.INFO)
log = logging.getLogger(__name__)
client = Elasticsearch()

YOUTUBE_VIDEO_INDEX = "videos"


class YoutubeVideo(Document):
    title = Keyword()
    description = Text()
    semantic = Text()
    url = Keyword()

    class Index:
        name = YOUTUBE_VIDEO_INDEX

    def save(self, **kwargs):
        return super(YoutubeVideo, self).save(**kwargs)


class YoutubeVideoFrame(Document):
    title = Keyword()
    description = Text()
    semantic = Text()
    url = Keyword()
    frame_number = Long()

    class Index:
        name = 'video-frames'

    def save(self, **kwargs):
        return super(YoutubeVideoFrame, self).save(**kwargs)


def search_video(url):
    s = Search(using=client, index=YOUTUBE_VIDEO_INDEX).query("term", url=url)
    return s.execute()


def init():
    for i in range(0, 5):
        try:
            YoutubeVideo.init()
            YoutubeVideoFrame.init()
            return
        except NewConnectionError as e:
            log.warning("Error while connecting to elastic search. Retrying..")
    log.error("Error while connecting to elastic search.")


init()
