str = "TigerYear"
# 左闭右开，不包含结束索引位置
print(str[0:5:1])  # Tiger

# 省略开始索引,默认从0开始
# 截取从开始~5位置的字符串
print(str[:5])  # Tiger

# 省略结束索引,默认到最后,省略步长,默认步长为1
# 截取5~末尾的字符串
print(str[5:])  # Year
# 截取完整字符串
print(str[:])   # TigerYear

# 从开始位置，每隔2个字符取一个
print(str[::3])   # Tee

# 从开始位置，每2个字符为一组，截取第一个字符
print(str[::2])   # Tgrer

# 从索引2开始，每隔⼀个取⼀个
print(str[2::2])   # grer

# 截取字符串末尾两个字符
print(str[-2:])    # ar

# 字符串的逆序（⾯试题）
print(str[::-1])    # raeYregiT

#       0       1       2       3
ls = ["小新", "广志", "美伢", "小葵"]
# 从开始位置，每隔⼀组截取
print(ls[::2])
# ['小新', '美伢']

print(ls[1::2])
# ['广志', '小葵']


