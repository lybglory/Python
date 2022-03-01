# 打开文件，返回文件对象
fl = open("./01_读文件.py", "r", encoding="utf8")
# 读取文件内容
txt = fl.read()
print(txt)
# 3.关闭文件
fl.close()