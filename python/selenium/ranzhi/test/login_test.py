import os,sys
sys.path.append(os.getcwd())

import unittest
from page.login_page import LoginPage
from base.util import BoxDriver,GetExcel,GetLogger
from parameterized import parameterized


class LoginTest(unittest.TestCase):

    def setUp(self):
        # driver = BoxDriver()
        # self.page = LoginPage(driver)
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(self):
        self.driver = BoxDriver()
        self.page = LoginPage(self.driver)
        self.logger = GetLogger('./report/ranzhi.log')
        self.logger.info('打开浏览器，输入网址完毕')

    @classmethod
    def tearDownClass(self):
        pass

    # for uname, upwd in [('admin','123456'),('tom','123456'),('user0','123456')]:
    #     test_login_success(uname,upwd)
    # 用例参数化
    @parameterized.expand(GetExcel().get(r'config\data.xlsx','login_success'))
    def test_login_success(self,uname,upwd,realname1):
        '''登陆成功功能测试用例'''
        try:
            page = self.page
            page.login(uname,upwd)
            self.logger.info('登陆完毕')
            # 断言
            realname2 = page.get_real_name()
            self.assertEqual(realname1,realname2,'登陆成功测试用例失败！')
            self.logger.info('断言成功')
        except:
            raise NameError('登录失败')
        finally:
            page.logout()
            self.logger.info('退出登录')

        # page.login('tom','123456')
        # # 断言
        # realname = page.get_real_name()
        # self.assertEqual(realname,'admin','登陆成功测试用例失败！')
        # page.logout()

        # page.login('user0','123456')
        # # 断言
        # realname = page.get_real_name()
        # self.assertEqual(realname,'admin','登陆成功测试用例失败！')
        # page.logout()
    
    @parameterized.expand(GetExcel().get(r'config\data.xlsx','login_fail'))
    def test_login_fail(self,uname,upwd,tips1):
        '''登陆失败功能测试用例'''
        try:
            page = self.page
            page.login(uname,upwd)
            self.logger.info('完成登录')
            # 断言
            tips2 = page.get_tips()
            self.assertEqual(tips1,tips2,'登陆失败测试用例失败!')
            # page.login(uname='admin',upwd='123')
            # page.confirm()
            self.logger.info('断言成功')
        except:
            raise NameError('登录失败')#必须抛异常
        finally:
            page.confirm()
            self.logger.info('点击确认按钮')

if __name__ == "__main__":
    unittest.main()