# 导入显示等待元素模块
from selenium.webdriver.support.wait import WebDriverWait
import time
class Tools:
    # 类方法，不需要实例化，通过类名调用即可
    # 减少代码量，显示等待来定位方法进行封装，返回定位的元素
    # findParams表示find_element()的两个参数：By.XX,“对应的参数”，用元组传入
    @classmethod
    def getElement(cls, driver, findParams):
        element = WebDriverWait(driver, 10, 1).until(
            lambda e: e.find_element(findParams[0], findParams[1]))
        return element

    # 输入的封装，传入元素对象、要输入的文本内容
    @classmethod
    def inputText(cls, element, text):
        element.clear()  # 先清空输入框
        element.send_keys(text)  # 再输入文本

    # 判断元素是否存在
    # 传入驱动对象、find_element方法的参数，这样传入的不是元素对象，避免传参的时候报错
    @classmethod
    def elementIsExist(cls, driver, findEleParams):
        try:
            cls.getElement(driver, findEleParams)
            return True
        except Exception as result:
            print(result)
            return False

    # 滑动方法的封装（参数:驱动对象、方向、可选参数滑动次数）
    @classmethod
    def swipeHandle(cls, driver, direction, swipeCount=1):
        # 获取手机屏幕的宽度
        h = driver.get_window_size()["height"]
        # 获取手机屏幕的高度
        w = driver.get_window_size()["width"]
        # 向上滑动，X轴不变，Y轴坐标变化由大到小
        if direction == "top":
            pos = (w / 2, h * 0.9, w / 2, h * 0.1)
        # 向下滑动，X轴不变，Y轴坐标变化由小到大
        elif direction == "down":
            pos = (w / 2, h * 0.1, w / 2, h * 0.9)
        # 向左滑动，X轴变化由大到小，Y轴不变
        elif direction == "left":
            pos = (w * 0.9, h / 2, w * 0.1, h / 2)
        # 向右滑动，X轴变化由小到大，Y轴不变
        elif direction == "right":
            pos = (w * 0.1, h / 2, w * 0.9, h / 2)
        for i in range(0, swipeCount):
            driver.swipe(*pos, duration=1500)
            time.sleep(1)

    # 边滑动边查找的封装（参数:驱动对象、滑动区域块元素对象、find_element方法的参数）
    # 区域内滑动，Y轴坐标的值不变，居中。只改变x坐标的值，实现左右滑动
    @classmethod
    def swipeAndFind(cls, driver, scrollBlockEle, findTargetParams):
        scrollBlockSize = scrollBlockEle.size    # 获取滑动区域块的大小
        h = scrollBlockSize["height"]           # 获取滑动区域块的宽度
        w = scrollBlockSize["width"]            # 获取滑动区域块的高度
        scrollBlockPos = scrollBlockEle.location # 获取滑动区域块的坐标位置
        x = scrollBlockPos["x"]                 # 获取区域快左上角x的坐标值
        y= scrollBlockPos["y"]                  # 获取区域快左上角y的坐标值
        start_x = x + w*0.9                     # 设置滑动起始点X的值
        y = y + h*0.5                           # 设置滑动Y的值。(中间位置)
        end_x = x + w*0.1                       # 设置滑动终点X的值
        while True:
            # 记录page_source返回页面源码，通过对比页面资源来退出死循环
            pages = driver.page_source
            try:
                # findTargetParams 参数是元组：By.xxx,"属性值"
                # 如果定位到该元素，那么点击并返回True
                driver.find_element(*findTargetParams).click()
                print("找到了元素")
                return True
            except Exception as result:
                print("没有找到该元素!")
                # 没有元素，则滑屏
                driver.swipe(start_x, y, end_x, y, duration=1000)
                time.sleep(1)
                # 直到返回源码信息相同的时候，表示滑到了结尾
                if pages == driver.page_source:
                    print("滑动结束，未找到元素信息")
                    return False