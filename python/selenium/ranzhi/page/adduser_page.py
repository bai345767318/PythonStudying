from selenium import webdriver
from selenium.webdriver.support.select import Select
import random
from util import BoxDriver,BasePage
from login_page import LoginPage

class AddUser(LoginPage):
    # def __init__(self):
    #     super().__init__(BoxDriver())

    def add_user(self,uname='admin',upwd='123456'):
        driver = self.driver

        # 添加成员
        driver.click('x //*[@id="s-menu-superadmin"]/button')


        # 切换到frame中
        driver.switch_to_frame('id iframe-superadmin')

        # 点击"添加成员"
        driver.click('p 添加成员')

        for i in range(11,16):
            username = 'user%d'%i

            # 添加成员
            driver.input('i account', username)
            driver.input('id realname', username)
            # 性别
            driver.click('id genderm' if i%2==0 else 'id genderf')

            # 选择部门
            driver.select_by_index('id dept',random.randint(1,6)) # 根据下标来选中

            # 选择角色
            driver.select_by_index('id role', random.randint(1,16)) # 根据下标来选中

            # 密码
            driver.input('id password1', '123456')
            driver.input('id password2', '123456')

            driver.input('id email','%s@163.com'%username)

            # 保存
            driver.click('id submit')

            driver.wait(3)

            # 跳转到最后一页
            driver.input('id _pageID', '10000')
            driver.click('id goto')
            driver.wait(1)

            # 断言
            accounts = driver.locate_elements('xpath /html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[3]')
            account = accounts[-1]
            assert account.text == username

            # 添加下一个成员

            driver.click('xpath /html/body/div/div/div/div[1]/div/div[2]/a[1]')

        driver.close()

if __name__ == "__main__":
    driver = BoxDriver()
    addUser = AddUser(driver)
    addUser.login()
    addUser.add_user()