import json
import unittest
import requests
# 导入参数化模块
from parameterized import parameterized

# 从Json文件获取测试数据
def loadData():
    testData = []  # 定义一个空列表
    filename = "./testdata.json"
    with open(filename, "r", encoding="utf8") as fl:
        jsData = json.load(fl)
        for casedata in jsData:
            username = casedata.get("username")
            password = casedata.get("password")
            verify_code = casedata.get("verify_code")
            status_code = casedata.get("status_code")
            status = casedata.get("status")
            msg = casedata.get("msg")
            testData.append( (username,password,verify_code,status_code,status,msg) )
    print(testData)
    return testData



class LoginTest(unittest.TestCase):
    # 方法级前置方法，获取地址,创建Session对象
    def setUp(self):
        self.verifylink = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.loginlink = "http://localhost/index.php?m=Home&c=User&a=do_login"
        self.ssin = requests.Session()

    # 方法级后置方法，关闭Session对象
    def tearDown(self):
        self.ssin.close()

    # 登录测试用例参数化
    @parameterized.expand(loadData())
    def testLogin(self,username,password,verify_code,status_code,status,msg):
        # 获取验证码
        verifyRsp = self.ssin.get(self.verifylink)
        print("type=%s" % (verifyRsp.headers.get("Content-Type")))
        self.assertIn("image", verifyRsp.headers.get("Content-Type"))

        # 登录请求数据
        userdata = {"username": username,
                    "password": password, "verify_code": verify_code}

        # tpshop项目登录接口传入的是表单数据，参数要用data
        loginRsp = self.ssin.post(url=self.loginlink, data=userdata)
        loginResult = loginRsp.json()
        print(loginResult)
        # 对登录接口响应状态码断言
        self.assertEqual(status_code, loginRsp.status_code)
        # 对登录接口响应数据进行断言
        self.assertEqual(status, loginResult.get("status"))
        self.assertIn(msg, loginResult.get("msg"))

