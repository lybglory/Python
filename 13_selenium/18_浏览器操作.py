import time
from selenium import webdriver  # 1.导包
# 元素定位方法参数化包
from selenium.webdriver.common.by import By

# 2.浏览器驱动实例化
dr = webdriver.Edge()

# 3.业务操作
dr.maximize_window()    # 窗口最大化
dr.get("file:///C:/App/pagetest/registerA.html")

# 在注册A页面中点击 新浪网站
dr.find_element(By.XPATH, "//*[text()='新浪']").click()
time.sleep(3)
dr.back()       # 调用浏览器的后退

time.sleep(3)
dr.forward()    # 再调用浏览器的前进

time.sleep(3)
dr.back()       # 再调用浏览器的后退

time.sleep(3)
# 通过css层级选择器定位点击访问新浪网站
dr.find_element(By.CSS_SELECTOR, "p>#fw").click()

time.sleep(3)   # 等待3S
dr.close()      # 再调用关闭按钮
time.sleep(3)   # 等待3S
dr.quit()       # 退出



