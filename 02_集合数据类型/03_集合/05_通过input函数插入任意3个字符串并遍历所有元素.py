st = set()
i = 0
while i < 3:
    print("请输入第%d个字符串" % (i + 1), end="")
    st.add(str(input(":")))
    i += 1
for e in st:
    # 集合元素的是无序的
    print(e, end=" ")
