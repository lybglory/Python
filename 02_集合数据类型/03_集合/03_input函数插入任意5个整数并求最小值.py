# input函数插入任意5个整数并求最小值
st = set()
i = 0
while i < 5:
    print("请输入第%d个整数" % (i+1), end="")
    st.add(int(input(":")))
    i += 1
print(st)
print("最小元素是%d" % (min(st)))