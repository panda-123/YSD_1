#ecoding=utf-8
# author:herui
# time:2020/8/17 11:12
# function:
from selenium.webdriver.common.by import By

from driver.browerdriver import BrowerDriver
from pages.loginpage import LoginPage

class TestLogin(object):
    def setup_class(self):
        self.login = LoginPage()

    def teardown_class(self):
        BrowerDriver.driver.close()

    def test_login(self):
        self.login.login_page("18633793529","ws123456")
        # element = self.driver.
        assert self.login.get_text() == "我的豆瓣"

    def test_search_book(self):
        self.login.login_page("18633793529","ws123456").\
            to_books_page().\
            search_book("利用python进行数据分析")


