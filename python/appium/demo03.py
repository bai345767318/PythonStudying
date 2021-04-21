'''
app独有定位
accessibility_id > content-desc
'''
from appium import webdriver
from time import sleep

desired_capabilities ={
"platformName": "Android",
"platformVersion": "5.1.1",
"appPackage": "com.baidu.wenku", #可删除
"appActivity": "com.baidu.wenku.splash.view.activity.WelcomeActivity", #可删除
"deviceName": "62001"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_capabilities)
sleep(2)
#关闭app
driver.close_app()
#打开美图秀秀 accessibility_id > content-desc
driver.find_element_by_accessibility_id('美图秀秀').click()
sleep(5)
driver.close_app()
