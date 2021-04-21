from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import random

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://localhost:8448/ranzhi/www/')

    # 登陆
    driver.find_element_by_id('account').send_keys('admin')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()
    # sleep(1)

    # 点击文档 D
    driver.find_element_by_id('s-menu-4').click()
    # sleep(1)
    # 进入iframe
    iframe = driver.find_element_by_id('iframe-4')
    driver.switch_to.frame(iframe)
    # sleep(1)

    # 点击"创建文档库"
    driver.find_element_by_id('createButton').click()
    # sleep(1)

    # 选择文档库类型
    select1 = driver.find_element_by_id('libType')
    types = Select(select1)
    types.select_by_visible_text('自定义文档库')

    # 文档库名称
    driver.find_element_by_id('name').send_keys('Python1')

    # 授权用户
    driver.find_element_by_xpath('//*[@id="users_chosen"]/ul').click()
    driver.find_element_by_xpath('//*[@id="users_chosen"]/div/ul/li').click()

    # 授权分组
    driver.find_element_by_id('groups1').click()
    driver.find_element_by_id('groups3').click()
    driver.find_element_by_id('groups5').click()

    # 保存
    driver.find_element_by_id('submit').click()
    # sleep(2)

    # 维护分类
    driver.find_element_by_partial_link_text('维护分类').click()
    sleep(1)
    driver.find_element_by_name('children[1]').send_keys('基础')
    driver.find_element_by_name('children[2]').send_keys('爬虫')
    driver.find_element_by_name('children[3]').send_keys('自动化')
    driver.find_element_by_name('children[4]').send_keys('pyqt')

    driver.find_element_by_id('submit').click()
    driver.back()
    # sleep(2)

    # 进入iframe
    iframe = driver.find_element_by_id('iframe-4')
    driver.switch_to.frame(iframe)
    # 创建文档
    driver.find_element_by_partial_link_text('创建文档').click()
    # sleep(3)

    # 所属分类
    select2 = driver.find_element_by_id('module')
    modules = Select(select2)
    modules.select_by_visible_text('/自动化')

    # 授权用户
    driver.find_element_by_xpath('//*[@id="users_chosen"]/ul').click()
    driver.find_element_by_xpath('//*[@id="users_chosen"]/div/ul/li').click()

    # 授权分组
    driver.find_element_by_id('groups1').click()
    driver.find_element_by_id('groups3').click()
    driver.find_element_by_id('groups5').click()

    # 文档类型   判断
    doctype = ['typetext','typeurl'][random.randint(0,1)]
    print(doctype)
    driver.find_element_by_id(doctype).click()
    # driver.find_element_by_id('typetext' if random.randint(0,1) else 'typeurl').click()

    # 标题
    driver.find_element_by_id('title').send_keys('requests')

    # 进入iframe
    iframe1 = driver.find_element_by_id('ueditor_0')
    driver.switch_to.frame(iframe1)
    # sleep(1)

    if doctype == 'typetext':
        driver.find_element_by_xpath('/html/body').send_keys('requests是一个爬虫工具...')
    else:
        driver.find_element_by_id('url').send_keys('https://www.baidu.com')

    # 回到上一级iframe
    driver.switch_to.parent_frame()
    # sleep(1)

    # 关键字
    driver.find_element_by_id('keywords').send_keys('requests')

    # 摘要
    driver.find_element_by_id('digest').send_keys('requests')

    # 上传文档
    driver.find_element_by_xpath('//*[@id="fileBox1"]/tbody/tr/td[1]/div/input').send_keys(r'D:\workspace\python\logo.png')
    driver.find_element_by_xpath('//*[@id="fileBox2"]/tbody/tr/td[1]/div/input').send_keys(r'D:\workspace\python\logo.png')

    driver.find_element_by_id('submit').click()

# except Exception as e:
#     print(e)
finally:
    # sleep(3)
    driver.close()