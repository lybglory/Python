# 导包
import requests

# 直接传递
# response=  requests.get("http://localhost/Home/Goods/search.html?q=iphone")

# 参数字典传递
addr = "http://localhost/Home/Goods/search.html"
dic = {"q": "iphone"}
# response = requests.get(url=addr, params=dic)

# 参数字符串传递
strAddr = "http://localhost/Home/Goods/search.html"
strParam = "q=iphone"
response = requests.get(url=strAddr, params=strParam)

print(response.text)
