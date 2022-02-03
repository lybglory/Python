ls = ["中国", "日本", "韩国"]
tp = ("带英", "美利坚", "土澳")
print(ls)
print(tp)
i = 0
for t in tp:
    ls.insert(i, t)
    i += 1
print(ls)
