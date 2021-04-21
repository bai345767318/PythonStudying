from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

desired_capabilities ={
"platformName": "Android",
"platformVersion": "5.1.1",
"deviceName": "62001"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_capabilities)
sleep(3)

#定位元素
mtxx = driver.find_element_by_accessibility_id(('美图秀秀'))
#长按元素            可以一系列操作    执行
pressed = TouchAction(driver).long_press(mtxx).perform()
#拖动并释放元素
pressed.move_to(x=125,y=84).release().perform()
#点击确认
driver.tap([(591,732)])
sleep((5))

#用命令行工具实现
#百度ANDRIOD KEYCODE
#CMD:adb shell input keyevent KEYCODE_HOME
#CMD:adb shell input keyevent 3