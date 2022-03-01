# 打开文件，返回文件对象
fl = open("./02Test-Write.txt", "a", encoding="utf8")

# 写入文件
fl.write("\n对酒当歌")

# 关闭文件
fl.close()
# 文件内容显示为：
# python,so easy!
# 对酒当歌