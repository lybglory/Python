import time
from appium import webdriver
# 定位元素参数化方法，需要导入By模块
from selenium.webdriver.common.by import By
# 导入显示等待模块
from selenium.webdriver.support.wait import WebDriverWait

drInfo = {}
drInfo["platformName"] = "android"  # 表示系统平台
drInfo["platformVersion"] = "7.1.2"  # 系统版本号
drInfo["deviceName"] = "emulator-5554"  # 设备ID名称，如果一个设备可以用4个*代替
drInfo["appPackage"] = "com.android.settings"  # "设置"app包名
drInfo["appActivity"] = ".Settings"  # "设置"app界面名

# 连接appium服务器
dr = webdriver.Remote("http://localhost:4723/wd/hub", drInfo)
dr.start_activity("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
# 通过xpath定位“购物车”
shopEle = WebDriverWait(dr, 10, 1).until(
    lambda e:e.find_element(By.XPATH, "//*[@text='购物车']"))
shopEle.click()
time.sleep(3)

# 通过class定位"手机号注册"按钮
telEle = WebDriverWait(dr, 10, 1).until(
    lambda e:e.find_element(By.CLASS_NAME, "android.widget.Button"))
telEle.click()
time.sleep(3)

# 通过id定位“返回”按钮
lefEle = WebDriverWait(dr, 10, 1).until(
    lambda e:e.find_element(By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"))
lefEle.click()
dr.close_app()

time.sleep(3)
dr.quit()


