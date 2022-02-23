n=12
def GetDiv(n):
    # 即使是形参n和全局变量n重名
    # 形参n在这里作为局部变量
    n=n/2
    print(n)   # 6.0

GetDiv(n)   # 全局变量n作为实参传递
print(n)
# 全局变量n的值没有改变，依旧是12

# 列表、集合、字典作为参数传递，将会改变实参的值
ls =[2022, 2, 23]
def LoveDay(lst):
    lst[0]=2017
    lst[1]=6
    lst[2]=20

print(ls)    # [2022, 2, 23]
LoveDay(ls)
print(ls)   # [2017, 6, 20]
