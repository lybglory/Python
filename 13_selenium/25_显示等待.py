import time
# 1.导包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 导入显示等待类
from selenium.webdriver.support.wait import WebDriverWait

dr = webdriver.Edge()  # 2.浏览器驱动实例化
dr.maximize_window()  # 窗口最大化

dr.get("file:///C:/App/pagetest/registerA.html")

# 第二个延时输入框9秒才会加载完，通过显示等待10s后，再输入输入admin
delayEleSec = WebDriverWait(dr, 10, 1).until(lambda x: x.find_element(By.XPATH, "//div[@id='wait']/input[2]"))
delayEleSec.send_keys("admin2")

time.sleep(3)  # 等待3S
dr.quit()  # 退出浏览器驱动
