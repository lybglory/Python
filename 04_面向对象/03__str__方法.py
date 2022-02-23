class Dog:
    # 类的初始化方法
    def __init__(self,name="福来"):
        self.m_name=name

    def SetName(self, name):    # 设置属性的方法
        self.m_name=name

    def GetName(self):          # 获取属性的方法
        return self.m_name

    def __str__(self):
        return "name=%s" % self.m_name

dg=Dog()
print(dg)   # 打印对象