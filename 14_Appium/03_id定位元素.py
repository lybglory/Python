import time
from appium import webdriver
# 定位元素参数化方法，需要导入By模块
from selenium.webdriver.common.by import By
# 导入显示等待模块
from selenium.webdriver.support.wait import WebDriverWait

appInfo = {}
appInfo["platformName"] = "android"  # 表示系统平台
appInfo["platformVersion"] = "7.1.2"  # 系统版本号
appInfo["deviceName"] = "emulator-5554"  # 设备ID名称，如果一个设备可以用4个*代替
appInfo["appPackage"] = "com.android.settings"  # "设置"app包名
appInfo["appActivity"] = ".Settings"  # "设置"app界面名

# 连接appium服务器
driver =webdriver.Remote("http://localhost:4723/wd/hub", appInfo)
# 找到“更多”按钮并点击(XPATH)
element = driver.find_element(By.XPATH, "//*[@text='更多']")
element.click()
time.sleep(2)
# 找到 飞行模式的 开关，并点击(ID)
air_element = driver.find_element(By.ID, "android:id/switch_widget")
air_element.click()
time.sleep(2)
# 找到返回按钮并点击(class)
return_element = driver.find_element(By.CLASS_NAME, "android.widget.ImageButton")
return_element.click()
driver.close_app()

time.sleep(3)
driver.quit()