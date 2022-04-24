# 1.导包
from selenium import webdriver
import time
# 2.edge浏览器驱动初始化
dr = webdriver.Edge()
# 3.业务操作
dr.get("file:///C:/App/pagetest/registerA.html")
dr.find_element_by_name("userA").send_keys("admin")
dr.find_element_by_name("passwordA").send_keys("123456")
# 4.等待3秒
time.sleep(3)
# 5.退出浏览器驱动
dr.quit()