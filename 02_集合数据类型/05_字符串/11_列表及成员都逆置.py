ls = ["梅西", "巴黎", "瓜秃", "曼城"]
# 列表逆置
sl = ls[::-1]
print(sl)
# ['曼城', '瓜秃', '巴黎', '梅西']
# 成员逆转
pos = 0
for e in sl:
    str = e[::-1]
    if pos <= len(sl):
        sl[pos] = str
        pos += 1
print(sl)
# ['城曼', '秃瓜', '黎巴', '西梅']