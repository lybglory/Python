# encoding=utf-8
num1, float1, str1 = 10, 0.5, 'hello world'
print(num1)
print(float1)
print(str1)

a = 100
a += 1
# 输出101 a = a + 1,最终a = 100 + 1
print(a)

b = 2
b *= 3
# 输出6 b = b * 3,最终b = 2 * 3
print(b)
c = 10
c += 1 + 2
# 输出13, 先算运算符右侧1 + 2 = 3， c += 3 , 推导出c = 10 + 3
print(c)