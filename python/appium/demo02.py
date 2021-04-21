import unittest
from util import BoxDriver,GetExcel
from search_page import SearchPage
from parameterized import parameterized

class Search(unittest.TestCase):

    def setUp(self):
        
        pass
    def tearDown(self):
        pass
        # self.driver.click('id com.baidu.wenku:id/h5_search_edit_text_inside')#点击搜索框
        # # self.driver.clear()
        # self.driver.click('id com.baidu.wenku:id/h5_search_clear_word')#点击x键
        
        # self.driver.close()
    @classmethod
    def setUpClass(self):
        #打开百度文库
        driver = BoxDriver(browser='App')
        driver.wait(10)
        driver.click('id com.baidu.wenku:id/tv_agree')
        driver.wait(10)
        driver.click('id com.baidu.wenku:id/dialog_pic_close')
        driver.wait(10)
        # driver.click('id com.baidu.wenku:id/newbie_gift_close_btn')
        # driver.wait(3)
        self.driver = driver

        self.driver.click('id com.baidu.wenku:id/h5_search_edit_text')
    @classmethod
    def tearDownClass(self):
        pass
        # self.driver.wait(3)
        # self.driver.close()
    @parameterized.expand(GetExcel().get(r'appium\search_page.xlsx','search_success'))
    def test_search_success(self,t1):
        try:
            self.driver.wait(10)
            self.driver.input('id com.baidu.wenku:id/h5_search_edit_text_inside',t1)
            self.driver.wait(5)
            self.driver.click('id com.baidu.wenku:id/h5_search_operate_text')#点击搜索
            self.driver.wait(10)
            #获取文本
            elements = self.driver.locate_elements('c android.view.View')
            texts = [e.text for e in elements]
            #断言
            
            assert t1 in texts
            print(texts)
        except Exception as e:
            print(e)
        finally:
            self.driver.click('id com.baidu.wenku:id/h5_search_edit_text_inside')#点击搜索框
            self.driver.click('id com.baidu.wenku:id/h5_search_clear_word')#点击x键

    # def test_search_fail(self):
    #     try:
    #         self.driver.click('id com.baidu.wenku:id/h5_search_edit_text')
    #         self.driver.wait(5)
    #         self.driver.input('id com.baidu.wenku:id/h5_search_edit_text_inside','高考满分作文')
    #         self.driver.wait(5)
    #         self.driver.click('id com.baidu.wenku:id/h5_search_operate_text')#点击搜索
    #         self.driver.wait(5)
    #         #获取文本
    #         elements = self.driver.locate_elements('c android.view.View')
    #         texts = [e.text for e in elements]
    #         #断言
    #         assert '2015上海高考满分作文(8篇)' not in texts
    #         print('测试查找失败用例成功')
    #     except Exception as e:
    #         print(e) 


if __name__ == "__main__":
    unittest.main()