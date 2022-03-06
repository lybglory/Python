try:
    n1 = int(input("请输入第一个数字"))
    n2 = int(input("请输入第二个数字"))
    print(n1 + n2)
except Exception as result:
    print(result)
finally:
    # 无论是否有异常，都会执行
    print("程序执行完毕!")

# 请输入第一个数字2022
# 请输入第二个数字po
# invalid literal for int() with base 10: 'po'
# 程序执行完毕!