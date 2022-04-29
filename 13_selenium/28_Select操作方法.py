import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 1.导入select类
from selenium.webdriver.support.select import Select
dr = webdriver.Edge()
dr.maximize_window()
dr.get("file:///C:/App/pagetest/registerA.html")

selectTagEle = dr.find_element(By.ID, "selectA")
se = Select(selectTagEle)   # 2.实例化Select对象
se.select_by_index(3)       # 3.调用操作方法：通过索引
time.sleep(2)
se.select_by_value("sh")    # 通过select对象的value来选择
time.sleep(2)
se.select_by_visible_text("广州") # 通过select对象的visible来选择

time.sleep(3)
dr.quit()
