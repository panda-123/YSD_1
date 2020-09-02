#ecoding=utf-8
# author:herui
# time:2020/8/25 14:49
# function:
import logging
import time

from selenium.webdriver.common.by import By

from src.pages.YSDpages.customerinfopage import CustomerInfoPage
from src.pages.basepage import BasePage


class MyLoan(BasePage):
    _apply_now = (By.XPATH, "//*[@text='贷款申请']")

    def apply_loan(self):
        logging.info("------已经进入【我的贷款】页面。。。")
        self.find(self._apply_now).click()
        time.sleep(5)
        return CustomerInfoPage()