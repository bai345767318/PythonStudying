from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    # full Xpath 绝对路径
    # driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input').send_keys('6G')
    # Xpath 相对路径
    # driver.find_element_by_xpath('//*[@id="kw"]').send_keys('096')
    driver.find_element_by_xpath('*[@id="for//m"]/span[1]/input').send_keys('096')

    # 百度一下
    driver.find_element_by_xpath('//input[@value="百度一下" and @type="submit"]').click()
except Exception as e:
    print(e)
finally:
    sleep(3)
    driver.close()