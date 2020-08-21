#ecoding=utf-8
# author:herui
# time:2020/8/20 16:55
# function:

import logging

logging.basicConfig(filename='logger.log', level=logging.INFO)

logging.debug('debug message')
logging.info('info message')
logging.warning('warn message')
logging.error('error message')
logging.critical('critical message')