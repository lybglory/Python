# 通过input 函数，输入一个字符串，
# 判断字符串是否可以转化为整数，
# 如果不可以转化, 显示"请输入数字"

str1 = input("请输入第一个数字：")
str2 = input("请输入第二个数字：")
if str1.isdigit() and str2.isdigit():
    n1 = int(str1)
    n2 = int(str2)
    print("%d-%d=%d" % (n1, n2, n1 - n2))
else:
    print("二货，输入的字符不是纯数字！")
