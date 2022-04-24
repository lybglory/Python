import time #导入时间模块
import unittest # 导包
from  HTMLTestRunner import HTMLTestRunner
# 导入测试类
from loginAPI import LoginTest
# 实例化测试套件
st = unittest.TestSuite()
# 把测试用例添加到测试套件
st.addTest(unittest.makeSuite((LoginTest)))

report = "./report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))
# 生成测试报告,打开文件流
with open(report, "wb") as fl:
    # 创建HTMLTestRunner运行器
    htmlRunner = HTMLTestRunner(stream=fl, title="登录接口测试")
    # 执行测试套件
    htmlRunner.run(st)

