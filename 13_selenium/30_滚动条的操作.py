import time
from selenium import webdriver

dr = webdriver.Edge()
dr.maximize_window()
dr.get("file:///C:/App/pagetest/registerA.html")

time.sleep(2)
js = "window.scrollTo(0,1000)" # 设置js脚本控制滚动条
dr.execute_script(js)          # 调用执行js脚本的方法

time.sleep(3)
dr.quit()
