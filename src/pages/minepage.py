#ecoding=utf-8
# author:herui
# time:2020/8/24 14:52
# function: 手机银行“我的”页面
import logging

from selenium.webdriver.common.by import By

from src.pages.basepage import BasePage
from src.pages.loginpage import LoginPage


class Mine(BasePage):
    _logon_button = (By.ID, "bt_more_login")
    _reg = (By.ID, "tv_login_registe")
    _reg_now = (By.XPATH, BasePage.byAttr("立即注册"))
    # _login_btn = (By.XPATH, BasePage.byAttr("已开通账号直接登陆"))
    _login_btn = (By.ID, "rl_direct_login")
    _text = (By.XPATH, "安全退出")

    def to_register(self):
        self.find(self._logon_button).click()
        self.find(self._reg_now).click()
        return self

    def register(self):
        pass

    def to_login(self):
        logging.info("准备进入登录页面")
        self.find(self._logon_button).click()
        # self.find(self._login_btn).click()
        self.driver.implicitly_wait(3)
        return LoginPage()


    def login(self):
        pass

    def get_result(self):
        return self.find(self._text).text

