import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def GetMobile():
    # 手机号码段前三位数字
    phoneStart = ['180', '181',  '136' '138']

    # 通过时间戳获取手机号码的后8位数(一定不会重复)
    # int(time.time()返回10位数字
    # 字符串切片,在切8个字符，从下标3开始切至结尾
    numbers =  str(int(time.time()))[2:]

    # 把手机号码格式的三位数与后8位数相加
    mobile = random.choice(phoneStart) + numbers
    return mobile

dr = webdriver.Edge()
dr.maximize_window()
dr.get("http://localhost/Home/user/reg.html")

# 通过CSS_id定位手机号码输入框
dr.find_element(By.CSS_SELECTOR, "#username").send_keys(GetMobile())
# 通过CSS属性定位验证码输入框
dr.find_element(By.CSS_SELECTOR, "[name='verify_code']").send_keys("8888")
# 通过CSS_id定位密码输入框
dr.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
# 通过CSS_id定位确认密码输入框
dr.find_element(By.CSS_SELECTOR, "#password2").send_keys("123456")
# 鼠标实例化
ac = ActionChains(dr)
# 通过CSS属性"我已阅读"单选框
ac.click(dr.find_element(By.CSS_SELECTOR, "[type='checkbox']"))
ac.perform()

time.sleep(3)
# 通过CSS_class定位“确认注册”按钮
dr.find_element(By.CSS_SELECTOR, ".regbtn").click()
time.sleep(10)
dr.quit()




