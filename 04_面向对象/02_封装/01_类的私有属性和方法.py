class Person:
    def __init__(self,name="Messi",age=32):
        # __mAge为类的私有属性
        self.mName=name
        self.__mAge=age

    # 类的私有方法
    def __PrivFunc(self):
        print("name=%s, age=%d" %(self.mName,self.__mAge))

    def ShowInfo(self,name="NPC"):
        self.__PrivFunc()


p=Person(age=35)
# 不能在类的外部访问类的私有属性、方法
# p.__mAge #错误代码
p.ShowInfo()
