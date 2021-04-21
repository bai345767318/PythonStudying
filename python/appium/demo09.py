from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

desired_capabilities ={
"platformName": "Android",
"platformVersion": "5.1.1",
"appPackage": "com.baidu.wenku", #可删除
"appActivity": "com.baidu.wenku.splash.view.activity.WelcomeActivity", #可删除
"deviceName": "62001"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_capabilities)
sleep(3)
# driver.close_app()
#home
# driver.press_keycode(3)
# #音量
# driver.press_keycode(25)
# driver.press_keycode(24)
# driver.press_keycode(24)
# driver.press_keycode(24)
# driver.long_press_keycode(25)
# driver.long_press_keycode(24)

#安装app
driver.install_app(r'd:\com.mt.mtxx.mtxx.apk')
sleep(20)
#卸载
driver.remove_app('com.mt.mtxx.mtxx')