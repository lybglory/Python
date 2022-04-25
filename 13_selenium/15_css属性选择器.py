# 1).使用CSS定位方式中属性选择器定位密码输入框，并输入：123456
import time
# 1.导包
from selenium import webdriver

# 2.浏览器驱动初始化
dr = webdriver.Edge()

# 3.业务操作
dr.get("file:///C:/App/pagetest/registerA.html")
# CSS定位方式中属性选择器定位密码输入框
dr.find_element_by_css_selector('[type="password"]').send_keys("123")

# 4.等待3s
time.sleep(3)

# 5.退出edge驱动
dr.quit()