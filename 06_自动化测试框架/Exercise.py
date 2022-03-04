# 测试digital函数是否正确,函数定义如下
# 参数str1为任意一个字符串;
# 函数返回值为参数str1中包含的数字个数;
# 如 参数str1的值为”sdfsdfsdf12”, 函数返回值为2;
# 如 参数str1的值为”hello”,函数返回值为0;
import unittest
from parameterized import parameterized


def digital(str1):
    sum = 0
    for n in str1:
        if n >= "0" and n <= "9":
            sum += 1
    return sum


ls = [("python3.1", 2), ("year2022", 4), ("date304", 3)]


class Digital(unittest.TestCase):
    # 列表里的元素是元组，元组最后一个数字表示预期的结果
    # 一个元素对应一个测试用例
    @parameterized.expand(ls)
    def test_001(self, a, b):
        rec = digital(a)
        self.assertEqual(rec, b)
