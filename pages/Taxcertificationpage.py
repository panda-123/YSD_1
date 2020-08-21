#ecoding=utf-8
# author:herui
# time:2020/8/19 10:44
# function:
import logging
import time

import allure
from selenium.webdriver.common.by import By

from pages.basepage import BasePage
from pages.letterofauthorization import LetterOfAuthorization

from pages.uploadIDcard import UploadIDCard

@allure.feature("税务认证页面")
class TaxCertificationPage(BasePage):
    _back_btn = (By.ID, "backView")
    _list_box = (By.CLASS_NAME, "list-box")
    _credit_Num = (By.ID, "creditNum")
    _legal_Name = (By.ID, "legalName")
    _legal_CardNo = (By.ID, "legalCardNo")
    _tele_No = (By.ID, "teleNo")
    _person_No = (By.ID, "personNo")
    _contact_Check = (By.CLASS_NAME, "contactCheck")
    # _submit = (By.XPATH, "//*[@text='立即申请']")
    _jump_to_letter = (By.XPATH, "//*[@text='我已阅读并知晓']")
    _submit = (By.CLASS_NAME, "apply-btn")
    _popup_content = (By.CLASS_NAME, "popup-content")
    _popup_msg = (By.CLASS_NAME, "popup-msg")
    _popup_sure = (By.ID, "popup-sure")
    _popup_title = (By.CLASS_NAME, "popup-title")
    _title_text = (By.XPATH, "//*[@text='温馨提示']")
    _close_btn = (By.CLASS_NAME, "close-btn")
    _input_Code = (By.ID, "vertifyCode")
    _vertify_Code = (By.XPATH, "//*[@text='短信验证码']")
    # _apply_btn = (By.XPATH, "//*[@text='提交']")
    _apply_btn = (By.CSS_SELECTOR, ".verification-btn")
    text = ""

    @allure.step("获取页面所有字段")
    def check_filed_name(self):
        """
        1、获取页面字段值；
        2、按照\n分割为每个字段
        :return: 字段值
        """
        ele_list = str(self.find(self._list_box).text).split()
        return ele_list

    @allure.step("社会统一信用代码")
    def input_creditNum(self,creditNum):
        self.set_value(self.find(self._credit_Num), creditNum)

    @allure.step("法人姓名")
    def input_legalName(self,legalName):
        self.set_value(self.find(self._legal_Name), legalName)

    @allure.step("法人身份证")
    def input_legalCardNo(self,legalCardNo):
        self.set_value(self.find(self._legal_CardNo), legalCardNo)

    @allure.step("联系人手机号码")
    def input_teleNo(self, teleNo):
        self.set_value(self.find(self._tele_No),teleNo)

    @allure.step("营销人员编号")
    def input_personNo(self, personNo=""):
        self.set_value(self.find(self._person_No), personNo)

    @allure.step("返回")
    def back_btn(self):
        #todo:返回上一个页面
        self.find(self._back_btn).click()
        return self

    @allure.step("勾选")
    def check_box(self):
        el = self.find(self._contact_Check)
        if el.is_selected():
            pass
        else:
            el.click()
            logging.info("已勾选合同")
            # print("已勾选合同")

    @allure.step("输入验证码")
    def input_vertify_code(self, vCode="123456"):
        """
        1、如果信息正确，进入输入短信验证码页面
        2、输入短信验证码，如果正确，通过；如果错误，确认，返回
        3、如果信息错入，弹窗提示，关闭弹窗
        :param vCode:
        :return:
        """
        try:
            if self.find(self._popup_title).text == "温馨提示":
                logging.info("直接报错，不到输入短信界面------------------")
                el3 = self.find(self._popup_msg)
                self.text = el3.text
                return self.find(self._popup_sure).click()
            else:
                self.set_value(self.find(self._input_Code), vCode)
                self.find(self._apply_btn).click()
                time.sleep(2)
                self.close_popup()
        except:
            pass


    @allure.step("关闭短信验证码弹窗")
    def close_popup(self):
        #todo:待优化,输入错误后,再次输入正确验证码
        """
        1、输入验证码之后，如果不对，弹出提示
        2、获取提示内容，点击确定
        3、关闭短信输入框
        """
        if self.find(self._popup_title).text == "温馨提示":
            logging.info("短信验证码错误，弹出温馨提示---------")
            el4 = self.find(self._popup_msg)
            self.text = el4.text
            self.find(self._popup_sure).click()
            return self.find(self._close_btn).click()
        else:
            logging.info("短信验证码正确，进入下个页面")
            return UploadIDCard()

    @allure.step("提交")
    def submit(self):
        self.find(self._submit).click()
        logging.info("点击提交")
        self.input_vertify_code()

    def check_input(self, creditNum, legalName, legalCardNo, teleNo,personNo=""):
        self.input_creditNum(creditNum)
        self.input_legalName(legalName)
        self.input_legalCardNo(legalCardNo)
        self.input_teleNo(teleNo)
        self.input_personNo(personNo)
        self.check_box()
        self.submit()
        return self

    def to_letter(self):
        self.find(self._jump_to_letter).click()
        return LetterOfAuthorization()

    def get_result(self):
        print(self.text)
        return self.text

