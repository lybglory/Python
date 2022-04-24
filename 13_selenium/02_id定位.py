# 需求：打开注册A.html页面，完成以下操作
# 1).使用id定位，输入用户名：admin
# 2).使用id定位，输入密码：123456
# 3).3秒后关闭浏览器窗口
# 1.导包
import time

from selenium import webdriver

# 2.浏览器驱动初始化
dr = webdriver.Edge()

# 3.业务操作
dr.get("file:///C:/App/pagetest/registerA.html")
dr.find_element_by_id("userA").send_keys("admin")
dr.find_element_by_id("passwordA").send_keys("123456")

# 4.等待3s
time.sleep(3)

# 5.退出浏览器
dr.quit()