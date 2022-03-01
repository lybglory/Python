# 读取文件模式打开文件，获取文件内容
fl =open("./letter.txt", "r", encoding="utf8")
content=fl.read()
print(content)
# 对酒当歌，我学python
fl.close()

# 写模式打开文件
fl=open("./cpLetter.txt", "w", encoding="utf8")
fl.write(content)
fl.close()

# 验证一下：读取文件模式打开文件，获取文件内容
fl =open("./cpLetter.txt", "r", encoding="utf8")
txt=fl.read()
print(txt)
fl.close()