# 写模式打开文件，指定字符集，防止乱码
fl2=open("./letter2.txt", "w", encoding="utf8")
fl2.write("譬如朝露，去日苦多")
fl2.close()

# 读取模式，打卡letter.txt文件
fl=open("./letter.txt", "r", encoding="utf8")
letter=fl.read()
print(letter)
fl.close()

# 读取模式，打卡letter2.txt文件
fl2=open("./letter2.txt", "r", encoding="utf8")
letter2=fl2.read()
print(letter2)
fl2.close()

# 将文件letter.txt和letter2.txt合并到letter3.txt
fl3=open("./letter3.txt", "w", encoding="utf8")
fl3.write(letter+"\n"+letter2)
fl3.close()
# 对酒当歌，我学python
# 譬如朝露，去日苦多