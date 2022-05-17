import time
from appium import webdriver
# 定位元素参数化方法，需要导入By模块
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from MyTools import  Tools					# 导入自动封装好的Tools类
drInfo = {
    "platformName": "android",  			# 表示系统平台(不区分大小写)
    "platformVersion": "7.1.2",  			# 系统版本号
    "deviceName" : "emulator-5554", 	    # 设备ID名称，如果一个设备可以用4个*代替
    "appPackage" : "com.android.settings",  # "设置"app包名
    "appActivity": ".Settings",  			# "设置"app界面名
    "resetKeyboard" : True,          		# 重置设备的输入键盘
    "unicodeKeyboard" : True,        		# 采用unicode编码输入，支持中文输入
    # 用来记住app的session，如果有登陆或做过初始化的操作，为True时，后面不需要再操作
    "noReset" : True,
    "automationName": "Uiautomator2"    # 获取toast消息
}
# 连接appium服务器
dr = webdriver.Remote("http://localhost:4723/wd/hub", drInfo)
# 调用滑动封装的方法，向上滑动几次（找到最下面的元素），点击"关于平板电脑"
Tools.swipeHandle(dr, "top", swipeCount=3)

# 定位“关于平板电脑”元素，并点击
findParams = By.XPATH, "//*[@text='关于平板电脑']"
aboutEle = Tools.getElement(dr, findParams)
aboutEle.click()

# 调用滑动封装的方法，向上滑动几次（找到最下面的元素），点击"版本号元素"
Tools.swipeHandle(dr, "top", swipeCount=3)
findParams = By.XPATH, "//*[@text='版本号']"   # 元组数据类型
versionEle =  Tools.getElement(dr, findParams)

versionEle.click()
time.sleep(1)

# 调用封装好的方法：元素是否能定位到的方法
# findParams = By.XPATH, "//*[contains(@text,'开发者模式')]"
# if Tools.elementIsExist(dr, findParams):
#     toastEle = Tools.getElement(dr, findParams)
#     print("获取到toast信息："+toastEle.get_attribute("text"))

print(Tools.getToastElement(dr, "开发者模式"))

time.sleep(3)
dr.quit()