# 1).利用元素的属性信息精确定位用户名输入框，并输入：admin
# 2).3秒后关闭浏览器窗口
import time
# 1.导包
from selenium import webdriver

# 2.浏览器驱动初始化
dr = webdriver.Edge()

# 3.业务操作
dr.get("file:///C:/App/pagetest/registerA.html")

# 利用元素定位用户名输入框
# //input[@placeholder="请输入用户名"]
dr.find_element_by_xpath('//*[@placeholder="请输入用户名"]').send_keys("admin")
dr.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys("admin")

# 4.等待3s
time.sleep(3)

# 5.退出edge驱动
dr.quit()
