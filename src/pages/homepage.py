#ecoding=utf-8
# author:herui
# time:2020/8/24 14:56
# function: 手机银行主页
import logging

from selenium.webdriver.common.by import By

from src.pages.YSDpages.ysdpage import YSDPage
from src.pages.basepage import BasePage
from src.pages.minepage import Mine


class HomePage(BasePage):

    _mine = (By.XPATH, BasePage.byAttr(text="我的", id='rb_more'))
    _home_page = (By.XPATH, BasePage.byAttr(text="首页"))
    _all_server = (By.XPATH, BasePage.byAttr(text="全部服务"))
    _loan = (By.XPATH, BasePage.byAttr(text="贷款"))
    _et_centre_search = (By.ID, "et_centre_search")
    _et_search = (By.ID, "et_search")
    _tv_item = (By.ID, "tv_item")
    _YSD = (By.XPATH, BasePage.byAttr(text="银税贷"))


    def to_mine(self):
        logging.info("进入“我的”页面了。。。")
        self.find(self._mine).click()
        return Mine()

    def to_homepage(self):
        self.find(self._home_page).click()
        return self

    def to_all_server(self):
        self.find(self._all_server).click()
        return self

    def to_loan(self):
        self.find(self._loan).click()
        return self

    def to_YSD(self):
        logging.info("准备进入YSD页面")
        self.find(self._et_centre_search).click()
        el = self.find(self._et_search)
        self.set_value(el, "银税贷")
        self.find(self._tv_item).click()
        return YSDPage()

