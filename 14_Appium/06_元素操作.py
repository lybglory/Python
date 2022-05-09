import time
from appium import webdriver
# 定位元素参数化方法，需要导入By模块
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

drInfo = {}
drInfo["platformName"] = "android"  # 表示系统平台
drInfo["platformVersion"] = "7.1.2"  # 系统版本号
drInfo["deviceName"] = "emulator-5554"  # 设备ID名称，如果一个设备可以用4个*代替
drInfo["appPackage"] = "com.android.settings"  # "设置"app包名
drInfo["appActivity"] = ".Settings"  # "设置"app界面名

# 连接appium服务器
dr = webdriver.Remote("http://localhost:4723/wd/hub", drInfo)
searchEle = WebDriverWait(dr, 10, 1).until(
    lambda e: e.find_element(By.ID, "com.android.settings:id/search"))
searchEle.click()  # 点击操作
time.sleep(2)
editEle = WebDriverWait(dr, 10, 1).until(
    lambda e: e.find_element(By.ID, "android:id/search_src_text"))
editEle.send_keys("Wifi")  # 输入操作
time.sleep(2)

editEle.clear()  # 输入框清空操作
time.sleep(3)
dr.close_app()
dr.quit()
