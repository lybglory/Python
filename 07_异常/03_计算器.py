try:
    n1 = int(input("请输入第1个整数："))
    n2 = int(input("请输入第2个整数："))
    opt = input("请输入操作符(+-*/)：")
    if opt == "+":
        print(n1 + n2)
    if opt == "-":
        print(n1 - n2)
    if opt == "*":
        print(n1 * n2)
    if opt == "/":
        print(n1 / n2)
except ValueError:
    print("请输入整数的数字!")
except ZeroDivisionError:
    print("除数不能为零！")
