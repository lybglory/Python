import time
from appium import webdriver
# 定位元素参数化方法，需要导入By模块
from selenium.webdriver.common.by import By
# 导入显示等待模块
from selenium.webdriver.support.wait import WebDriverWait
from MyTools import Tools   # 导入封装好的显示等待定位元素的模块
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
findParams = By.XPATH, "//*[@text='购物车']",    # 元组，确保元组里的元素不能修改
shopEle = Tools.getElement(dr, findParams)
shopEle.click()
time.sleep(3)


# 元组，确保元组里的元素不能修改
findParams = By.CLASS_NAME, "android.widget.Button",
# 通过class定位"手机号注册"按钮
telEle = Tools.getElement(dr, findParams)
telEle.click()
time.sleep(3)


# 元组，确保元组里的元素不能修改
findParams = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image",
# 通过id定位“返回”按钮
lefEle = Tools.getElement(dr, findParams)
lefEle.click()
dr.close_app()

time.sleep(3)
dr.quit()