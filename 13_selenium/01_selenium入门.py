import time
# 1.导入selenium模块
from selenium import webdriver
# 2.实例化Edge浏览器驱动对象
dr = webdriver.Edge()
# 3.业务操作
dr.get("http://www.baidu.com")
# 4.等待3s
time.sleep(3)
# 5.退出浏览器驱动
dr.quit()

