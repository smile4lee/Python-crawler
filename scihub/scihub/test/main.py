import yml_logging
import test_logging
import logging

# logging.config.fileConfig(fname='conf/logging.conf', disable_existing_loggers=False)
# logger = logging.getLogger(__name__)

yml_logging.setup_logging()
logger = logging.getLogger(__name__)



def main():

    logger.info("aaaaaaaaaaaaaa")
    logger.debug("aaaaaaaaaaaaaa")
    logger.error("aaaaaaaaaaaaaa")
    logger.warn("aaaaaaaaaaaaaa")
    logger.critical("aaaaaaaaaaaaaa")

    test_logging.foo()


if __name__ == "__main__":
    main()
