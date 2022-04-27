import time
# 1.导包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

dr = webdriver.Edge()   # 2.浏览器驱动实例化
dr.maximize_window()    # 窗口最大化
dr.implicitly_wait(5)   # 隐士等待5秒

dr.get("file:///C:/App/pagetest/registerA.html")

# 第一个延时4s才会显示，设定隐士等待5秒在操作输入admin
print("开始时间：", time.strftime("%H:%M:%S"))
dr.find_element(By.XPATH, "//div[@id='wait']/input[1]").send_keys("admin")
print("找到第一个元素的时间:", time.strftime("%H:%M:%S"))
time.sleep(3)   # 等待3S
dr.quit()       # 退出浏览器驱动
