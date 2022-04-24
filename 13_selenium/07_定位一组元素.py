# 1).使用tag_name定位密码输入框(第二个input标签)，并输入：123456
# 2).3秒后关闭浏览器窗口
import time
# 1.导包
from selenium import webdriver

# 2.浏览器驱动初始化
dr = webdriver.Edge()

# 3.业务操作
dr.get("file:///C:/App/pagetest/registerA.html")
# <input type="text" name="userA" id="userA" placeholder="请输入用户名">
# input标签
dr.find_elements_by_tag_name("input")[1].send_keys("123456")

# 4.等待3s
time.sleep(3)

# 5.退出edge驱动
dr.quit()
