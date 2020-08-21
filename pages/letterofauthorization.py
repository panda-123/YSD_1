#ecoding=utf-8
# author:herui
# time:2020/8/19 15:03
# function:
from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class LetterOfAuthorization(BasePage):
    _marginTop = (By.CLASS_NAME, "marginTop")

    def check_letter_of_authorization(self):
        return self.find(self._marginTop).text