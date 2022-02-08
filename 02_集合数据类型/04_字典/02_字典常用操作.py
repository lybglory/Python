dic = {"name": "刘备", "age": 6, "high": "1.1"}
print(dic)
# 修改
dic["name"] = "汤圆"
print(dic)
# 增加
dic["sex"] = "男"
print(dic)
# 删除
dic.pop("high")
print(dic)
# 清空
dic.clear()
print(dic)
dc = {"江雪": "柳宗元", "静夜思": "李白", "悯农": "李绅"}
# 得到具体键值
print(dc["江雪"])
