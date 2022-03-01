import json
# 读取模式打开json
j1 = open("./data.json", "r", encoding="utf8")
dic = json.load(j1)
j1.close()
dic["中文名"] = "新之助"
# 写入模式打开json
j2 = open("./data.json", "w", encoding="utf8")
json.dump(dic, j2, ensure_ascii=False)
j2.close()