from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://localhost/ranzhi/www/')

    # 登陆
    driver.find_element_by_id('account').send_keys('tom')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()

    realname = driver.find_element_by_xpath('//*[@id="mainNavbar"]/div/ul[1]/li/a').text
    # 判断登陆是否成功
    # if realname == 'Tom Cruse':
    #     print('登陆成功！')
    # else:
    #     print('登陆失败！')

    # 断言
    assert realname == 'Tom Cruse'

    # 断言
    current_url = driver.current_url # 获取当前的url
    assert current_url == 'http://localhost:8448/ranzhi/www/sys/index.html'

    # 断言
    title = driver.title
    assert title == '然之协同'

    print('用例运行结束！')

# except Exception as e:
#     print(e)
finally:
    sleep(3)
    driver.close()