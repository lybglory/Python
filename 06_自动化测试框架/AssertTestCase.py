import random
import unittest


# 模块级前置函数
def setUpModule():
    print("SetUpModule前置方法调用")


# 模块级后置函数
def tearDownModule():
    print("TearDownModule前置方法调用")


def GetSum(n1, n2):
    return n1 + n2


def GetFiveRand():
    # 返回 [1, 5] 闭区间的任意整数
    return random.randint(1, 5)


class MyTest(unittest.TestCase):
    def test_001(self):
        rec = GetSum(100, -99)
        # 断言，判断实际结果和预期结果是否一样
        self.assertEqual(rec, 1)

    def test_002(self):
        rec = GetSum(100, -98)
        # 断言，判断实际结果和预期结果是否一样
        self.assertEqual(rec, 2)

    def test_003(self):
        rec = GetFiveRand()
        # assertIn断言，判断实际结果是否在预期结果列表中
        self.assertIn(rec, [1, 2, 3, 4, 5])
