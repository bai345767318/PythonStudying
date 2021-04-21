from selenium import webdriver
from time import sleep


try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')

    # driver.find_element_by_class_name('mnav').click()
    '''link_text:精确匹配'''
    # driver.find_element_by_link_text('视频').click()
    # driver.find_element_by_link_text('美媒宣布拜登当选 错判咋办?').click()
    '''partial_link_text:模糊匹配'''
    # driver.find_element_by_partial_link_text('学').click()
    driver.find_element_by_partial_link_text('成都确诊女孩当晚疑在一酒吧面试').click()
    # driver.find_element_by_partial_link_text('百度').click()

    # 关闭当前浏览器窗口
    # driver.close()
except Exception as e:
    print(e)
finally:
    # 休息3秒
    sleep(3)
    # 退出浏览器
    driver.quit()


