from appium import webdriver
from time import sleep

#打开百度文库
desired_capabilities ={
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "appPackage": "com.baidu.wenku",
  "appActivity": "com.baidu.wenku.splash.view.activity.WelcomeActivity",
  "deviceName": "62001"
}

#打开百度文库
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_capabilities)
sleep(8)

driver.find_element_by_id('com.baidu.wenku:id/tv_agree').click()
sleep(10)
driver.find_element_by_id('com.baidu.wenku:id/dialog_pic_close').click()
sleep(8)
# driver.find_element_by_id('com.baidu.wenku:id/newbie_gift_close_btn').click()
# sleep(3)
driver.find_element_by_id('com.baidu.wenku:id/h5_search_edit_text').click()
sleep(5)
driver.find_element_by_id('com.baidu.wenku:id/h5_search_edit_text_inside').send_keys('高考满分作文')
sleep(2)
driver.find_element_by_id('com.baidu.wenku:id/h5_search_operate_text').click()#点击搜索
sleep(3)
elements = driver.find_elements_by_class_name('android.view.View')
sleep(3)
texts = [e.text for e in elements]
assert '2015上海高考满分作文(8篇)' in texts
print(texts)
