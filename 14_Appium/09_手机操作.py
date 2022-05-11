import os
import time
from appium import webdriver

drInfo = {}
drInfo["platformName"] = "android"  		# 表示系统平台(不区分大小写)
drInfo["platformVersion"] = "7.1.2" 		# 系统版本号
drInfo["deviceName"] = "emulator-5554"  	# 设备ID名称，如果一个设备可以用4个*代替
drInfo["appPackage"] = "com.android.settings"  # "设置"app包名
drInfo["appActivity"] = ".Settings"  			  # "设置"app界面名
drInfo["resetKeyboard"] = True				# 重置设备的输入键盘
drInfo["unicodeKeyboard"] = True 			# 采用unicode编码输入，支持中文输入

# 连接appium服务器
dr = webdriver.Remote("http://localhost:4723/wd/hub", drInfo)
time.sleep(3)

print(dr.get_window_size())     # 获取手机分辨率
# 获取手机网络（通过属性获取）
print("设置前网络类型%d" %(dr.network_connection))
dr.set_network_connection(2)    # 设置wifi模式
# 获取手机网络（通过属性获取）
print("设置后网络类型%d" %(dr.network_connection))

dr.open_notifications() # 打开通知栏
time.sleep(3)
dr.press_keycode(4)     # 返回键操作

# 手机截图操作
dr.get_screenshot_as_file(os.getcwd()+os.sep+"img/err_{}.png".format(time.strftime("%Y%m%d%H%M%S")))

time.sleep(3)
dr.quit()