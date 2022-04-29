import time
from selenium import webdriver
dr = webdriver.Edge()
dr.maximize_window()
dr.get("http://www.baidu.com")
cookieDic={
    "name" : "BDUSS",
    "value" : "BDUSS_Value"
}
time.sleep(3)
# 添加cookie
dr.add_cookie(cookieDic)

# 刷新页面
dr.refresh()