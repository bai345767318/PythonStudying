'''
等待:
休眠：简单，每次要写，难于确定准确时间
隐式等待
显示等待
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')


'''
隐式等待
1.等待整个页面加载完成
2.参数为最大等待时间
优点：只需要写一次，不会浪费太多时间
'''
driver.implicitly_wait(10)  

'''
显示等待
1.等待指定的元素加载完成
优点：不会浪费时间
缺点：每次使用的时候都要写
'''
# driver.find_element_by_id('kw').send_keys('霜降')
driver.find_element(By.ID,'kw').send_keys('霜降')

# 返回值就是要等待的目标元素
element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'su')))
element.click()

sleep(3)