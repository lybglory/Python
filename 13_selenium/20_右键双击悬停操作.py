# 打开注册页面A，在用户名文本框上点击鼠标右键
import time
# 1.导包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

dr = webdriver.Edge()   # 2.浏览器驱动实例化
dr.get("file:///C:/App/pagetest/registerA.html")
dr.maximize_window()    # 窗口最大化
ac = ActionChains(dr)   # 实例化鼠标对象
userInputElemnt = dr.find_element(By.CSS_SELECTOR, "p>#userA")
ac.context_click(userInputElemnt)   # 鼠标右键操作
time.sleep(3)
ac.send_keys("admin")   # 输入用户名

ac.double_click(userInputElemnt)    # 双击用户名输入框
time.sleep(3)
# 通过css层级选择器定位【注册】按钮
btnRegElemnt = dr.find_element(By.CSS_SELECTOR, "p>button")
ac.move_to_element(btnRegElemnt) # 悬停在"注册"按钮

ac.perform()            #调用鼠标执行

time.sleep(3)
dr.quit()