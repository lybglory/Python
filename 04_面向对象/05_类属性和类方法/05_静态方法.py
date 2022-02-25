class Person:
    # 静态方法，交换列表前两个元素
    @staticmethod
    def Swape(ls):  # 形参是列表会影响实参的值
        if len(ls) >= 2:
            temp = ls[1]
            ls[1] = ls[0]
            ls[0] = temp
        else:
            print("交换失败！")


class China:
    @staticmethod
    def Swape():
        print("这是China的静态方法")


l = [2019, 2022]
Person.Swape(l)
print(l)  # [2022, 2019]

# 静态方法可以避免函数重名带来的错误
China.Swape()
# 这是China的静态方法
