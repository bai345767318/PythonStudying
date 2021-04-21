'''鼠标操作'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')

    '''右键单击'''
    # element = driver.find_element_by_id('kw')
    # ActionChains(driver).context_click(element).perform()
    # sleep(2)

    '''左键单击'''
    # driver.find_element_by_id('kw').send_keys('Selenium')
    # element = driver.find_element_by_id('su')
    # ActionChains(driver).click(element).perform()

    '''双击'''
    # element = driver.find_element_by_id('kw')
    # element.send_keys('哥伦比亚')
    # ActionChains(driver).double_click(element).perform()

    '''悬停'''
    # element = driver.find_element_by_id('s-usersetting-top')
    # ActionChains(driver).move_to_element(element).perform()
    # driver.find_element_by_partial_link_text('高级搜索').click()

    '''按住不放'''
    driver.find_element_by_partial_link_text('拜登再次恳请民众戴口罩').click()
    sleep(1)
    # 切换窗口
    driver.switch_to.window(driver.window_handles[1])

    element = driver.find_element_by_xpath('//*[@id="con-ar"]/div/div/div/table/tbody[1]/tr[1]/td[1]/a')
    ActionChains(driver).click_and_hold(element).perform()

except Exception as e:
    print(e)
finally:
    sleep(3)
    driver.quit()