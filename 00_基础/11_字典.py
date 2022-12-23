#encoding=utf-8
dic = {"name": "刘备", "age": 6, "high": "1.1"}
print(dic)
# 修改
dic["name"] = "汤圆"
print(dic)
# 增加
dic["sex"] = "男"
print(dic)
# pop删除
dic.pop("high")
print(f"dic.pop()删除：\n{dic}")

del dic["age"]  # del删除
print(f"del dic['age']删除：\n{dic}")
# 查

# 清空
dic.clear()
print(dic)
dc = {"江雪": "柳宗元", "静夜思": "李白", "悯农": "李绅"}
# 得到具体键值
print(dc["江雪"])
