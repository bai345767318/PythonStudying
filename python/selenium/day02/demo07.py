from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://localhost:8448/ranzhi/www/sys/user-login.html')

    # 登陆
    driver.find_element_by_id('account').send_keys('admin')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()
    sleep(1)

    # 添加成员
    driver.find_element_by_xpath('//*[@id="s-menu-superadmin"]/button').click()
    sleep(1)

    # 切换到frame中
    frame = driver.find_element_by_id('iframe-superadmin')
    driver.switch_to.frame(frame)

    # 点击"添加成员"
    driver.find_element_by_partial_link_text('添加成员').click()
    sleep(1)

    # 添加成员
    driver.find_element_by_id('account').send_keys('tom')
    driver.find_element_by_id('realname').send_keys('Tom Cruse')
    driver.find_element_by_id('genderm').click()

    # 选中select元素
    select1 = driver.find_element_by_id('dept')
    # 使用Select进行处理
    depts = Select(select1)
    # 选择部门
    depts.select_by_index(1) # 根据下标来选中
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
    roles.select_by_value("pm") # 根据下标来选中

    # 密码
    driver.find_element_by_id('password1').send_keys('123456')
    driver.find_element_by_id('password2').send_keys('123456')

    driver.find_element_by_id('email').send_keys('tom@163.com')

    # 保存
    driver.find_element_by_id('submit').click()

    sleep(2)

    # 删除
    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[3]').click()
    sleep(1)
    # 点击“取消”
    driver.switch_to.alert.dismiss()

    # 再次点击删除
    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[3]').click()
    sleep(1)
    # 点击“确认”
    driver.switch_to.alert.accept()

except Exception as e:
    print(e)
finally:
    sleep(3)
    driver.close()