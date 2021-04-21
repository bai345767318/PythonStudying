from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')

    # 窗口最大化
    driver.maximize_window()
    # 窗口最小化
    # driver.minimize_window()
    # 获取窗口的尺寸
    print(driver.get_window_size())

    driver.find_element_by_id('kw').send_keys('天津')
    sleep(2)
    # 清除搜索框内容
    driver.find_element_by_id('kw').clear()
    driver.find_element_by_id('kw').send_keys('上海')

    driver.find_element_by_id('su').click()
    sleep(2) # 等待网页加载完成

    # 点击 百度百科
    driver.find_element_by_partial_link_text('百度百科').click()
    sleep(2)

    # 切换浏览器窗口
    print('当前窗口句柄：'+driver.current_window_handle)
    # 获取所有的窗口的句柄
    handles = driver.window_handles
    print(handles)
    # 获取指定的窗口的句柄
    second_handle = handles[1]
    # 切换到指定的窗口
    driver.switch_to.window(second_handle)
    print('当前窗口句柄：'+driver.current_window_handle)
    
    driver.find_element_by_partial_link_text('上海报告一例新冠肺炎确诊病例').click()

except Exception as e:
    print(e)
finally:
    sleep(3)
    driver.quit()