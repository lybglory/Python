import time
from appium import webdriver
# 定位元素参数化方法，需要导入By模块
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# 导入自动逸封装好显示等待定位元素、输入封装、判断元素是否存在的类
from MyTools import  Tools

drInfo = {}
drInfo["platformName"] = "android"  # 表示系统平台
drInfo["platformVersion"] = "7.1.2"  # 系统版本号
drInfo["deviceName"] = "emulator-5554"  # 设备ID名称，如果一个设备可以用4个*代替
drInfo["appPackage"] = "com.android.settings"  # "设置"app包名
drInfo["appActivity"] = ".Settings"  # "设置"app界面名
drInfo["resetKeyboard"] = True				# 重置设备的输入键盘
drInfo["unicodeKeyboard"] = True 			# 采用unicode编码输入，支持中文输入
# 用来记住app的session，如果有登陆或做过初始化的操作，为True时，后面不需要再操作
drInfo["noReset"] = True

# 连接appium服务器
dr = webdriver.Remote("http://localhost:4723/wd/hub", drInfo)
dr.start_activity("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")

# find_element方法的参数(元组)：通过xpath定位“购物车”
findParams = By.XPATH, "//*[@text='不存在的元素值']",
# 调用"判断元素是否定位到"封装好的方法，能定位则调用定位元素的方法
if Tools.elementIsExist(dr, findParams):
    # 调用元素定位的方法
    shopEle = Tools.getElement(dr, findParams)
    shopEle.click()
else:
    print("元素定位出错啦！")
    dr.get_screenshot_as_file("./img/err{}.png".format(time.strftime("%Y%m%d-%M%S")))

dr.press_keycode(4)
dr.quit()