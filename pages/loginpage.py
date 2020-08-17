#ecoding=utf-8
# author:herui
# time:2020/8/13 16:28
# function:
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.basepage import BasePage
from driver.browerdriver import BrowerDriver

class LoginPage(BasePage):
    # 直接写在这里的是 类变量
    # 实际在下面的方法中用self._log_frame 是取不到值的
    _login_frame = (By.TAG_NAME, "iframe")
    _login_table = (By.CLASS_NAME, "account-tab-account")
    _username = (By.ID, "username")
    _pwd = (By.ID, "password")
    _login_btn = (By.PARTIAL_LINK_TEXT, "登录豆瓣")
    _text = (By.PARTIAL_LINK_TEXT, "我的豆瓣")

    def __init__(self):
        # 在这里，带self.的是实例变量，在下面的方法中用self.可取到值
        BasePage.__init__(self)

    def login_page1(self,username,pwd):
        login_frame = self.find(self._login_frame)
        self.switch_frame_by_element(login_frame)
        self.find(self._login_table).click()
        self.find(self._username).send_keys(username)
        self.find(self._pwd).send_keys(pwd)
        self.find(self._login_btn).click()
        return self

    def _locate_login_frame(self):
        return self.find(self._login_frame)

    def switch_to_login_frame(self):
        self.switch_frame_by_element(self._locate_login_frame())

    def _locate_login_table(self):
        return self.find(self._login_table)

    def click_login_table(self):
        self.click_element(self._locate_login_table())

    def _locate_username_filed(self):
        return self.find(self._username)

    def input_username(self,username):
        self.set_value(self._locate_username_filed(),username)

    def _locate_pwd_filed(self):
        return self.find(self._pwd)

    def input_pwd(self,pwd):
        self.set_value(self._locate_pwd_filed(), pwd)

    def _locate_login_btn(self):
        return self.find(self._login_btn)

    def click_login(self):
        self.click_element(self._locate_login_btn())

    def find_text(self):
        return self.find(self._text).text

    def login_page(self,username, pwd):
        self.switch_to_login_frame()
        self.click_login_table()
        self.input_username(username)
        self.input_pwd(pwd)
        self.click_login()




