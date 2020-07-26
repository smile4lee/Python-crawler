import logging.config

logger = logging.getLogger(__name__)


def foo():
    logger.debug('This is a debug message')
    logger.info('This is a info message')
    logger.error('This is error message')
    logger.critical('This is a critical message')

    logger.info('%s, %s', 'a', 'b')
