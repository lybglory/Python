class Person:
    # 默认构造函数
    def __init__(self, name="Messi",age=32):
        self.m_name=name
        self.m_age=age

    def ShowInfo(self):
        print("name=%s;age=%d" %(self.m_name,self.m_age))

p1=Person()
p1.ShowInfo()   # name=Messi;age=32
print(p1.m_name)

class Animal:
    def Eat(self):
        print("在恰饭")

    def Drink(self):
        print("在喝水")