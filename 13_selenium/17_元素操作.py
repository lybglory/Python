# 1).通过脚本执行输入用户名：admin；密码：123；电话号码：10010；电子邮件：123@qq.com
# 2).间隔3秒，修改电话号码为：10086
# 3).间隔3秒，点击‘注册’按钮
# 4).间隔3秒，关闭浏览器
# 5).元素定位方法不限
import time

from selenium import webdriver  # 1.导包
# 元素定位方法参数化包
from selenium.webdriver.common.by import By

dr = webdriver.Edge()  # 2.浏览器驱动实例化

# 3.业务操作
dr.get("file:///C:/App/pagetest/registerA.html")

# 通过id定位用户名输入框
dr.find_element(By.ID, "userA").send_keys("admin")
# 通过css属性选择器定位密码输入框
dr.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys("123")
# 通过Xpath元素属性定位电话号码输入框
dr.find_element(By.XPATH, '//*[@id="telA"]').send_keys("10010")
# 通过css中的class属性定位电话号码输入框
dr.find_element(By.CSS_SELECTOR, ".emailA").send_keys("123@qq.com")

# 间隔3s修改电话号码
time.sleep(3)

# 通过Xpath层级与属性结合定位电话号码输入框，清除操作
dr.find_element(By.XPATH, "//input[@id='telA']").clear()

time.sleep(2)
# 通过css中的id属性定位电话号码输入框
dr.find_element(By.CSS_SELECTOR, "#telA").send_keys("10086")

# 间隔3点击“访问 新浪 网站”
time.sleep(3)
# 通过局部链接定位点击“访问 新浪 网站”
dr.find_element(By.PARTIAL_LINK_TEXT, "访问").click()

time.sleep(3)
# 最后退出浏览器驱动
dr.quit()
