from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import random

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://localhost/ranzhi/www/sys/user-login.html')

    # 登陆
    driver.find_element_by_id('account').send_keys('admin')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()

    # 添加成员
    driver.find_element_by_xpath('//*[@id="s-menu-superadmin"]/button').click()

    # 切换到frame中
    frame = driver.find_element_by_id('iframe-superadmin')
    driver.switch_to.frame(frame)

    # 点击"添加成员"
    driver.find_element_by_partial_link_text('添加成员').click()

    for i in range(8,20):
        username = 'user%d'%i

        # 添加成员
        driver.find_element_by_id('account').send_keys(username)
        driver.find_element_by_id('realname').send_keys(username)
        # 性别
        driver.find_element_by_id('genderm' if i%2==0 else 'genderf').click()

        # 选中select元素
        select1 = driver.find_element_by_id('dept')
        # 使用Select进行处理
        depts = Select(select1)
        # 选择部门
        depts.select_by_index(random.randint(1,6)) # 根据下标来选中
        # sleep(2)
        # depts.select_by_value('11') # 根据value属性的值来选择
        # sleep(2)
        # depts.select_by_visible_text('/后勤部') # 根据可见文本来选择 
        # 角色

        # 选中select元素
        select2 = driver.find_element_by_id('role')
        # 使用Select进行处理
        roles = Select(select2)
        # 选择角色
        roles.select_by_index(random.randint(1,16)) # 根据下标来选中

        # 密码
        driver.find_element_by_id('password1').send_keys('123456')
        driver.find_element_by_id('password2').send_keys('123456')

        driver.find_element_by_id('email').send_keys('%s@163.com'%username)

        # 保存
        driver.find_element_by_id('submit').click()

        sleep(3)

        # 断言
        accounts = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[3]')
        account = accounts[-1]
        assert account.text == username

        # 添加下一个成员

        driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div[2]/a[1]').click()
# except Exception as e:
#     print(e)
finally:
    sleep(3)
    driver.close()