from base.util import BoxDriver,BasePage,GetYaml
import yaml

class LoginPage(BasePage):


    config = GetYaml().get(r'config\config.yaml')

    # def __init__(self):
    #     super().__init__(BoxDriver())

    def login(self,uname='admin',upwd='123456'):
        '''登陆操作流程'''
        driver = self.driver

        # 登陆
        driver.input(self.config['LoginPage']['ACCOUNT'],uname)
        driver.input(self.config['LoginPage']['PASSWORD'],upwd)
        driver.click(self.config['LoginPage']['SUBMIT'])

        driver.wait(2)

    def logout(self):
        # 登陆成功后退出
        self.driver.click('p 签退')

    def confirm(self):
        # 登陆失败后确认提示信息
        self.driver.click('x /html/body/div[2]/div/div/div[2]/button')

    def get_real_name(self):
        # 获取登陆以后的真实姓名
        element = self.driver.locate_element('x //*[@id="mainNavbar"]/div/ul[1]/li/a')
        return element.text

    def get_tips(self):
        element = self.driver.locate_element('x /html/body/div[2]/div/div/div[1]/div')
        return element.text
    
if __name__ == "__main__":
    LoginPage(BoxDriver()).login()