#ecoding=utf-8
# author:herui
# time:2020/8/6 17:23
# function:

from selenium import webdriver
import pytest
import time

def test_douban_multiple_windows():
    driver = webdriver.Chrome()
    driver.get("https://www.douban.com/")
    login_frame = driver.find_element_by_tag_name("iframe")
    driver.switch_to.frame(login_frame)
    driver.find_element_by_class_name("account-form-link").click()
    win_handles = driver.window_handles
    print("*"*20)
    print("windows_handles:"+ str(win_handles))
    driver.switch_to.window(win_handles[1])
    time.sleep(5)
    assert driver.title == "帐号 使用帮助"
