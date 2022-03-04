# 1、导入模块
import unittest

# 2、通过TestLoader()对象的.discover实例化TestSuit
st = unittest.TestLoader().discover("./", "parameter*.py")

# 3、实例化TextTestRunner
txtRunner=unittest.TextTestRunner()

# 4、TextTestRunner对象调用run
txtRunner.run(st)





