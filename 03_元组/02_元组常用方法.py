# count
# index
# 公共方法
# len
# min
# max
# in
# not in
tuple1 = (2017, 2022, 2017, 2021, 2018, 2020)
# 常用方法
print("元素2017有%d个" % (tuple1.count(2017)))
print("元素2022的下标是%d" % (tuple1.index(2022)))
# 公用方法
print("元组中最大的元素是%d" % (max(tuple1)))
print("元组中最小的元素是%d" % (min(tuple1)))
if 2022 in tuple1:
    print("元素2022存在元组中")

if 2019 not in tuple1:
    print("元素2019不在元组中")
