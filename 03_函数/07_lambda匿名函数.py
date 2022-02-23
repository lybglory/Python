# 求和匿名函数
GetSum = lambda n1, n2: n1 + n2
sum = GetSum(32, 8)
print(sum)


# 两个整数求最大值
# 普通函数的实现
def GetMax(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

print(GetMax(2017, 2022))  # 2022

# 匿名函数的实现
num = (lambda n1, n2: n1 if n1 > n2 else n2)(2017, 2022)
print(num)  # 2022
