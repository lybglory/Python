try:
    n1 = int(input("请输入第一个数字"))
    n2 = int(input("请输入第二个数字"))
    print(n1 + n2)
except Exception as result:
    print(result)
else:
    print("Very good,输入正确！")

# 请输入第一个数字2022
# 请输入第二个数字-1990
# 32
# Very good,输入正确！
