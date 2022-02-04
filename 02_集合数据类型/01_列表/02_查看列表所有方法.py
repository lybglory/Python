# dir(列表变量名)
print(dir(list))
list1 = ["李白", "柳宗元", "王之涣"]
list2 = ["静夜思", "江雪", "登鹳雀楼"]
list1.insert(1, "杜甫")
list2.insert(1, "春望")
print(list1, list2)
list1.extend(list2)
print(list1)

list1.append("玉斌")
print(list1)

list1[2]="李白"
print(list1)

list1.pop()
print(list1)

list1.remove("杜甫")
list2.remove("春望")

list1.reverse()
print(list1)

list1.sort()
print(list1)

print(list1.count("李白"), list1.index("李白"))


