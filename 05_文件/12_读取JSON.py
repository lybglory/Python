# 1.导入json模块
import json

# 2.读取方式打开json
jn = open("./data.json", "r", encoding="utf8")
# 3.读取内容，json.load(json对象)返回字典
data = json.load(jn)
# 4，关闭json
jn.close()

#  拆包方式遍历字典,字典.items()返回的是元组
for k, v in data.items():
    print(k, v)

