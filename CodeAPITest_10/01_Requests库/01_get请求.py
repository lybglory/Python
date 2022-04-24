# 导包
import requests

# 发送请求
response = requests.get("http://www.baidu.com")

# 查看响应数据的编码格式
print(response.encoding)
print(response.text)

# 设置响应数据的编码格式，解决乱码问题
response.encoding = "utf-8"

print(response.encoding)
print(response.text)
