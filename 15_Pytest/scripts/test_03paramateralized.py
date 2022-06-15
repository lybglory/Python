import pytest   # pytest参数化装饰器需要导入pytest模块
def getSum(n1, n2):
    return n1 + n2

class TestParametrized:
    argus = "n1, n2, expect"
    testData = [(2, 3, 5), (10, 9, 19), (2010, 12, 2022)]
    @pytest.mark.parametrize(argus, testData)
    def test_01getSum(self, n1, n2, expect):
        assert expect == getSum(n1, n2)

