import unittest


# 模块级前置函数
def setUpModule():
    print("SetUpModule前置方法调用")

# 模块级后置函数
def tearDownModule():
    print("TearDownModule前置方法调用")


def GetSum(n1, n2):
    return n1 + n2


class MyTest(unittest.TestCase):
    # # 类级别
    # @classmethod
    # def setUpClass(cls) :
    #     print("setUpClass前置")
    #
    # @classmethod
    # def tearDownClass(cls) :
    #     print("tearDownClass后置方法")
    #
    # # Fixture方法级,每个测试用例执行前都会调用一次
    # def setUp(self):
    #     print("setUp前置处理")
    #
    # def tearDown(self) :
    #     print("tearDown后置处理")
    def test_001(self):
        GetSum(100, -99)

    def test_002(self):
        GetSum(99, -1)


