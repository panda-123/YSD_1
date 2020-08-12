#ecoding=utf-8
# author:herui
# time:2020/8/12 17:23
# function:
from selenium import webdriver


class BrowerDriver(object):

    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument('--disable-infobars')
        self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.implicitly_wait(10)

    def douban(self):
        self.douban = self.driver.get("https://www.douban.com/")
        return self.douban