#ecoding=utf-8
# author:herui
# time:2020/8/19 10:47
# function:

import pytest

from driver.browerdriver import BrowerDriver
from pages.Taxcertificationpage import TaxCertificationPage
import yaml
import allure

@allure.feature("测试税务认证页面")
class TestTaxCertify():

    def setup_class(self):
        self.page = TaxCertificationPage()

    def teardown_class(self):
        pass
        # BrowerDriver.driver.close()


    @allure.story("字段检查核对")
    @allure.title("税务认证页面字段检查")
    @pytest.mark.parametrize("result",yaml.load(open(r"E:\Hogwarts\python\YSD\data\data.yml", encoding="UTF-8")))
    def test_taxcertifypage(self,result):
        assert self.page.check_filed_name() == result

    @allure.title("字段输入场景：{step}")
    @allure.story("字段输入")
    @allure.step("字段测试：社会统一信用代码")
    @pytest.mark.parametrize("step,creditNum,legalName,legalCardNo,teleNo,personNo",
                             yaml.load(open(r"E:\Hogwarts\python\YSD\data\creditNum.yml", encoding="UTF-8")))
    def test_input_creditNum(self,step,creditNum,legalName,legalCardNo,teleNo,personNo):
        self.page.check_input(creditNum,legalName,legalCardNo,teleNo,personNo)
        print(step)
        assert self.page.get_result() == ""



