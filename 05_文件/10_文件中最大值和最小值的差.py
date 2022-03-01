fl = open("./math.txt", "w", encoding="utf8")
fl.write("2022\n2019\n2017\n2020\n1990")
fl.close()
fl = open("./math.txt", "r", encoding="utf8")

# 定义一个空列表，用来接收转成int的行内容
ls=[]
while True:
    # 按行读取
    txt=fl.readline()
    if txt=="" :
        break
    ls.append(int(txt))
fl.close()
nMax = max(ls)
nMin = min(ls)
n = nMax - nMin
print("%s-%s=%s" % (nMax, nMin, n))
