from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')

    driver.find_element_by_id('kw').send_keys('股市暴涨')
    sleep(2)
    # 后退
    driver.back()
    sleep(2)
    # 前进
    driver.forward()
    sleep(2)
    # 刷新
    driver.refresh()
except Exception as e:
    print(e)
finally:
    sleep(3)
    driver.quit()