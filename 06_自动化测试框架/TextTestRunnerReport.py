import unittest # 导入unittest模块

# 通过TestLoader()对象的.discover实例化TestSuit
st = unittest.TestLoader().discover("./", "parameter*.py")

# 1、写入方式打开测试报告文件
fl = open("./testReport.txt", "w", encoding="utf8")

# 2、实例化TextTestRunner，写入测试报告文件
txtRunner=unittest.TextTestRunner(stream=fl, verbosity=2)

# 3、TextTestRunner对象调用run
txtRunner.run(st)

# 4、关闭文件对象
fl.close()