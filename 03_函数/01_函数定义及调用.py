def Getsum(n1, n2):
    return n1 + n2


sum = Getsum(2022, -1990)
print(sum)


# 返回参数中最大值
def GetMaxVal(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


nMax = GetMaxVal(2019, 2022)
print(nMax)  # 2022
