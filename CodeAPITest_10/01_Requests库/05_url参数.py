# 1.访问TPshop搜索商品的接口，通过查询字符串的方式传递搜索的关键字iPhone，并查看响应数据；
# 2.请求路径格式为：http://localhost/Home/Goods/search.html?q=iPhone；
import requests

link = "http://localhost/Home/Goods/search.html"

# 1、字典传入url参数
dicArgu = {"q": "iphone"}
response1 = requests.get(url=link, params=dicArgu)
# print(response1.text)

# 2、字符串传入url参数
strArgu = "q=iphone"
response2 = requests.get(url=link, params=strArgu)
print(response2.text)
