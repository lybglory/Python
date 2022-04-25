import time
# 1.导包
from selenium import webdriver

# 2.浏览器驱动初始化
dr = webdriver.Edge()

# 3.业务操作
dr.get("file:///C:/App/pagetest/registerA.html")
dr.find_element_by_css_selector("#telA").send_keys("10010")

# 4.等待3s
time.sleep(3)

# 5.退出edge驱动
dr.quit()