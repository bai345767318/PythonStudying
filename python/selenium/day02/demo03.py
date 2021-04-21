from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com')

    # tree.xpath('//*[@id="kw"]/@maxlength')
    # 获取指定属性的值
    # maxlength = driver.find_element_by_xpath('//*[@id="kw"]').get_attribute('maxlength')
    # print('maxength=%s'%maxlength)

    # 用class定位元素
    elements = driver.find_elements_by_class_name('mnav') # 返回一个列表
    for e in elements:
        print(e.get_attribute('href'))#attribute 属性
        if e.get_attribute('href') == "http://tieba.baidu.com/":
            e.click()

except Exception as e:
    print(e)
finally:
    sleep(3)
    driver.quit()