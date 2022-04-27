# 打开注册页面A，在用户名文本框上点击鼠标右键
import time
# 1.导包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

dr = webdriver.Edge()  # 2.浏览器驱动实例化
dr.get("file:///C:/App/pagetest/drag.html")
dr.maximize_window()  # 窗口最大化

ac = ActionChains(dr)  # 实例化鼠标对象

redElemnt = dr.find_element(By.ID, "div1")
blueElemnt = dr.find_element(By.ID, "div2")
ac.drag_and_drop(redElemnt, blueElemnt)
ac.perform()  # 调用鼠标执行

time.sleep(3)
dr.quit()
