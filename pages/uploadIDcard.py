#ecoding=utf-8
# author:herui
# time:2020/8/21 17:06
# function:税务认证信息填写完成后，进入该页面上传身份证
from selenium.webdriver.common.by import By

from pages.basepage import BasePage


class UploadIDCard(BasePage):
    _upload_A = (By.CSS_SELECTOR, ".upload-left")
    _upload_B = (By.CSS_SELECTOR, ".upload-right")
    _apply_btn = (By.CSS_SELECTOR, ".apply-btn")


    def upload_ID_A(self):
        self.find(self._upload_A).click()

        pass
    def upload_ID_B(self):
        pass

    def submit(self):
        self.find(self._apply_btn).click()
        return self



