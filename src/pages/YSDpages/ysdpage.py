#ecoding=utf-8
# author:herui
# time:2020/8/25 14:42
# function:
import logging
import time

from selenium.webdriver.common.by import By

from src.pages.YSDpages.Taxcertificationpage import TaxCertificationPage
from src.pages.YSDpages.myloan import MyLoan
from src.pages.basepage import BasePage


class YSDPage(BasePage):
    # _tax_loan_apply = (By.ID, "btn_silver_tax_loan_apply")
    _tax_loan_apply = (By.XPATH, "//*[@text='立即申请']")
    # _tax_my_loan = (By.ID, "btn_silver_tax_my_loan")
    _tax_my_loan = (By.XPATH, "//*[@text='我的贷款']")

    def loan_apply(self):
        self.find(self._tax_loan_apply).click()
        self.find(self._tax_loan_apply).click()
        logging.info("-------已点击  立即申请。。。。。")
        time.sleep(2)
        print("手动点击立即申请吧~~~~~，如果还在立即申请界面")
        return TaxCertificationPage()

    def my_loan(self):
        self.find(self._tax_my_loan).click()
        self.find(self._tax_my_loan).click()
        logging.info("已点击：我的贷款")
        time.sleep(6)
        return MyLoan()