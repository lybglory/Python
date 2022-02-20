# id = 1
# name = "小新"
# high = 1.1
# addr = "tokey JAPN"
# 以上变量实现如下效果：
###############
# 编号：00001
# 姓名：小新
# 身高：1.1m
# 地址：tokey JAPN
###############
id = 1
name = "小新"
high = 1.1
addr = "tokey JAPN"
print("*"*15)
print("编号：%05d" %id)
print("姓名：%s" %name)
print("身高：%.1fm" %high)
print("地址：%s" %addr)
print("*"*15)
