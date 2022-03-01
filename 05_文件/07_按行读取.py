# 读取模式，打开letter3.txt文件
fl = open("./letter3.txt", "r", encoding="utf8")
while True:
    # 按行去读内容，如果当前读到的行是结尾，中止
    if fl.readline() == "":
        break
    print(fl.readline(), end="")
fl.close()