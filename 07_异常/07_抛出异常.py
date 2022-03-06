try:
    passwd = input("请输入6位密码：")
    if len(passwd) < 6:
        raise Exception("密码长度少于6位!")
    else:
        print("长度OK!")
except Exception as result:
    print(result)
# 请输入6位密码：tiger
# Exception: 密码长度少于6位!