from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class BoxDriver:

    '''工具类'''
    def __init__(self,browser='Chrome',separator=' '):
        if browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'Opera':
            self.driver = webdriver.Opera()
        elif browser == 'Safari':
            self.driver = webdriver.Safari()
        else:
            self.driver == webdriver.Ie()
        self.separator = separator
        

    def maximize_window(self):
        '''窗口最大化'''
        self.driver.maximize_window()

    def wait(self,second):
        '''
        休眠指定的时间
        second: 休眠的时间
        '''
        sleep(second)

    def implicitly_wait(self,second=10):
        '''
        隐式等待
        second: 最大等待时间
        '''
        self.driver.implicitly_wait(second)

    def web_driver_Wait(self,selector,timeout=5,poll_frequency=0.5):
        '''
        显示等待
        '''
        locator = self.convert_selector_to_locator(selector)
        return WebDriverWait(self.driver,timeout,poll_frequency).until(EC.presence_of_element_located(locator))

    def get(self,url):
        '''
        打开网页
        url : 网页的地址
        '''
        self.driver.get(url)

    def convert_selector_to_locator(self,selector):
        '''
        将自定义的selector转换为selenium标准定位格式
        'id kw' -> (By.ID,'kw')
        selector: 自定义元素定位方式
        '''
        args = selector.split(self.separator)
        by = args[0].strip()    #定位方式
        value = args[1].strip() #定位值
        if by == 'id' or by == 'i':
            locator = (By.ID,value)
        elif by == 'name' or by == 'n':
            locator = (By.NAME,value)
        elif by == 'class' or by == 'c':
            locator = (By.CLASS_NAME,value)
        elif by == 'xpath' or by == 'x':
            locator = (By.XPATH,value)
        elif by == 'link_text' or by == 'l':
            locator = (By.LINK_TEXT,value)
        elif by == 'partial_link_text' or by == 'p':
            locator = (By.PARTIAL_LINK_TEXT,value)
        elif by == 'tag_name' or by == 't':
            locator = (By.TAG_NAME,value)
        elif by == 'css_selector' or by == 'cs':
            locator = (By.CSS_SELECTOR,value)
        else:
            raise NameError('请输入一个合法的定位方式！')

        return locator

    def locate_element(self,selector):
        '''
        定位单个元素
        selector: 自定义元素定位方式
        '''
        locator = self.convert_selector_to_locator(selector)
        # return self.driver.find_element(locator[0],locator[1])
        return self.driver.find_element(*locator)

    def locate_elements(self,selector):
        '''
        定位多个个元素
        selector: 自定义元素定位方式
        '''
        locator = self.convert_selector_to_locator(selector)
        # return self.driver.find_element(locator[0],locator[1])
        return self.driver.find_elements(*locator)

    def click(self,selector):
        '''
        对元素进行单击操作
        selector: 自定义元素定位方式
        '''
        self.locate_element(selector).click()

    def input(self,selector,text):
        '''
        向元素发送信息
        selector: 自定义元素定位方式
        '''
        self.locate_element(selector).send_keys(text)

    def switch_to_frame(self,selector):
        '''
        进入iframe
        '''
        frame = self.locate_element(selector)
        self.driver.switch_to.frame(frame)

    def select_by_index(self,selector,index):
        '''
        根据index选择下拉选择框的选项
        '''
        # 选中select元素
        select = self.locate_element(selector)
        # 使用Select进行处理
        options = Select(select)
        # 选择选项
        options.select_by_index(index) # 根据下标来选中

    def select_by_value(self,selector,value):
        '''
        根据value选择下拉选择框的选项
        '''
        # 选中select元素
        select = self.locate_element(selector)
        # 使用Select进行处理
        options = Select(select)
        # 选择选项
        options.select_by_value(value) 

    def select_by_visible_text(self,selector,visible_text):
        '''
        根据visible_text选择下拉选择框的选项
        '''
        # 选中select元素
        select = self.locate_element(selector)
        # 使用Select进行处理
        options = Select(select)
        # 选择选项
        options.select_by_visible_text(visible_text)

    def close(self):
        '''
        关闭当前窗口
        '''
        self.driver.close()

    def quit(self):
        '''
        退出浏览器
        '''
        self.driver.quit()


if __name__ == "__main__":
    BoxDriver()


