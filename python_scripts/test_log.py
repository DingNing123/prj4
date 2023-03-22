import logging
import argparse
import sys

def set_logging_level(loglevel='error'):
    '''
    loglevel:"debug", "info", "warning", "error", "critical
    # assuming loglevel is bound to the string value obtained from the
    # command line argument. Convert to upper case to allow the user to
    # specify --log=DEBUG or --log=debug
    '''
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)

    logging.basicConfig(
    # logging.basicConfig(filename='myapp.log',\
            level=numeric_level,\
            format='%(levelname)s : %(name)s [line:%(lineno)d]  %(asctime)s %(message)s',\
            filemode='w',\
            # encoding='utf-8',\  # python 3.7 not support
            datefmt='%m/%d/%Y %I:%M:%S %p')

parser = argparse.ArgumentParser()
parser.add_argument("--log", type=str,
    choices=["debug", "info", "warning", "error", "critical"],
    default="error")

args = parser.parse_args()
loglevel=args.log


set_logging_level(loglevel=loglevel)

logging.warning('is when this event was logged.')
logging.info('is when this event was logged.')
logger = logging.getLogger(__name__)
logger.info("test loggerr")


