# 导包
import requests

# 发送post请求
# http://localhost/index.php?m=Home&c=User&a=do_login
addr = "http://localhost/index.php?m=Home&c=User&a=do_login"
dt = {"username" : "18888888888","password" : "123456", "verify_code" : "8888"}

response = requests.post(url=addr, data=dt)
print(response.json())

import requests
response = requests.put("http://www.baidu.com", data={"key": "value"})
response = requests.delete("http://www.baidu.com")
response = requests.head("http://www.baidu.com")
response = requests.options("http://www.baidu.com")