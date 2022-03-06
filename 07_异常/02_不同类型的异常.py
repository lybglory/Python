try :
    n1 = int(input("请输入第一个整数："))
    n2 = int(input("请输入第二个整数："))
    print(n1 / n2)
except ValueError:
    print("输入的字符串不能有效转换为整数")
except ZeroDivisionError:
    print("除数不能为0")
