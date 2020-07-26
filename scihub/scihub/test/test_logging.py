import logging.config
import yml_logging

# logging.config.fileConfig(fname='conf/logging.conf', disable_existing_loggers=False)

# Get the logger specified in the file
# logger = logging.getLogger(__name__)

# yml_log.setup_logging()
logger = logging.getLogger(__name__)

def foo():
    logger.debug('This is a debug message')
    logger.info('This is a info message')
    logger.error('This is error message')
    logger.critical('This is a critical message')

    logger.info('%s, %s', 'a', 'b')
