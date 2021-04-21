from selenium import webdriver

# 创建浏览器
driver = webdriver.Chrome()
# 打开网页
driver.get('https://www.baidu.com')

# 搜索 拜登
# 1.找到搜索框，输入搜索关键字
# id
driver.find_element_by_id("kw").send_keys("拜登")
# name
# driver.find_element_by_name('wd').send_keys('拜登')
# class_name
# driver.find_element_by_class_name('s_ipt').send_keys('拜登')
# tag_name
# 当同时定位到多个元素时，返回第一个
# driver.find_element_by_tag_name('input').send_keys('拜登') #?????

# 2.找到'百度一下'按钮并单击 click()
driver.find_element_by_id('su').click()

