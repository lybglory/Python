# 1、导入模块
import unittest

def GetMinus(n1, n2):
    return n1 - n2

def IsStr(str):
    if str.isalpha():
        return ("%s是纯字母" %str)
    else:
        return ("%s不是纯字母" %str)


# 2.实现一个类，继承自unittest.TestCase
class MyTest02(unittest.TestCase):
    # 3、类中每个方法代表一个测试用例,
    # 方法名必须以test开头
    def test_001(self):
        print(GetMinus(1990, 32))

    def test_002(self):
        print(GetMinus(2022, 2017))

    def test_003(self):
        print(IsStr("tigerYear"))

