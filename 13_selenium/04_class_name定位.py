# 1).通过class_name定位电话号码A，并输入：18888888888
# 2).通过class_name定位电子邮箱A，并输入：888@qq.com
# 3).3秒后关闭浏览器窗口

# 1.导包
import time

from selenium import webdriver

# 2.浏览器驱动初始化
dr = webdriver.Edge()

# 3.业务操作
dr.get("file:///C:/App/pagetest/registerA.html")
dr.find_element_by_class_name("telA").send_keys("18888888888")
# <input type="email" name="emailA" class="emailA dzyxA" placeholder="请输入电子邮箱">
dr.find_element_by_class_name("emailA").send_keys("888@qq.com")
# class="emailA dzyxA",通过by_class_name定位的话，
# 只能取class属性中的取其中一个值。如果是"emailA dzyxA"则定位不到

# 4.等待3s
time.sleep(3)

# 5.退出edge驱动
dr.quit()
