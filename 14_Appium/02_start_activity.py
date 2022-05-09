import time

from appium import webdriver
appInfo ={}
appInfo["platformName"]="android"               # 表示系统平台
appInfo["platformVersion"]="7.1.2"              # 系统版本号
appInfo["deviceName"] = "****"                  # 设备ID名称
appInfo["appPackage"]="com.android.settings"    # "设置"app包名
appInfo["appActivity"] = ".Settings"            # "设置"app界面名

dr= webdriver.Remote("http://localhost:4723/wd/hub", appInfo)

time.sleep(3)
# 启动"作业帮app"
dr.start_activity("com.baidu.homework", ".activity.index.IndexActivity")
print(dr.current_package)   # 获取当前脚本运行中的app包名
print(dr.current_activity)  # 获取当前脚本app的界面名

dr.close_app()  # 关闭app
print(dr.is_app_installed("com.baidu.homework")) # 作业帮是否安装
time.sleep(3)

# 启动"微信"App
dr.start_activity("com.tencent.mm", ".app.WeChatSplashActivity")
dr.background_app(6)

# 如果安装了"云通信"，则卸载,没有安装则安装
if dr.is_app_installed("com.em.mobile") :
    dr.remove_app("com.em.mobile")
else:
    # 安装"云通信"App
    dr.install_app(r"C:\Users\lybgl\Downloads\ytx.apk")

time.sleep(6)
dr.quit()


