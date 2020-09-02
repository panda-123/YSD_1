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

@allure.feature("YSD-我的贷款")
class TestLogin(object):

    def setup_class(self):
        AppDriver.initDriver()
        self.home = HomePage()
        self.login = self.home.to_mine().to_login().login_info("6230730030796412","111111")
        self.myLoan = self.home.to_homepage().to_YSD().my_loan().apply_loan()

    @pytest.mark.run(order=1)
    @allure.story("页面字段")
    @allure.title("获取客户信息字段")
    def test_customer_info_filed(self):
        self.myLoan.customer_info_filed()
        assert 1==1

    @pytest.mark.run(order=2)
    @allure.story("字段数输入测试")
    @allure.story("户籍地址")
    @allure.title("户籍地址")
    @pytest.mark.parametrize("step,name",
                    yaml.safe_load(open(r"E:\Hogwarts\python\YSD\data\customerInfo\name.yml", encoding="UTF-8")))
    def test_customer_info1(self,step,name):
        print(step)
        logging.info("执行案例:%s",step)
        assert self.myLoan.household_check(name) == name

    @pytest.mark.run(order=3)
    @allure.story("客户居住地区地址")
    @allure.title("客户居住地区地址")
    @pytest.mark.parametrize("step,name",
                             yaml.safe_load(
                                 open(r"E:\Hogwarts\python\YSD\data\customerInfo\name.yml", encoding="UTF-8")))
    def test_customer_info2(self, step, name):
        print(step)
        logging.info("执行案例:%s", step)
        assert self.myLoan.homeAddress_check(name) == name

    @pytest.mark.run(order=4)
    @allure.story("本人手机号")
    @allure.title("本人手机号")
    @pytest.mark.parametrize("step,num",
                             yaml.safe_load(
                                 open(r"E:\Hogwarts\python\YSD\data\customerInfo\num.yml", encoding="UTF-8")))
    def test_customer_info3(self, step, num):
        print(step)
        logging.info("执行案例:%s", step)
        assert self.myLoan.my_phone_num(num) == num

    @pytest.mark.run(order=5)
    @allure.story("单位名称")
    @allure.title("单位名称")
    @pytest.mark.parametrize("step,name",
                             yaml.safe_load(
                                 open(r"E:\Hogwarts\python\YSD\data\customerInfo\name.yml", encoding="UTF-8")))
    def test_customer_info4(self, step, name):
        print(step)
        logging.info("执行案例:%s", step)
        assert self.myLoan.company_name(name) == name

    @pytest.mark.run(order=6)
    @allure.story("单位详细地址")
    @allure.title("单位详细地址")
    @pytest.mark.parametrize("step,name",
                             yaml.safe_load(
                                 open(r"E:\Hogwarts\python\YSD\data\customerInfo\name.yml", encoding="UTF-8")))
    def test_customer_info4(self, step, name):
        print(step)
        logging.info("执行案例:%s", step)
        assert self.myLoan.company_address(name) == name



