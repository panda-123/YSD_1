#ecoding=utf-8
# author:herui
# time:2020/8/24 14:40
# function:

from selenium import webdriver
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AppDriver(object):
    # driver = None
    # "@type driver: WebDriver"
    # 下面方法适用于python 3.5以上
    driver: WebDriver = None

    @classmethod
    def getDriver(cls):
        return cls.driver
    @classmethod
    def initDriver(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "MIMax"
        # udid指定 特定的设备
        # caps["udid"] = "192.168.63.101:5555"
        caps["appPackage"] = "com.urthinker.langfangbank.lfbank"
        caps["appActivity"] = ".activity.SplashActivity"
        # 设置不清除已有数据
        caps["noReset"] = "True"
        caps["fullReset"] = "False"
        # 从底层获取一些权限，规避获取权限的弹框
        caps["autoGrantPermissions"] = "true"
        # 8.0主打UiAutomator2
        caps["automationName"] = "UiAutomator2"

        # remote方法:远程连接命令行工具
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # cls.driver = webdriver.Remote("http://localhost:5037/wd/hub", caps)
        cls.driver.implicitly_wait(10)


