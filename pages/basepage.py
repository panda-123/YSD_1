#ecoding=utf-8
# author:herui
# time:2020/8/12 17:15
# function:
from driver.browerdriver import BrowerDriver

class BasePage(object):
    def __init__(self):
        self.driver = BrowerDriver.getDriver()

    def find(self,locator):
        # 高亮显示元素定位
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].style.background = 'rgb(138,43,266)';",
                                   element)
        return element

    def find_all(self,locator)->[]:
        # 高亮显示元素定位
        element = self.driver.find_elements(*locator)
        self.driver.execute_script("arguments[0].style.background = 'rgb(138,43,266)';",
                                   element)
        return element

    def switch_frame_by_element(self,element):
        self.driver.switch_to.frame(element)

    def get_element_text(self, element):
        return element.text

    def get_table_content(self, table_name):
        return table_name.title()

    def set_value(self, element, value):
        element.clear()
        element.click()
        element.send_keys(value)

    def click_element(self,element):
        element.click()

    def switch_handle(self):
        win_handles = self.driver.window_handles
        self.driver.switch_to.window(win_handles[1])

    def isElementExist(self, element):
        flag = True
        try:
            # self.find(element)
            self.driver.find_element_by_css_selector(element)
            return flag
        except:
            flag = False
            return flag


