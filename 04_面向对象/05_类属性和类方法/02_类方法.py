class Animal(object):
    # 类属性
    mName="Animal"
    # 类方法
    @classmethod
    def SetName(cls,name):
        # 类方法通过形参修改类属性
        cls.mName=name
        # 类方法中不能调用普通方法(不能通过self方式调用)
        # 类方法只能访问同一个类中类方法和类属性

    def __init__(self,age):
        self.mAge=age

    # 普通方法
    def ShowInfo(self):
        print("普通方法：%s,%s" %(Animal.mName,self.mAge))

# 通过类名调用类方法
Animal.SetName("福来")
# 通过类名直接修改类属性的值
Animal.mName="黑虎"
# 通过类名访问类属性
print(Animal.mName)  # 福来

# 对象的属性，只能通过对象来调用
a = Animal(5)
a.mAge=10
a.ShowInfo() # 普通方法：黑虎,10
