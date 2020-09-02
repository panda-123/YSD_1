#ecoding=utf-8
# author:herui
# time:2020/8/19 16:15
# function:
import logging
import time

import allure
from selenium.webdriver.common.by import By

from src.pages.basepage import BasePage
from src.utils.utils import Utils


class CustomerInfoPage(BasePage):
    _list_box = (By.CLASS_NAME, "android.widget.TextView")
    _el_list = (By.XPATH, "//*[@class='android.widget.TextView' and @index='0']")
    _classNme = "android.widget.ScrollView"
    _el_values = (By.XPATH, "//*[@class='android.widget.TextView' and @index='1']")
    _el_values_2 = (By.XPATH, "//*[@class='android.widget.EditText']")
    _contact_Check = (By.CLASS_NAME, "contactCheck")
    _draw_money = (By.XPATH, "//*[@text='立即提款']")
    _list_param = ["name","ID","birthday","expiredate","sex","nation","zzmm","myPhone","education","degree","houseHold",
                   "homeAddress","living","homePhone","homePostcode","contactAdr","contactPc","maritalStatus",
                   "companyName","companyAddress","companyAdr","companyPhone","companyType","companyIndustry","jobName",
                   "isStaff","jobType","companyScale","jobTitle","spouseName","spouseID","spousePhone","loanAmount",
                   "exerciseRate","loanPeriod","loanUsage","paymentMethod","loanAccount"]

    _tv_name = (By.ID, "tv_name")
    _tv_certNo = (By.ID, "tv_certNo")
    _tv_begin_date = (By.ID, "tv_begin_date")
    _tv_end_date = (By.ID, "tv_end_date")
    _tv_sex = (By.ID, "tv_sex")
    _tv_nation = (By.ID, "tv_nation") #显示字段内容
    _rl_nation = (By.ID, "rl_nation") #可点击，弹出下拉选项
    _rl_political = (By.ID, "rl_political")
    _tv_political = (By.ID, "tv_political")
    _et_mobileTelephone = (By.ID, "et_mobileTelephone") #本人手机号
    _tv_eduExperience = (By.ID, "tv_eduExperience")
    _rl_eduExperience = (By.ID, "rl_eduExperience")
    _rl_education_degree = (By.ID, "rl_education_degree")
    _tv_education_degree = (By.ID, "tv_education_degree")
    _et_NativeAdd = (By.ID, "et_NativeAdd")
    _rl_regionCode = (By.ID, "rl_regionCode")
    _tv_regionCode = (By.ID, "tv_regionCode")
    _et_familyAdd = (By.ID, "et_familyAdd") # 居住地区详细地址
    _et_familyZip = (By.ID, "et_familyZip") #居住地址邮编
    _rl_live_status = (By.ID, "rl_live_status") #居住状况
    _tv_familyStatus = (By.ID, "tv_familyStatus")
    _et_familyTel = (By.ID, "et_familyTel") #住宅电话
    _et_workCorp = (By.ID, "et_workCorp") #单位名称
    _et_workAdd = (By.ID, "et_workAdd") #单位详细地址
    _et_workZip = (By.ID, "et_workZip") #单位地址邮编
    _et_workTel = (By.ID, "et_workTel") #单位电话
    _rl_nature = (By.ID, "rl_nature") #单位性质
    _tv_workNature = (By.ID, "tv_workNature")
    _tv_UnitKind = (By.ID, "tv_UnitKind")
    _rl_UnitKind = (By.ID, "rl_UnitKind")
    _rl_Occupation = (By.ID, "rl_Occupation")
    _tv_Occupation = (By.ID, "tv_Occupation")
    _tv_HeadShip = (By.ID, "tv_HeadShip") #职务类型
    _rl_HeadShip = (By.ID, "rl_HeadShip")
    _rl_Position = (By.ID, "rl_Position") #职称
    _tv_Position = (By.ID, "tv_Position")
    _rl_scaleJudgement = (By.ID, "tv_scaleJudgement")
    _rl_marital_status = (By.ID, "rl_marital_status") #婚姻状况
    _tv_marital_status = (By.ID, "rl_marital_status")
    _et_spouse_name = (By.ID, "et_spouse_name") #配偶姓名
    _et_spouse_certId = (By.ID, "et_spouse_certId") #配偶身份证号
    _et_loan_money = (By.ID, "et_loan_money") #贷款金额
    # 执行利率
    _tv_siliver_tax_execute_interestrate = (By.ID, "tv_siliver_tax_execute_interestrate")
    _tv_loan_deadline = (By.ID, "tv_loan_deadline")
    _rl_loan_deadline = (By.ID, "rl_loan_deadline")
    _tv_dkyt = (By.ID, "tv_dkyt") #贷款用途
    _rl_dkyt = (By.ID, "rl_dkyt")
    _rl_repayment_way = (By.ID, "rl_repayment_way")
    _tv_repayment_way = (By.ID, "tv_repayment_way")
    _rl_borrow_return_account = (By.ID, "rl_borrow_return_account")
    _tv_borrow_return_account = (By.ID, "tv_borrow_return_account")
    _tv_get_msg_code = (By.ID, "tv_get_msg_code") # 获取验证码
    _et_mobileVerCode = (By.ID, "et_mobileVerCode") # 输入验证码
    # 勾选
    _ck_silver_tax_loan_credit = (By.ID, "ck_silver_tax_loan_credit")
    _CheckBox = (By.CLASS_NAME, "android.widget.CheckBox")



    @allure.step("所有字段")
    def filed_name_check(self):
        ele_list = str(self.find(self._list_box).text).split()
        logging.info("页面所有字段：%s", ele_list)
        return ele_list

    def customer_info_filed(self):
        logging.info("----已经进入银税贷申请页面---------")
        # self.print_page_source()
        filed_list = []
        for i in range(0,3):
            self.driver.save_screenshot(Utils.screen_path())
            # ele_list = self.findAll(self._list_box)
            # ele_list = self.driver.find_elements_by_android_uiautomator(
            #     'new UiSelector().className("android.widget.TextView")'
            # )
            ele_list = self.findAll(self._el_list)
            for e in ele_list:
                filed_list.append(e.text)
                logging.info("获取到的字段：%s", e.text)
            # self.print_page_source()
            # self.swipe_up(t=80)
            self.move_to_element("android.widget.ScrollView","婚姻状况")
            time.sleep(1)
        self.swipe_down(t=100)
        logging.info("页面所有字段：%s", filed_list)
        return filed_list


    def customer_info_values(self):
        logging.info("----已经进入银税贷申请页面---------")
        # self.print_page_source()
        filed_values_list = []
        for i in range(0,3):
            self.driver.save_screenshot(Utils.screen_path())
            # ele_list = self.findAll(self._list_box)
            # ele_list = self.driver.find_elements_by_android_uiautomator(
            #     'new UiSelector().className("android.widget.TextView")'
            # )
            ele_list = self.findAll(self._el_values or self._el_values_2)
            for e in ele_list:
                filed_values_list.append(e.text)
                logging.info("获取到的字段：%s", e.text)
            self.print_page_source()
            self.swipe_up(t=100)
            time.sleep(1)
        logging.info("页面所有字段：%s", filed_values_list)


    @allure.step("姓名")
    def name_check(self,name):
        el = self.find(self._tv_name)
        self.set_value(el, name)

    @allure.step("身份证号")
    def ID_check(self,ID):
        el = self.find(self._tv_certNo)
        self.set_value(el, ID)

    @allure.step("出生日期")
    def birthday_check(self, birthday=""):
        el = self.find(self._tv_begin_date)
        self.set_value(el, birthday)

    @allure.step("证件到期日")
    def ID_expire_date_check(self,expireDate):
        el = self.find(self._tv_end_date)
        self.set_value(el, expireDate)

    @allure.step("性别")
    def sex_check(self,sex):
        el = self.find(self._tv_sex)
        self.set_value(el, sex)

    @allure.step("民族")
    def nation_check(self, nation):
        pass

    @allure.step("政治面貌")
    def zzmm_check(self, zzmm):
        pass

    @allure.step("本人手机号码")
    def my_phone_num(self, myPhone):
        self.move_to_element(self._classNme, "本人手机号")
        el = self.find(self._et_mobileTelephone)
        self.set_value(el, myPhone)
        return el.text

    @allure.step("最高学历")
    def education_check(self, education):
        pass

    @allure.step("最高学位")
    def degree_check(self, degree):
        pass

    @allure.step("户籍地址")
    def household_check(self, houseHold):
        self.move_to_element(self._classNme, "户籍地址")
        el = self.find(self._et_NativeAdd)
        self.set_value(el, houseHold)
        return el.text

    @allure.step("居住地区详细地址")
    def homeAddress_check(self, homeAddress):
        self.move_to_element(self._classNme, "居住地区详细地址")
        el = self.find(self._et_familyAdd)
        self.set_value(el, homeAddress)
        return el.text
        pass

    @allure.step("居住状况")
    def living_status_check(self, living):
        pass

    @allure.step("住宅电话")
    def home_phone_check(self, familyTel):
        el = self.find(self._et_familyTel)
        self.set_value(el, familyTel)
        return el.text

    @allure.step("居住地址邮编")
    def home_postcode_check(self, homePostcode):
        pass

    @allure.step("联系地址")
    def contact_address_check(self, contactAdr):
        pass

    @allure.step("联系地址邮编")
    def contact_address_postcode(self, contactPc):
        pass

    @allure.step("婚姻状况")
    def marital_status(self, maritalStatus):
        pass

    @allure.step("单位名称")
    def company_name(self, companyName):
        self.move_to_element(self._classNme, "单位名称")
        el = self.find(self._et_workCorp)
        self.set_value(el, companyName)
        return el.text

    @allure.step("单位详细地址")
    def company_address(self, companyAddress):
        self.move_to_element(self._classNme, "单位详细地址")
        el = self.find(self._et_workAdd)
        self.set_value(el, companyAddress)
        return el.text

    @allure.step("单位地址邮编")
    def company_address_postcode(self, companyAdr):
        pass

    @allure.step("单位电话")
    def company_phone(self, companyPhone):
        pass

    @allure.step("单位性质")
    def company_type(self, companyType):
        pass

    @allure.step("单位所属行业")
    def company_industry(self, companyIndustry):
        pass

    @allure.step("职业名称")
    def job_name(self, jobName):
        pass

    @allure.step("是否我行员工-默认否")
    def is_bank_staff(self, isStaff):
        pass

    @allure.step("职务类型")
    def job_type(self, jobType):
        pass

    @allure.step("公司规模")
    def company_scale(self, companyScale):
        pass

    @allure.step("职称")
    def job_title(self, jobTitle):
        pass

    @allure.step("配偶姓名")
    def Name_of_Spouse(self, spouseName):
        pass

    @allure.step("配偶身份证号码")
    def ID_of_Spouse(self, spouseID):
        pass

    @allure.step("配偶手机号")
    def phone_of_Spouse(self, spousePhone):
        pass

    @allure.step("贷款金额")
    def loan_amount(self,loanAmount):
        pass

    @allure.step("执行利率")
    def exercise_rate(self, exerciseRate):
        pass

    @allure.step("贷款期限")
    def loan_period(self, loanPeriod):
        pass

    @allure.step("贷款用途")
    def loan_usage(self, loanUsage):
        pass

    @allure.step("还款方式")
    def payment_method(self, paymentMethod):
        pass

    @allure.step("借款及还款账户")
    def loan_account(self, loanAccount):
        pass

    @allure.step("勾选")
    def check_box(self):
        el = self.find(self._contact_Check)
        if el.is_selected():
            pass
        else:
            el.click()
            logging.info("已勾选合同")

    @allure.step("立即提款")
    def draw_money(self):
        self.find(self._draw_money).click()










