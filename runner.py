#ecoding=utf-8
# author:herui
# time:2020/8/19 17:17
# function:
import logging
import os
import time

import allure
import pytest
import subprocess
import sys

sys.path.append(os.path.dirname(sys.modules[__name__].__file__))

file_name = r"E:\Hogwarts\python\YSD\log\uiauto.log"
# time_line = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
# log_path = os.getcwd() + "\\" + "log" + "\\"
# print(log_path)
# file_name = log_path + time_line + '.log'

# 创建处理器 fileHandler
# 创建日志器logger，设置日志级别
# 创建格式处理器 Format,并将其添加到处理器
# 为日志器添加 处理器
logger = logging.getLogger()
logger.setLevel(logging.INFO)

filehandler = logging.FileHandler(file_name, encoding="utf-8")
# filehandler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s %(levelname)s %(filename)s %(lineno)d:%(message)s")
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)

if __name__=="__main__":
    logging.info("开始执行了~~~~~~~~~~~~~~~~~~")
    # print(os.getcwd())
    pytest.main(['-sq', './testcase/test_Taxcertify.py'])
    # pytest.main(['-sq', '--alluredir','./testreport/06','./testcase/test_Taxcertify.py'])
    # split = 'allure ' + 'generate ' + './testreport/06 ' + '-o ' + './testreport/06/html ' + '--clean'
    # os.system('cd E:/Hogwarts/python/YSD/testreport/06')
    # os.system(split)
    # print(split)
    logging.info("执行结束了--------------------")
