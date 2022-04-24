import unittest
import requests
class LoginTest(unittest.TestCase):
    # 方法级前置方法，获取地址,创建Session对象
    def setUp(self):
        self.verifylink = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.loginlink = "http://localhost/index.php?m=Home&c=User&a=do_login"
        self.ssin = requests.Session()

    # 方法级后置方法，关闭Session对象
    def tearDown(self):
        self.ssin.close()

    # 登录成功测试用例
    def testLoginSuccess(self):
        # 获取验证码
        verifyRsp = self.ssin.get(self.verifylink)
        print("type=%s" % (verifyRsp.headers.get("Content-Type")))
        self.assertIn("image", verifyRsp.headers.get("Content-Type"))

        # 登录请求数据
        userdata = {"username": "18888888888",
                    "password": "123456", "verify_code": "8888"}

        # tpshop项目登录接口传入的是表单数据，参数要用data
        loginRsp = self.ssin.post(url=self.loginlink, data=userdata)
        loginResult = loginRsp.json()
        print(loginResult)
        # 对登录接口响应状态码断言
        self.assertEqual(200, loginRsp.status_code)
        # 对登录接口响应数据进行断言
        self.assertEqual(1, loginResult.get("status"))
        self.assertIn("登陆成功", loginResult.get("msg"))


    # 登录失败测试用例--手机号不存在
    def testLoginUserIsNotExist(self):
        # 获取验证码
        verifyRsp = self.ssin.get(self.verifylink)
        print("type=%s" % (verifyRsp.headers.get("Content-Type")))
        self.assertIn("image", verifyRsp.headers.get("Content-Type"))

        # 登录请求数据
        userdata = {"username": "13888888888",
                    "password": "123456", "verify_code": "8888"}

        # tpshop项目登录接口传入的是表单数据，参数要用data
        loginRsp = self.ssin.post(url=self.loginlink, data=userdata)
        loginResult = loginRsp.json()
        print(loginResult)
        # 对登录接口响应数据进行断言
        self.assertEqual(200, loginRsp.status_code)
        self.assertEqual(-1, loginResult.get("status"))
        self.assertIn("账号不存在", loginResult.get("msg"))

