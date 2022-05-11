import time
from appium import webdriver
# 定位元素参数化方法，需要导入By模块
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from MyTools import  Tools					# 导入自动封装好的Tools类

drInfo = {}
drInfo["platformName"] = "android"  			# 表示系统平台(不区分大小写)
drInfo["platformVersion"] = "7.1.2"  			# 系统版本号
drInfo["deviceName"] = "emulator-5554" 	 # 设备ID名称，如果一个设备可以用4个*代替
# "网易新闻"app包名
drInfo["appPackage"] = "com.netease.newsreader.activity"
# "网易新闻"app界面名
drInfo["appActivity"] = "com.netease.nr.biz.ad.AdActivity"
drInfo["resetKeyboard"] = True          		# 重置设备的输入键盘
drInfo["unicodeKeyboard"] = True         		# 采用unicode编码输入，支持中文输入

# 用来记住app的session，如果有登陆或做过初始化的操作，为True时，后面不需要再操作
drInfo["noReset"] = True
# 连接appium服务器
dr = webdriver.Remote("http://localhost:4723/wd/hub", drInfo)
time.sleep(8)

# 通过class定位滑动区域块
findScrollParams = By.CLASS_NAME, "android.widget.HorizontalScrollView"
scrollBlock = Tools.getElement(dr, findScrollParams)

# 查找目标元素"游戏"频道的定位参数，通过By.XPATH方式定位
findTarParams = By.XPATH, "//*[@text= '游戏']"
Tools.swipeAndFind(dr, scrollBlock, findTarParams)
time.sleep(2)

# 查找目标元素"游戏"频道的定位参数，通过By.XPATH方式定位
findTarParams = By.XPATH, "//*[@text= '不存在的元素']"
Tools.swipeAndFind(dr, scrollBlock, findTarParams)
time.sleep(2)

dr.quit()

