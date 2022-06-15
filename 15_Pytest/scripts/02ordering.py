# 使用pytest-ordering插件就需要导入pytest模块
import pytest


def add(x, y):
    return x + y


version = 21


class TestAdd:
    @pytest.mark.last  # 设置用例最后执行
    def test_add_01(self):
        result = add(1, 2)
        assert 3 == result

    @pytest.mark.run(order=0)
    def test_add_02(self):
        result = add(2, 2)
        assert 4 == result

    @pytest.mark.run(order=-2)
    def test_add_03(self):
        result = add(3, 2)
        assert 5 == result

    @pytest.mark.skipif(version > 20, reason="大于2.0的版本不需要再执行此用例")
    def test_add_04(self):
        result = add(4, 2)
        assert 6 == result

    @pytest.mark.skip("不需要执行此用例")
    def test_add_05(self):
        result = add(5, 2)
        assert 7 == result

    def test_add_06(self):
        assert 9 == add(6, 2)
