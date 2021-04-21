from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
import os,sys
print(sys.path)
# get currenty working directory
print(os.getcwd()) # print working directory: pwd()
sys.path.append(os.getcwd())
print(sys.path)
 
# 设置chrome浏览器无界面模式
# chrome_options = Options()
# chrome_options.add_argument('--headless')

# # driver = webdriver.Chrome()
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('https://www.qktxt.com/book/shikongshanghao/')
# driver.maximize_window()
# driver.implicitly_wait(10)

# aa = driver.find_elements_by_xpath('//*[@id="list"]/ul/li/a')
# print(aa)

# links = [a.get_attribute('href') for a in aa[:10]]
# print(links)

