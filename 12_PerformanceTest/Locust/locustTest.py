# 定义任务
# 定义登录
def login(l):
    l.client.post("/login", data={"username": "admin", "password": "123456"})

# 首页
def index(l):
    l.client("/index")

# 获取用户信息
def profile(l):
    l.client.get("/profile")

# 退出
def logout(l):
    l.client.post("/logout")

# 定义任务集
from locust import TaskSet  # 从locust库中导入任务集的类
class UserBehavior(TaskSet):
    tasks = {index:3, profile:1}
    # 在所有用户行为脚本前执行，类似与setup
    def on_start(self):
        login(self)
    # 在所有用户行为脚本后执行，类似于teardown
    def on_stop(self):
        logout(self)

# 先从locust包导入HttpLocust用户类
from locust import HttpLocust
# 定义locust类
class UserWebsite(HttpLocust):
    # task_set固定写法，把定义任务集的类名复制给task_set
    task_set = UserBehavior
    # 发送请求时的最小时间间隔
    min_wait = 1000
    # 发送请求时的最大时间间隔
    max_wait = 1500
    # 检测系统的根URL
    host = "http://bms-test.itheima.net/bms"

    # 权重：当前有多个用户类（线程组）来执行时，
    # 通过这个权重来控制不同用户类之间的请求比例
    weight = 10