# 1.导入json模块
import json
# 2.读取方式打开json
j1 = open("./data.json", "r", encoding="utf8")
# 3.读取内容，json.load(json对象)返回字典
data1 = json.load(j1)
j1.close()

data2 = {"中文名": "小新", "爱好": "美女"}
for k, v in data2.items():
    # 数据插入到data1
    data1[k] = v

# 写入方式打开json，“a”追加模式会在末尾追加
j2 = open("./data.json", "w", encoding="utf8")

# 不转义写入json
json.dump(data1, j2, ensure_ascii=False)
j2.close()
