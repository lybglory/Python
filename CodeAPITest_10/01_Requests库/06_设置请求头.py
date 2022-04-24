# 1. 请求IHRM项目的登录接口，URL： http://ihrm-test.itheima.net/api/sys/login
# 2. 请求头： Content-Type: application/json
# 3. 请求体： {"mobile":"13800000002", "password":"123456"}
import requests

link = "http://ihrm-test.itheima.net/api/sys/login"
requHead={"Content-Type" : "application/json"}
userData={"mobile":"13800000002", "password":"123456"}

response = requests.post(url=link, headers=requHead,json=userData)
print(response.json())