import logging

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Text, Document, Search, Long
from elasticsearch_dsl.connections import connections
from urllib3.exceptions import NewConnectionError

connections.create_connection(hosts=['localhost'])

logging.getLogger('elasticsearch').setLevel(logging.INFO)
log = logging.getLogger(__name__)
client = Elasticsearch()

YOUTUBE_VIDEO_INDEX = "videos"


class YoutubeVideo(Document):
    title = Text()
    description = Text()
    semantic = Text()
    url = Text()

    class Index:
        name = YOUTUBE_VIDEO_INDEX

    def save(self, **kwargs):
        return super(YoutubeVideo, self).save(**kwargs)


class YoutubeVideoFrame(Document):
    title = Text()
    description = Text()
    semantic = Text()
    url = Text()
    frame_number = Long()

    class Index:
        name = 'video-frames'

    def save(self, **kwargs):
        return super(YoutubeVideoFrame, self).save(**kwargs)


def search_video(url):
    s = Search(using=client, index=YOUTUBE_VIDEO_INDEX)\
        .filter("term", category="search")\
        .query("match", title="python")
    return s.execute()


try:
    YoutubeVideo.init()
    YoutubeVideoFrame.init()
except NewConnectionError as e:
    log.error("Error while connecting to elastic search", e)
    exit(1)

