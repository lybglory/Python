fl = open("./letter3.txt", "r", encoding="utf8")
txt=fl.read()
print(txt)
fl.close()

# 效果一样的
with open("./letter3.txt", "r", encoding="utf8") as f:
    text=f.read()
    print(text)
