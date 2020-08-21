#ecoding=utf-8
# author:herui
# time:2020/8/12 17:23
# function:
from selenium import webdriver

class BrowerDriver(object):

    driver: webdriver = None
    "@type driver: WebDriver"

    @classmethod
    def getDriver(cls):
        chrome_option = webdriver.ChromeOptions()
        # chrome_option.add_argument('--disable-infobars')
        # 关闭“请停用以开发者模式运行的扩展程序”信息
        extset = ['enable-automation', 'ignore-certificate-errors']
        chrome_option.add_experimental_option("excludeSwitches", extset)
        # 不显示 Chrome正在受自动测试软件的控制
        chrome_option.add_experimental_option("useAutomationExtension", False)
        # 设置chrome不显示弹窗：保存密码
        prefs = {"": ""}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        chrome_option.add_experimental_option("prefs", prefs)
        cls.driver = webdriver.Chrome(options=chrome_option)

        cls.driver.get("https://boltest2.lccb.com.cn:18006/perbank/EliteLoan/BankEasyLoan/taxCertify.html")
        # 隐式等待10s，全局等待
        cls.driver.implicitly_wait(10)
        return cls.driver