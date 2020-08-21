#ecoding=utf-8
# author:herui
# time:2020/8/20 16:39
# function:

import logging
import os
import time

# file_name = r"E:\Hogwarts\python\YSD\log\uiauto.log"
time_line = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.dirname(os.getcwd()) + "\\" + "log" + "\\"
print(log_path)
logfile = log_path + time_line + '.log'
print(logfile)
# 创建处理器 fileHandler
# 创建日志器logger，设置日志级别
# 创建格式处理器 Format,并将其添加到处理器
# 为日志器添加 处理器
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

filehandler = logging.FileHandler(logfile, encoding="utf-8")
filehandler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)-15s %(levelname)s %(filename)s %(lineno)d:%(message)s",
                              "%a %d %b %Y %H:%M:%S")
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)

if __name__ == '__main__':
    logging.info("logging.info: This is logging example, current file log level is logging.DEBUG")
    logging.debug(
        "logging.debug: you should not see this line in log file, "
        "for current file log level to logging.DEBUG")
    logging.warning(
        "logging.warning: you can see this line in log file , "
        "for current file log level to logging.DEBUG, and logging.warning is above logging.DEBUG")
    logging.error(
        "logging.error: you can see this line in log file , "
        "for current file log level to logging.DEBUG, and logging.error is above logging.DEBUG")
