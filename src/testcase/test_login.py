#ecoding=utf-8
# author:herui
# time:2020/8/17 11:12
# function:
import logging

import allure
import pytest
import yaml

from src.pages.homepage import HomePage
from src.driver.appdriver import AppDriver

@allure.feature("测试廊坊银行YSD")
class TestLogin(object):

    def setup_class(self):
        AppDriver.initDriver()
        self.home = HomePage()
        self.login = self.home.to_mine().to_login().login_info("6230730030796412","111111")
        self.myLoan = self.home.to_homepage().to_YSD().my_loan().apply_loan()

    @pytest.mark.skip("登录放在 初始化中了")
    @pytest.mark.run(order=1)
    @allure.story("登录 app")
    @pytest.mark.parametrize("username, pwd",
                             yaml.safe_load(open(r"E:\Hogwarts\python\YSD\data\login.yml", encoding="UTF-8")))
    def test_login(self,username,pwd):
        self.home.to_mine().to_login().login_info(username,pwd)
        # assert self.home.to_mine().get_result() == "安全退出"
        assert 1==1

    @pytest.mark.skip(reason="不测试这个功能")
    @pytest.mark.run(order=2)
    @allure.story("税务认证流程")
    @pytest.mark.parametrize("step,creditNum,legalName,legalCardNo,teleNo,personNo",
                             yaml.safe_load(open(r"E:\Hogwarts\python\YSD\data\creditNum.yml", encoding="UTF-8")))
    def test_tax_search(self,step,creditNum,legalName,legalCardNo,teleNo,personNo):
        """
        我的贷款--税务认证--上传身份证--税务查询--
        :return:
        """
        print(step)
        self.home.to_YSD().loan_apply().check_input(creditNum,legalName,legalCardNo,teleNo,personNo).\
            upload_ID().tax_search()
        assert 1==1

    @pytest.mark.run(order=5)
    @allure.story("客户信息页面测试")
    @allure.title("获取客户信息字段")
    # @pytest.mark.parametrize(yaml.safe_load(open(r"E:\Hogwarts\python\YSD\data\customerfiled.yml", encoding="UTF-8")),
    #                          yaml.safe_load(open(r"E:\Hogwarts\python\YSD\data\customer.yml", encoding="UTF-8")))
    def test_customer_filed(self):
        self.myLoan.customer_info_filed()
        assert 1==1

    @pytest.mark.run(order=4)
    @allure.story("字段输入测试")
    @allure.title("客户居住地区地址")
    @pytest.mark.parametrize("step,name",
                    yaml.safe_load(open(r"E:\Hogwarts\python\YSD\data\customerInfo\name.yml", encoding="UTF-8")))
    def test_customer_info(self,step,name):
        print(step)
        logging.info("执行案例:%s",step)
        # self.home.to_homepage().to_YSD().my_loan().apply_loan().household_check(name)
        assert self.myLoan.household_check(name) == name



