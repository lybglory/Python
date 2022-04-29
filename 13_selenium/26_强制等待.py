import time
# 1.导包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 导入显示等待类
from selenium.webdriver.support.wait import WebDriverWait

dr = webdriver.Edge()  # 2.浏览器驱动实例化
dr.maximize_window()  # 窗口最大化
dr.get("http://localhost/Home/user/login.html")
# 用户名输入框
dr.find_element(By.CSS_SELECTOR, ".text_uspa>#username").send_keys("18888888888" )

# 密码输入框
dr.find_element(By.CSS_SELECTOR, "[type='password']").send_keys("123456")

# 验证码
dr.find_element(By.XPATH, "//*[@id='verify_code']").send_keys("8888")

# 点击登录
dr.find_element(By.CSS_SELECTOR, "[name='sbtbutton']").click()

# 强制等待，避免获取元素出错
time.sleep(10)
# 获取购物车数量
carNumber=dr.find_element(By.CSS_SELECTOR, "#cart_quantity").text
print("购车数量=%s" %carNumber)

time.sleep(3)  # 等待3S
dr.quit()  # 退出浏览器驱动

