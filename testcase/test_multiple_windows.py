#ecoding=utf-8
# author:herui
# time:2020/8/6 17:23
# function:

from selenium import webdriver
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_douban_multiple_windows():
    chrome_option = webdriver.ChromeOptions()
    # chrome_option.add_argument('--disable-infobars')
    extset = ['enable-automation', 'ignore-certificate-errors']
    chrome_option.add_experimental_option("excludeSwitches", extset)
    driver = webdriver.Chrome(options=chrome_option)
    chrome_option.add_experimental_option("useAutomationExtension", False)
    driver.get("https://www.douban.com/")
    login_frame = driver.find_element_by_tag_name("iframe")
    driver.execute_script("arguments[0].style.background = 'rgb(138,43,226)';", login_frame)
    driver.switch_to.frame(login_frame)
    forgot_pwd_locator = (By.CLASS_NAME, "account-form-link")
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(forgot_pwd_locator))

    driver.find_element_by_class_name("account-form-link").click()
    win_handles = driver.window_handles
    print("*"*20)
    print("windows_handles:"+ str(win_handles))
    driver.switch_to.window(win_handles[1])
    time.sleep(5)
    assert driver.title == "帐号 使用帮助"
