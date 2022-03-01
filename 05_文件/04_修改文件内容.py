# 有文件a.txt
# “对酒当歌，人生几何”
# 把“人生几何”换成“我学oython”

# 写模式打开文件，指定字符集，防止乱码
fl=open("./letter.txt", "w", encoding="utf8")
fl.write("对酒当歌，人生几何")
fl.close()

# 读取文件模式打开文件，获取文件内容
fl =open("./letter.txt", "r", encoding="utf8")
txt=fl.read()
print(txt)
fl.close()

# 写模式打开文件
fl=open("./letter.txt", "w", encoding="utf8")
newTxt=txt.replace("人生几何", "我学python")
fl.write(newTxt)
fl.close()

# 验证一下：读取文件模式打开文件，获取文件内容
fl =open("./letter.txt", "r", encoding="utf8")
content=fl.read()
print(content)
fl.close()
