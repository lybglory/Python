import unittest

# 2、查找"TestCase"开头的py文件，自动加载到TestSuite中
st = unittest.TestLoader().discover("./", "TestCase*.py")

# 3、实例化TextTestRunner()
txtRunner = unittest.TextTestRunner()

# 4、TextTestRunner实例化出来的对象调用Run方法
txtRunner.run(st)
