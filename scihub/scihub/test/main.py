import yml_logging
import test_logging
import logging

yml_logging.setup_logging()
logger = logging.getLogger(__name__)


def main():
    logger.info("aaaaaaaaaaaaaa")
    logger.debug("aaaaaaaaaaaaaa")
    logger.error("aaaaaaaaaaaaaa")
    logger.warning("aaaaaaaaaaaaaa")
    logger.critical("aaaaaaaaaaaaaa")

    test_logging.foo()


if __name__ == "__main__":
    main()
