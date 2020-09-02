#ecoding=utf-8
# author:herui
# time:2020/8/21 17:06
# function:税务认证信息填写完成后，进入该页面上传身份证
import logging

from selenium.webdriver.common.by import By

from src.pages.YSDpages.Taxsearch import TaxSearch
from src.pages.basepage import BasePage
from src.utils.utils import Utils

class UploadIDCard(BasePage):
    _upload_A = (By.CSS_SELECTOR, ".upload-left")
    _upload_B = (By.CSS_SELECTOR, ".upload-right")
    _apply_btn = (By.CSS_SELECTOR, ".apply-btn")
    _card_front = (By.XPATH, "//*[@text='card_front']")
    _card_behind = (By.XPATH, "//*[@text='card_behind']")


    def upload_ID_A(self):
        #todo:待完善
        logging.info("上传身份证正面")
        # self.find(self._upload_A).click()
        self.find(self._card_front).click()
        self.print_page_source()


    def upload_ID_B(self):
        logging.info("上传身份证背面")
        # self.find(self._upload_B).click()
        self.find(self._card_behind).click()
        self.print_page_source()

    def submit(self):
        file_name = Utils.screen_path()
        self.driver.save_screenshot(file_name)
        self.find(self._apply_btn).click()
        logging.info("点击提交，进入  税务查询页面")

    def upload_ID(self):
        logging.info("-------进入上传身份证页面。。。")
        self.upload_ID_A()
        self.upload_ID_B()
        self.submit()
        return TaxSearch()



