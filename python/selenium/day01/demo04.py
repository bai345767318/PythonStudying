from selenium import webdriver
from time  import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    # 窗口最大化
    driver.maximize_window()

    # 精确文本定位
    # driver.find_element_by_xpath('//span[text()="设置"]').click()
    # sleep(3)
    # driver.find_element_by_xpath('//a[text()="登录"]').click()
    # driver.find_element_by_xpath('//*[@id="u1"]/a').click()
    # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/a').click()

    # 模糊文本定位
    # driver.find_element_by_xpath('//*[contains(text(),"拜登胜选")]').click()

    # 属性精确定位
    # driver.find_element_by_xpath('//*[@maxlength="255"]').send_keys('川普')
    # 属性模糊定位
    # driver.find_element_by_xpath('//*[contains(@maxlength,"55")]').send_keys('川普')

    # driver.find_element_by_xpath('//*[starts-with(@maxlength,"25")]').send_keys('川普')

    # css定位
    driver.find_element_by_css_selector('#kw').send_keys('川普')

except Exception as e:
    print(e)
finally:
    sleep(3)
    driver.quit()