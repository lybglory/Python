# 1).使用层级与属性结合定位策略，在test1对应的输入框里输入：admin
# 2).3秒后关闭浏览器窗口
import time
# 1.导包
from selenium import webdriver

# 2.浏览器驱动初始化
dr = webdriver.Edge()

# 3.业务操作
dr.get("file:///C:/App/pagetest/registerA.html")

# 利用层级与属性结合定位test1输入框
dr.find_element_by_xpath('//p[@id="p1"]/input').send_keys("admin")

# 4.等待3s
time.sleep(3)

# 5.退出edge驱动
dr.quit()