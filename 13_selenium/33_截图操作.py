import time
from selenium import webdriver
from selenium.webdriver.common.by import By
dr = webdriver.Edge()
dr.maximize_window()
dr.get("file:///C:/App/pagetest/registerA.html")

try:
    # 通过CSS_id定位密码输入框,主动抛出异常
    pwdEle =dr.find_element(By.CSS_SELECTOR, "#passwordA")
    pwdEle.send_keys("123456")
    if pwdEle :
        # 出现异常截图
        dr.get_screenshot_as_file("./img/error{}.png".format(time.strftime("%Y%m%d-%H%M%S")))
        raise Exception("主动抛出异常：元素找不到！")
except Exception as result:
    print(result)

time.sleep(3)
dr.quit()

