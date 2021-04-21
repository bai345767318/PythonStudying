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
#利用坐标定位元素
driver.tap([(450,860)])
sleep(10)
driver.tap([(360,940)])
sleep(10)

#滑动
driver.swipe(350,1000,350,500,1000)
sleep(5)

driver.close_app()
#美图秀秀
# driver.tap([(360,700)])
# sleep(7)
# driver.tap([(382,751)])
# sleep(5)
