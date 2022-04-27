# 需求：打开注册A页面，完成以下操作
# 1). 输入用户名：admin1，暂停2秒，删除1
# 2). 全选用户名：admin，暂停2秒
# 3). 复制用户名：admin，暂停2秒
# 4). 粘贴到密码框
import time
# 1.导包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

dr = webdriver.Edge()  # 2.浏览器驱动实例化
dr.get("file:///C:/App/pagetest/registerA.html")
dr.maximize_window()  # 窗口最大化
# 通过css层级选择器定位用户名输入框元素
userInputElemnt = dr.find_element(By.CSS_SELECTOR, "p>#userA")
userInputElemnt.send_keys("admin1")
time.sleep(2)

# 删除最后一个字符串
userInputElemnt.send_keys(Keys.BACK_SPACE)

# 全选用户名：admin，暂停2秒
userInputElemnt.send_keys(Keys.CONTROL, 'a')
time.sleep(2)

# 复制用户名：admin，暂停2秒
userInputElemnt.send_keys(Keys.CONTROL, 'C')
time.sleep(2)

# 通过css_id选择器定位密码输入框元素
pawdElemnt = dr.find_element(By.CSS_SELECTOR, "#passwordA")
# 粘贴到密码框
pawdElemnt.send_keys(Keys.CONTROL, 'v')
time.sleep(3)
dr.quit()



