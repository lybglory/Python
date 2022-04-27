# 打开注册页面A，在用户名文本框上点击鼠标右键
import time
# 1.导包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

dr = webdriver.Edge()  # 2.浏览器驱动实例化
dr.get("file:///C:/App/pagetest/codenumber/index.html")
dr.maximize_window()  # 窗口最大化

ac = ActionChains(dr)  # 实例化鼠标对象

# 通过classname定位滑动块元素
sliderElemnt = dr.find_element(By.CLASS_NAME, "handler")
ac.drag_and_drop_by_offset(sliderElemnt, 265, 0)

ac.perform()  # 调用鼠标执行

time.sleep(3)
dr.quit()
