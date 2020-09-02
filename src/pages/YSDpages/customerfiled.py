#ecoding=utf-8
# author:herui
# time:2020/8/29 15:40
# function:
from selenium.webdriver.common.by import By

from src.pages.basepage import BasePage


class CustomerFiled(BasePage):
    _list_box = (By.CLASS_NAME, "android.widget.TextView")
    _el_list = (By.XPATH, "//*[@class='android.widget.TextView' and @index='0']")
    _el_values = (By.XPATH, "//*[@class='android.widget.TextView' and @index='1']")
    _el_values_2 = (By.XPATH, "//*[@class='android.widget.EditText']")
    _contact_Check = (By.CLASS_NAME, "contactCheck")
    _draw_money = (By.XPATH, "//*[@text='立即提款']")
    _list_param = ["name", "ID", "birthday", "expiredate", "sex", "nation", "zzmm", "myPhone", "education", "degree",
                   "houseHold",
                   "homeAddress", "living", "homePhone", "homePostcode", "contactAdr", "contactPc", "maritalStatus",
                   "companyName", "companyAddress", "companyAdr", "companyPhone", "companyType", "companyIndustry",
                   "jobName",
                   "isStaff", "jobType", "companyScale", "jobTitle", "spouseName", "spouseID", "spousePhone",
                   "loanAmount",
                   "exerciseRate", "loanPeriod", "loanUsage", "paymentMethod", "loanAccount"]

    _tv_name = (By.ID, "tv_name")
    _tv_certNo = (By.ID, "tv_certNo")
    _tv_begin_date = (By.ID, "tv_begin_date")
    _tv_end_date = (By.ID, "tv_end_date")
    _tv_sex = (By.ID, "tv_sex")
    _tv_nation = (By.ID, "tv_nation")  # 显示字段内容
    _rl_nation = (By.ID, "rl_nation")  # 可点击，弹出下拉选项
    _rl_political = (By.ID, "rl_political")
    _tv_political = (By.ID, "tv_political")
    _et_mobileTelephone = (By.ID, "et_mobileTelephone")
    _tv_eduExperience = (By.ID, "tv_eduExperience")
    _rl_eduExperience = (By.ID, "rl_eduExperience")
    _rl_education_degree = (By.ID, "rl_education_degree")
    _tv_education_degree = (By.ID, "tv_education_degree")
    _et_NativeAdd = (By.ID, "et_NativeAdd")
    _rl_regionCode = (By.ID, "rl_regionCode")
    _tv_regionCode = (By.ID, "tv_regionCode")
    _et_familyAdd = (By.ID, "et_familyAdd")
    _et_familyZip = (By.ID, "et_familyZip")
    _rl__live_status = (By.ID, "rl__live_status")  # 居住状况
    _tv_familyStatus = (By.ID, "tv_familyStatus")
    _et_familyTel = (By.ID, "et_familyTel")  # 住宅电话
    _et_workCorp = (By.ID, "et_workCorp")  # 单位名称
    _et_workAdd = (By.ID, "et_workAdd")  # 单位详细地址
    _et_workZip = (By.ID, "et_workZip")  # 单位地址邮编
    _et_workTel = (By.ID, "et_workTel")  # 单位电话
    _rl_nature = (By.ID, "rl_nature")  # 单位性质
    _tv_workNature = (By.ID, "tv_workNature")
    _tv_UnitKind = (By.ID, "tv_UnitKind")
    _rl_UnitKind = (By.ID, "rl_UnitKind")
    _rl_Occupation = (By.ID, "rl_Occupation")
    _tv_Occupation = (By.ID, "tv_Occupation")
    _tv_HeadShip = (By.ID, "tv_HeadShip")  # 职务类型
    _rl_HeadShip = (By.ID, "rl_HeadShip")
    _rl_Position = (By.ID, "rl_Position")  # 职称
    _tv_Position = (By.ID, "tv_Position")
    _rl_scaleJudgement = (By.ID, "tv_scaleJudgement")
    _rl_marital_status = (By.ID, "rl_marital_status")  # 婚姻状况
    _tv_marital_status = (By.ID, "rl_marital_status")
    _et_spouse_name = (By.ID, "et_spouse_name")  # 配偶姓名
    _et_spouse_certId = (By.ID, "et_spouse_certId")  # 配偶身份证号
    _et_loan_money = (By.ID, "et_loan_money")  # 贷款金额
    # 执行利率
    _tv_siliver_tax_execute_interestrate = (By.ID, "tv_siliver_tax_execute_interestrate")
    _tv_loan_deadline = (By.ID, "tv_loan_deadline")
    _rl_loan_deadline = (By.ID, "rl_loan_deadline")
    _tv_dkyt = (By.ID, "tv_dkyt")  # 贷款用途
    _rl_dkyt = (By.ID, "rl_dkyt")
    _rl_repayment_way = (By.ID, "rl_repayment_way")
    _tv_repayment_way = (By.ID, "tv_repayment_way")
    _rl_borrow_return_account = (By.ID, "rl_borrow_return_account")
    _tv_borrow_return_account = (By.ID, "tv_borrow_return_account")
    _tv_get_msg_code = (By.ID, "tv_get_msg_code")  # 获取验证码
    _et_mobileVerCode = (By.ID, "et_mobileVerCode")  # 输入验证码
    # 勾选
    _ck_silver_tax_loan_credit = (By.ID, "ck_silver_tax_loan_credit")
    _CheckBox = (By.CLASS_NAME, "android.widget.CheckBox")
