import logging
from videotime.resources import app
from videotime.video_manager import VideoManager


def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s [%(name)s] %(message)s')
    log = logging.getLogger('main')
    log.info("Starting videotime...")

    video_manager = VideoManager()
    video_manager.process_video("https://www.youtube.com/watch?v=De8vZW8ws6o")

    app.run()


if __name__ == '__main__':
    main()
