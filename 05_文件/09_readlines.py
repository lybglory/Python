# 读取模式，打开letter3.txt文件
fl = open("./letter3.txt", "r", encoding="utf8")
# readlines()返回列表
ls=fl.readlines()
fl.close()
for e in ls:
    print(e, end="")