# 1).使用link_text定位(访问 新浪 网站)超链接，并点击
# 2).3秒后关闭浏览器窗口

import time
# 1.导包
from selenium import webdriver

# 2.浏览器驱动初始化
dr = webdriver.Edge()

# 3.业务操作
dr.get("file:///C:/App/pagetest/registerA.html")
# <a href="http://www.sina.com.cn" id="fw" target="_blank">访问 新浪 网站</a>
# element_by_link_text通过超链接的文本内容来定位元素
# dr.find_element_by_link_text("访问 新浪 网站").click()
# partial_link_text可以使用局部来匹配元素，也可以使用全部文本内容匹配元素。
dr.find_element_by_partial_link_text("网站").click()
dr.find_elements_
# 4.等待3s
time.sleep(3)

# 5.退出edge驱动
dr.quit()
