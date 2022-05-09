# 导入显示等待元素模块
from selenium.webdriver.support.wait import WebDriverWait
class Tools:
    # 减少代码量，显示等待来定位方法进行封装
    # （类方法，不需要实例化，通过类名调用即可）
    @classmethod
    def getElement(cls, driver, findParams ):
        element = WebDriverWait(driver, 10, 1).until(
            lambda e:e.find_element(findParams[0], findParams[1]) )
        return element

    # 输入的封装，传入元素对象、要输入的文本内容
    @classmethod
    def inputText(cls, element, text):
        """
        :param element: 元素对象
        :param text: 需要输入的文本
        :return:
        """
        element.clear()         # 先清空输入框
        element.send_keys(text) # 在输入文本

