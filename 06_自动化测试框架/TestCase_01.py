# 1、导入模块
import unittest

def GetSum(n1, n2):
    return n1 + n2

def IsNum(num):
    if num.isdigit():
        return ("%s是纯数字" %num)
    else:
        return ("%s不是纯数字" %num)


# 2.实现一个类，继承自unittest.TestCase
class MyTest(unittest.TestCase):
    # 3、类中每个方法代表一个测试用例,
    # 方法名必须以test开头
    def test_001(self):
        print(GetSum(1990, 32))

    def test_002(self):
        print(GetSum(-2017, 2022))

    def test_003(self):
        print(IsNum("year1990"))

