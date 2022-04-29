import time
from selenium import webdriver
from selenium.webdriver.common.by import By

dr = webdriver.Edge()
dr.maximize_window()
dr.get("file:///C:/App/pagetest/page/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
# 定位主页的用户名输入admin
dr.find_element(By.CSS_SELECTOR, "#user").send_keys("admin")

# 切换到注册A页面
dr.switch_to.frame(dr.find_element(By.ID, "idframe1"))
dr.find_element(By.CSS_SELECTOR, "#userA").send_keys("admin_A")
time.sleep(2)

# 回到首页
dr.switch_to.default_content()
# 在切换到注册b页面
dr.switch_to.frame(dr.find_element(By.NAME, "myframe2"))
dr.find_element(By.CSS_SELECTOR, "#userB").send_keys("admin_B")

time.sleep(3)
dr.quit()