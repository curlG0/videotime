import logging
from time import sleep

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s [%(name)s] %(message)s')
    log = logging.getLogger('main')
    log.info("Starting videotime...")
    sleep(1000)
