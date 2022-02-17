dic = {"name": "新之助", "age": 6, "high": "1.1"}
# 方法1：直接for循环遍历
for key in dic:
    print(key, dic[key])

# 方法2：拆包方式遍历
for kv in dic.items():
    # 对元组进行拆包
    k, v = kv
    print(k, v)
# 方法2进一步简化
for a, b in dic.items():
    print(a, b)
