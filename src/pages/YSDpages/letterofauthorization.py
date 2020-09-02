#ecoding=utf-8
# author:herui
# time:2020/8/19 15:03
# function: 检查授权委托书
from selenium.webdriver.common.by import By

from src.pages.basepage import BasePage


class LetterOfAuthorization(BasePage):
    _marginTop = (By.CLASS_NAME, "marginTop")

    def check_letter_of_authorization(self):
        return self.find(self._marginTop).text