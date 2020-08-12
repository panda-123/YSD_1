#ecoding=utf-8
# author:herui
# time:2020/8/12 17:15
# function:

class BasePage():
    def __init__(self):
        self.driver = ''
        pass

    def extend_find_element(self):
        pass

    def get_element_text(self, element):
        return element.text

    def get_table_content(self, tabel_name):
        pass