import time
from selenium import webdriver
from selenium.webdriver.common.by import By

dr = webdriver.Edge()
dr.maximize_window()
dr.get("file:///C:/App/pagetest/page/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
dr.find_element(By.ID, "ZCA").click()
time.sleep(2)

# 获取当前窗口句柄信息
print("当前窗口句柄信息：" + dr.current_window_handle )

# 获取所有窗口句柄信息
wds = dr.window_handles

# 切换最后一个窗口句柄(-1表示最新的窗口句柄)
dr.switch_to.window(wds[-1])
# 在注册A页面定位用户名输入框元素
dr.find_element(By.CSS_SELECTOR, "#userA").send_keys("admin")

time.sleep(3)
dr.quit()

