#ecoding=utf-8
# author:herui
# time:2020/8/21 17:19
# function: 上传完身份证后，进行纳税信息查询
import logging

import allure
from selenium.webdriver.common.by import By

from src.pages.basepage import BasePage

@allure.feature("纳税信息查询授权页面")
class TaxSearch(BasePage):
    _nsrsbh = (By.ID, "nsrsbh")
    _certCode = (By.ID, "certCode")
    _pwd = (By.ID, "password")
    _agree = (By.NAME, "agree")
    _submit = (By.CSS_SELECTOR, ".submit")

    @allure.step("输入纳税人识别号")
    def input_nsrsbh(self,nsrNum):
        nsrsbh = self.find(self._nsrsbh)
        self.set_value(nsrsbh, nsrNum)

    @allure.step("输入身份证号")
    def input_certCode(self,certCode):
        ID = self.find(self._certCode)
        self.set_value(ID, certCode)

    @allure.step("税务局登录密码")
    def input_pwd(self, pwd):
        password = self.find(self._pwd)
        self.set_value(password,pwd)

    @allure.step("勾选同意")
    def check_box(self):
        self.find(self._agree).click()

    @allure.step("确认授权")
    def submit(self):
        self.find(self._submit).click()

    def tax_search(self,nsrNum, certCode, pwd):
        logging.info("-------进入税务查询授权页面。。。")
        self.input_nsrsbh(nsrNum)
        self.input_certCode(certCode)
        self.input_pwd(pwd)
        self.check_box()
        self.submit()
        return self



