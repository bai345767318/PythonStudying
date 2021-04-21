from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    # 设置窗口尺寸
    driver.set_window_size(300,300)
    sleep(2)

    # 滚动页面
    # 目标元素
    element = driver.find_element_by_partial_link_text('美国平均')
    # 滚动代码
    script = 'arguments[0].scrollIntoView();'
    # 滚动到目标元素所在的位置
    driver.execute_script(script,element)

except Exception as e:
    print(e)
finally:
    sleep(3)
    driver.close()