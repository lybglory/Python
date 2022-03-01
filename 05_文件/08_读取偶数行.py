# 读取模式，打开letter3.txt文件
fl = open("./letter3.txt", "r", encoding="utf8")
lineNum = 1
while True:
    lnContext = fl.readline()
    # 按行去读内容，如果当前读到的行是结尾，中止
    if lnContext == "":
        break
    if lineNum % 2 == 0:
        print(lnContext, end="")
    lineNum += 1
fl.close()