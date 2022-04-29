import time
import autoit   # 导入autoit模块，用来操作windows窗口
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

dr = webdriver.Edge()
dr.maximize_window()
dr.get("http://www.baidu.com")

# 通过CSS层级定位百度搜图按钮
dr.find_element(By.CSS_SELECTOR, "span>.soutu-btn").click()
uploadEle = dr.find_element(By.CLASS_NAME, "upload-pic")
# 实例化鼠标对象
ac = ActionChains(dr)
# 调用事件
ac.click(uploadEle)
# 执行鼠标事件方法
ac.perform()
time.sleep(2)

# 针对windows操作
# 通过autoit来获取弹出的窗口
autoit.win_wait_active("打开", 3)

# 在文件选择输入框中输入文件的地址及文件名称
autoit.control_send("打开", "Edit1", r"C:\Users\lybgl\Desktop\st.jpg")
# 在弹出窗口中点击打开按钮
autoit.control_click("打开", "Button1")

time.sleep(10)
dr.quit()
