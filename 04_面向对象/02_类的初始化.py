class Person:
    # 初始化函数
    def __init__(self,name="Python"):
        self.m_name=name
        print("这是类的初始化方法")

    def __del__(self):
        print("这是销毁函数")

p1=Person()  # 这是类的初始化方法
print("p1.m_name=%s" %(p1.m_name))
# p1.m_name=Python

print("==end==")
# ==end==
# 最后输出：这是销毁函数

