# 导包
import requests

addr = "http://ihrm-test.itheima.net/api/sys/login"
js = {"mobile": "13800000002", "password": "123456"}

# 发送post请求，传入json参数
response = requests.post(url=addr,json=js)
print(response.json())
