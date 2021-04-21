from appium import webdriver
from time import sleep
from util import BoxDriver
class SearchPage:
    def search(self):
        #打开百度文库
        driver = BoxDriver(browser='App')
        driver.wait(3)
        
        driver.click('id com.baidu.wenku:id/tv_agree')
        driver.wait(9)
        driver.click('id com.baidu.wenku:id/dialog_pic_close')
        driver.wait(8)
        # driver.find_element_by_id('com.baidu.wenku:id/newbie_gift_close_btn').click()
        # sleep(3)
        #单击选择搜索框
        driver.click('id com.baidu.wenku:id/h5_search_edit_text')
        driver.wait(5)
        driver.input('id com.baidu.wenku:id/h5_search_edit_text_inside','高考满分作文')
        driver.wait(2)
        driver.click('id com.baidu.wenku:id/h5_search_operate_text')#点击搜索
        driver.wait(3)
        #获取文本
        elements = driver.locate_elements('c android.view.View')
        texts = [e.text for e in elements]

        #断言
        assert '2015上海高考满分作文(8篇)' in texts
        print(texts)

if __name__ == "__main__":
    SearchPage().search()
