
ls = []
ls.append("虎")
ls.append("猪")
ls.append("马")
ls.append("马")
ls.append("羊")
print(ls)

ls.pop()
print(ls)

del (ls[3])
print(ls)

ls.remove("马")
print(ls)

ls[0] = "虎年"
print(ls)