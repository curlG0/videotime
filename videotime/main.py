import logging
from videotime.resources import app


def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s [%(name)s] %(message)s')
    log = logging.getLogger('main')
    log.info("Starting videotime...")

    app.run()


if __name__ == '__main__':
    main()
