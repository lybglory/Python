import requests
# 获取响应验证码请求数据
response = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
print(response.cookies) # 查看cookies

PHPSESSID = response.cookies.get("PHPSESSID")
print(PHPSESSID)

login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {"username": "18888888888",
              "password": "123456","verify_code": "8888"}

# 设置cookie
cookies = {"PHPSESSID" : PHPSESSID}

response = requests.post(url=login_url, data=login_data, cookies=cookies)
print(response.json())

orderLink="http://localhost/Home/Order/order_list.html"
response = requests.get(orderLink, cookies=cookies)
print(response.text)
