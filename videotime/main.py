import logging
from resources import app

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s [%(name)s] %(message)s')
    log = logging.getLogger('main')
    log.info("Starting videotime...")

    app.run()