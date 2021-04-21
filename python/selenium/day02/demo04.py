'''键盘操作'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com')

    search = driver.find_element_by_id('kw')
    search.send_keys('哥伦比亚')
    # Ctrl+a
    search.send_keys(Keys.CONTROL,'a')
    sleep(2)
    search.send_keys(Keys.CONTROL,'c')
    sleep(2)
    search.send_keys(Keys.CONTROL,'v')
    search.send_keys(Keys.CONTROL,'v')
    search.send_keys(Keys.CONTROL,'v')


    # 输入一个回车
    search.send_keys(Keys.ENTER)

except Exception as e:
    print(e)
finally:
    sleep(3)
    driver.quit()