import time
from selenium import webdriver
from selenium.webdriver.common.by import By

dr = webdriver.Edge()
dr.maximize_window()
dr.get("file:///C:/App/pagetest/registerA.html")

time.sleep(3)
dr.find_element(By.CSS_SELECTOR, "[value='gz']").click()
time.sleep(3)
dr.find_element(By.CSS_SELECTOR, "[value='bj']").click()
time.sleep(3)
dr.find_element(By.CSS_SELECTOR, "[value='sh']").click()

time.sleep(3)
dr.quit()