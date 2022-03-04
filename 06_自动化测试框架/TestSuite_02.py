# 1、导入模块
import unittest
# 2、导入其他包含测试用例的py文件
import  TestCase_01
import  TestCase_02

# 3、实例化testSuite
st= unittest.TestSuite()
# 4、tsetSuite对象调用添加用例
# st.addTest(TestCase_01.MyTest("test_001"))
# st.addTest(TestCase_01.MyTest("test_002"))

# 用unittest.makeSuite一次导入一个类中的所有测试方法
st.addTest(unittest.makeSuite(TestCase_01.MyTest))
st.addTest(unittest.makeSuite(TestCase_02.MyTest02))

# 实例化TextTestRunner
runner= unittest.TextTestRunner()
# 调用run方法
runner.run(st)


