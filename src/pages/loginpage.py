#ecoding=utf-8
# author:herui
# time:2020/8/24 14:58
# function:手机银行登录页面
import logging

from selenium.webdriver.common.by import By

from src.pages.basepage import BasePage

import time

class LoginPage(BasePage):
    _usr_name = (By.ID, "et_name")
    _usr_pwd = (By.ID, "pge_loginpwd")
    _login_bt = (By.ID, "bt_login")
    _text = (By.XPATH, "//*[@text='预留信息']")


    def login_info(self,usrName,pwd):
        """
        step1:输入用户名
        step2:找到密码输入，调出安全键盘，点击输入密码
        """
        #todo:优化密码输入，明文输入不识别
        logging.info("已经进入登录页面")
        logging.info("开始输入用户名:%s", usrName)
        el = self.find(self._usr_name)
        el.clear()
        el.send_keys(usrName)
        self.set_value(el, usrName)
        logging.info("开始输入密码。。。")
        self.find(self._usr_pwd).click()
        try:
            self.driver.save_screenshot("../../screen/pwd.png")
            self.click_pwd(pwd)
        except:
            time.sleep(5)
        self.find(self._login_bt).click()
        logging.info("已经点击了登录按钮。。。")
        time.sleep(10)

    def get_result(self):
        return self.find(self._text)