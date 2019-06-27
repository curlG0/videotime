import logging

from elasticsearch_dsl import Keyword, Text, Document
from elasticsearch_dsl.connections import connections
from urllib3.exceptions import NewConnectionError

connections.create_connection(hosts=['localhost'])

logging.getLogger('elasticsearch').setLevel(logging.INFO)
log = logging.getLogger(__name__)


class YoutubeVideo(Document):
    title = Text()
    description = Text()
    semantic = Text()
    url = Text()

    class Index:
        name = 'videos'

    def save(self, **kwargs):
        return super(YoutubeVideo, self).save(**kwargs)


try:
    YoutubeVideo.init()
except NewConnectionError as e:
    log.error("Error while connecting to elastic search", e)
    exit(1)
