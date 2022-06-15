def getSum(n1, n2):
    return n1 + n2

class TestLogin:
    def setup_class(self):
        print("pytest类级前置函数")
    def teardown_class(self):

        print("pytest类级后置函数")

    def setup(self):
        print("pytest方法级前置函数")

    def teardown(self):
        print("pytest方法级后置函数")

    def test_add01(self):
        print(getSum(10, 5))

    def test_add02(self):
        print(getSum(15, 5))