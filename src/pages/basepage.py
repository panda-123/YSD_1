#ecoding=utf-8
# author:herui
# time:2020/8/24 15:00
# function: 公共方法
import logging
import time

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from src.driver.appdriver import AppDriver
from lxml import etree

from src.utils.utils import Utils

class BasePage(object):
    def __init__(self):
        self.driver = AppDriver.getDriver()
    # 黑名单，处理随时可能的弹窗
    # _blank_words = [(By.XPATH, "//*[text='好的']"),
    #                 (By.XPATH, "//*[@text='下次再说']"),
    #                 (By.XPATH, "//*[@text='同意']"),
    #                 (By.ID, "btn_diss")]
    _blank_words = [ "//*[@text='取消']", "//*[text='好的']", "//*[@text='下次再说']", "//*[@text='同意']",
                    "//*[text='确定']"]
    @classmethod
    def byAttr(cls, text=None, id=None):
        text_selector = ""
        if text is not None:
            text_selector = "@text='" + text + "'"

        if id is not None:
            id_selector = "contains(@resource-id, '" + id + "')"
            return "//*[" + text_selector + " and " + id_selector + "]"
        else:
            return "//*[" + text_selector + "]"

    @classmethod
    def byUiSel(cls, text=None, id=None):
        text_selector = ""
        if text is not None:
            text_selector = "@text='" + text + "'"

        if id is not None:
            id_selector = "contains(@resource-id, '" + id + "')"
            # return "//*[" + text_selector + " and " + id_selector + "]"
            return (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("'+id+'").text("'+text+'")')
        else:
            return (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("'+text+'")')

    def exception_handle(self):
        # 加todo，会提示相关内容
        #todo:优化
        for w in self._blank_words:
            elements = self.driver.find(w)
            if len(elements) > 0:
                elements[0].click()
                return self.driver.find(w)

    def exception_handle1(self):
        # todo:优化弹框处理逻辑，发现toast,自动发现兼容性问题等
        page_source = self.driver.page_source
        # print(page_source)
        page_source = bytes(bytearray(page_source, encoding='utf-8'))
        file_name = Utils.screen_path()
        self.driver.save_screenshot(file_name)
        logging.info("可能有异常弹窗，截图了")
        # xml = etree.XML(page_source)
        # xml = etree.XML(str(page_source)).encode("utf-8")
        xml = etree.XML(page_source)
        for w in self._blank_words:
            if len(xml.xpath(w))>0:
                logging.info("%s, %s:", w,xml.xpath(w))
                self.driver.find_element_by_xpath(w).click()

    def findBy(self,by=By.ID, value = None):
        try:
            return self.driver.find_element(by, value)
        except:
            # 以下为比较粗暴的处理方式，后续需要优化
            self.exception_handle1()
            return self.driver.find_element(by, value)

    def find(self,locate)->WebElement:
        # ->表示指定返回类型
        # 返回的内容若无类型，则无法自动识别其特性,比如 click等
        return self.findBy(*locate)

    def findAll(self,locate) -> []:
        # 返回列表类型
        return self.driver.find_elements(*locate)

    def longPress(self, el, duration=1):
        center_x = el.location.get('x') *1.05
        center_y = el.location.get('y') *1.05
        duration = duration * 3000
        # center = (center_x, center_y)
        # TouchAction(Appium.driver).tap(center_x,center_y).perform()
        self.driver.swipe(center_x,center_y,center_x,center_y,duration)
        return self

    def click_pwd(self,pwd,im="../screen/pwd.png"):
        pwd = Utils.get_pwd_pos(im, pwd)
        for e in pwd:
            self.driver.tap(e)
        return self

    def set_value(self, element, value):
        element.clear()
        # element.click()
        element.send_keys(value)

    def input_value(self,element):
        #todo:待完善,显示等待直到输入的值正确
        if self.find(element).text != "":
            self.find(element).send_keys()

    def print_page_source(self):
        page_source = self.driver.page_source
        logging.info("当前page_source:%s", page_source)

    def switch_to_webview(self):
        contexts = self.driver.contexts
        logging.info("切换前的content:%s", contexts)
        self.print_page_source()
        self.driver.switch_to.context(contexts[-1])
        current_context = self.driver.current_context
        print(current_context)
        logging.info("当前context：%s", current_context)
        self.print_page_source()

    def switch_to_app(self):
        self.driver.switch_to.context('NATIVE_APP')

    def wait_input(self, element, text=""):
        while True:
            if element.text != text and element.text != "":
                break
            else:
                time.sleep(5)
                continue
        return self

    def swipe_up(self,t=300,n=1):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.75  # 起点y坐标
        y2 = s['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_down(self,t=500,n=1):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.5  # 起点y坐标
        y2 = s['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_left(self,t=500,n=1):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.75
        y1 = s['height'] * 0.5
        x2 = s['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipe_right(self,t=500,n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def scroll(self, origin_el, destination_el, duration=100):
        return self.driver.scroll(origin_el, destination_el,duration)

    def move_to_element(self,className,text):
        element =  self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().className("'+ className +'").instance(0)).scrollIntoView(new UiSelector().text("' + text +'"))')
        return element





