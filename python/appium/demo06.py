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
'''联合定位'''
#同时对多个属性进行定位
# javascript基本都可以进行连续调用
#精确文本定位 :text()
# selector = 'className("android.widget.TextView").text("同意并继续")'
'''模糊定位'''
#模糊文本定位 :textContains()
# selector = 'new UiSelector().textContains("意并继")'
# driver.find_element_by_android_uiautomator(selector).click()

'''利用元素之间的关系进行定位'''
#父子关系--------
# selector = 'className("android.widget.FrameLayout").childSelector(text("同意并继续"))'
# driver.find_element_by_android_uiautomator(selector).click()
# #兄弟关系
selector = 'text("温馨提示").fromParent(text("同意并继续"))'
driver.find_element_by_android_uiautomator(selector).click()

sleep(5)

driver.close_app()
#用javascript定位方式，定位元素属性content-desc:美图秀秀
# selector = 'new UiSelector().description("美图秀秀")'
# driver.find_element_by_android_uiautomator(selector).click()