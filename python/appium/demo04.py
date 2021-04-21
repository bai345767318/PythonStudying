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


#点击同意并继续
driver.find_element_by_xpath('//*[contains(@text,"同意并继续")]').click()
sleep(5)
#关闭升级
driver.find_element_by_xpath('//*[contains(@resource-id,"com.baidu.wenku:id/dialog_pic_close")]').click()