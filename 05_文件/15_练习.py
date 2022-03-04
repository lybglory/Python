# 创建文件number.txt一共100行,每行内容为001、002…
fl = open("./number.txt", "w", encoding="utf8")
n=1
while n<=100:
    fl.write("%03d\n" %n)
    n+=1
fl.close()
