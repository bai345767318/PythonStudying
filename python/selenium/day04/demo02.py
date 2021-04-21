from selenium import webdriver
from selenium.webdriver.support.select import Select
import random
from time import sleep

class AddProject:

    def add_project(self,uname='admin',upwd='123456'):
        try:
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.implicitly_wait(10)
            driver.get('http://localhost:8448/ranzhi/www/sys/user-login.html')

            # 登陆
            driver.find_element_by_id('account').send_keys(uname)
            driver.find_element_by_id('password').send_keys(upwd)
            driver.find_element_by_id('submit').click()

            driver.find_element_by_id('s-menu-3').click()

            # 进入iframe3
            iframe3 = driver.find_element_by_id('iframe-3')
            driver.switch_to.frame(iframe3)

            for i in range(1,6):
                # 点击 "添加区块"
                driver.find_element_by_xpath('//*[@id="dashboard"]/div[2]/a').click()
                #点击"区块"下拉框
                driver.find_element_by_xpath('//*[@id="blocks"]').click()
                # 选择任务列表
                select1 = driver.find_element_by_id('blocks')
                # select1 = driver.find_element_by_xpath('//*[@id="blocks"]/option[2]')
                blocks = Select(select1)
                blocks.select_by_value('task')

                # 选择名称
                driver.find_element_by_id('title').send_keys('区块%d'%i)

                # 外观
                select2 = driver.find_element_by_id('grid')
                grids = Select(select2)
                grids.select_by_index(random.randint(0,5))

                # 颜色
                driver.find_element_by_xpath('//*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button').click()
                driver.find_element_by_xpath('//*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%d]'%random.randint(1,6)).click()

                # 类型
                driver.find_element_by_xpath('//*[@id="paramstype_chosen"]/a/span').click()
                driver.find_element_by_xpath('//*[@id="paramstype_chosen"]/div/ul/li[%d]'%random.randint(1,5)).click()

                # 数量
                driver.find_element_by_id('params[num]').clear()
                driver.find_element_by_id('params[num]').send_keys(random.randint(1,100))

                # 排序
                driver.find_element_by_xpath('//*[@id="paramsorderBy_chosen"]/a/span').click()
                driver.find_element_by_xpath('//*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%random.randint(1,6)).click()

                # 状态
                driver.find_element_by_xpath('//*[@id="paramsstatus_chosen"]/ul').click()
                driver.find_element_by_xpath('//*[@id="paramsstatus_chosen"]/div/ul/li[%d]'%random.randint(1,6)).click()

                driver.find_element_by_id('submit').click()
                sleep(2)
        except Exception as e:
            print(e)
        finally:
            sleep(3)
            driver.close()

if __name__ == "__main__":
    AddProject().add_project()