import logging

import yaml

from videotime.resources import app
from videotime.video_manager import manager

CONFIG_FILE = "configs/config.yml"

def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s [%(name)s] %(message)s')
    log = logging.getLogger('main')
    log.info("Starting videotime...")


    with open(CONFIG_FILE) as f:
        config = yaml.safe_load(f)

    for video_url in config['preload']:
        manager.process_video(video_url)

    app.run()


if __name__ == '__main__':
    main()
