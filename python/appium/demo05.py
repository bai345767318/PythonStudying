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
sleep(3)
'''UiAutomator'''
#同意并继续
#            java代码         属性：值
selector = 'new UiSelector().text("同意并继续")'
driver.find_element_by_android_uiautomator(selector).click()
sleep(10)
#点击关闭升级
# selector = 'new UiSelector().resourceId("com.baidu.wenku:id/dialog_pic_close")'
selector = 'new UiSelector().className("android.widget.ImageView")'
# selector = 'new UiSelector().className("android.widget.TextView")'#找到3个
driver.find_element_by_android_uiautomator(selector).click()
sleep(10)

driver.close_app()