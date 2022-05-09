# 导入appiunm的webdriver
import time

from appium import webdriver
appInfo = {}
appInfo["platformName"]="android"               # 表示系统平台
appInfo["platformVersion"]="7.1.2"              # 系统版本号
appInfo["deviceName"] = "****"                  # 设备ID名称
appInfo["appPackage"]="com.android.settings"    # app包名
appInfo["appActivity"] = ".Settings"            # app界面名

dr= webdriver.Remote("http://localhost:4723/wd/hub", appInfo)
time.sleep(6)
dr.quit()
