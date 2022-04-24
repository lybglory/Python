import requests
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
verifyLink = "http://localhost/index.php?m=Home&c=User&a=verify"
orderLink = "http://localhost/Home/Order/order_list.html"
login_data = {"username": "18888888888",
              "password": "123456", "verify_code": "8888"}

# 创建session对象
ssin = requests.Session()
response = ssin.get(verifyLink)

response = ssin.post(url=login_url, data=login_data)
print(response.json())

response = requests.get(orderLink)
print(response.text)
