# 数据类型转换
# 1.float()转换成浮点型
num1 = 1
print(float(num1))  # 1.0
print(type(float(num1)))  # <class 'float'>

# 2.str()转换成字符串类型
num2 = 10
print(type(str(num2)))  # <class 'str'>

# 3.tuple()将⼀个序列列转换成元组
list1 = [10, 20, 30]
print(tuple(list1))  # (10, 20, 30)
print(type(tuple(list1)))  # <class 'tuple'>
# 4.list()将⼀个序列列转换成列列表
t1 = (100, 200, 300)
print(list(t1))  # [100, 200, 300]
print(type(list(t1)))  # <class 'list'>

# 5. eval() -- 将字符串中的数据转换成Python表达式原本类型
str1 = '10'
str2 = '[1, 2, 3]'
str3 = '(1000, 2000, 3000)'
print(type(eval(str1)))  # <class 'int'>
print(type(eval(str2)))  # <class 'list'>
print(type(eval(str3)))  # <class 'tuple'>
