import unittest
import random
# 导入参数化模块
from parameterized import parameterized

def GetSum(n1, n2):
    return n1 + n2

class MyTest(unittest.TestCase):
    # 类级Fixture
    @classmethod
    def setUpClass(cls):
        print("类级别前置方法")

    # 参数也可定义成列表类型变量
    # 列表成员是元组
    # 列表最后一个元组，故意设置错误
    ls = [(10, 5, 15), (15, 5, 20), (20, 5, 30)]

    # 参数a表示调用GetSum第一个参数
    # 参数b表示调用GetSum第二个参数
    # 参数c表示调用GetSum函数的预期结果
    @parameterized.expand(ls)
    def test_001(self, a, b, c):
        rec = GetSum(a, b)
        self.assertEqual(rec, c)

    # 跳过
    @unittest.skip
    def test_002(self):
        print("开发ing")
