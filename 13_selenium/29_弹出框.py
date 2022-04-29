import time
from selenium import webdriver
from selenium.webdriver.common.by import By

dr = webdriver.Edge()
dr.maximize_window()
dr.get("file:///C:/App/pagetest/registerA.html")
dr.find_element(By.ID, "alerta").click()
time.sleep(2)
alert = dr.switch_to.alert # 获取弹出框
print(alert.text)
alert.dismiss()
time.sleep(2)
# 弹出框取消才能进行页面的操作，定位test1输入框，输入admin
dr.find_element(By.CSS_SELECTOR, "#p1>.login").send_keys("admin")
time.sleep(3)
dr.quit()
