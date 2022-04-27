import time
from selenium import webdriver  # 1.导包
from selenium.webdriver.common.by import By

# 2.浏览器驱动实例化
dr = webdriver.Edge()

# 3.业务操作
dr.get("file:///C:/App/pagetest/registerA.html")
dr.maximize_window()    # 窗口最大化
# 通过css层级选择器获取[注册]按钮的大小
print(dr.find_element(By.CSS_SELECTOR, "p>button").size)
# 输出结果是字典：{'height': 41, 'width': 158}

# 通过css_id选择器定位[访问新浪网站]的文本
print(dr.find_element(By.CSS_SELECTOR, "#fw").text)
# 输出结果是字典：访问 新浪 网站

# <a href="http://www.sina.com.cn" id="fw" target="_blank">访问 新浪 网站</a>
# 通过css_id选择器获取[访问新浪网站]href的属性值
print(dr.find_element(By.CSS_SELECTOR, "#fw").get_attribute("href"))
# 输出结果：http://www.sina.com.cn/

# <span name="sp1">我隐身了</span>
# 通过name定位该元素是否显示，默认是False
print(dr.find_element(By.NAME, "sp1").is_displayed())
# 输出结果：False

# <input type="reset" value="取消" disabled="disabled" id="cancelA">
# 通过id定位该元素是否可用，默认是False
print(dr.find_element(By.ID, "cancelA").is_enabled())

# <input type="checkbox" name="hobby" value="旅游" id="lyA" checked="checked">
# 通过id定位该复选框元素是否被选中,默认是True
print(dr.find_element(By.ID, "lyA").is_selected())

time.sleep(3)
dr.quit()
