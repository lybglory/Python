import unittest
from HTMLTestRunner import HTMLTestRunner

# 通过TestLoader()对象的.discover实例化TestSuit
st = unittest.TestLoader().discover("./", "Exercise*.py")

#  1、二进制写入方式打开文件
fl =  open("./HTMLReport.html", "wb")

# 2、实例化HTMLTestRunner，写入测试报告文件
txtRunner=HTMLTestRunner(stream=fl, title="Digital测试报告")

# 3、调用run，执行用例
txtRunner.run(st)

# 4、关闭文件对象
fl.close()
