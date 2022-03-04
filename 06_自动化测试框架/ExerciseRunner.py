import unittest
from HTMLTestRunner import HTMLTestRunner

# 实例化suitCase
st = unittest.TestLoader().discover("./", "Exercise.py")

# 二进制写入方式打开html文件(不需要指定字符集)
fl = open("./Digital.html", "wb")


# 实例化TextTestRunner(自带的生成测试报告方法)
#textRunner=unittest.TextTestRunner()

# 实例化HTMLTestRunner
htmlRunner = HTMLTestRunner(stream=fl, title="digital函数测试报告")

# 调用HTMLTestRunner对象的run方法
htmlRunner.run(st)

# 关闭文件对象
fl.close()

