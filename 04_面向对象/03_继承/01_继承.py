class Country:
    # 初始化函数
    def __init__(self, type="CN",technic="None"):
        self.mType = type
        self.__mTechnic=technic

    def ShowType(self):
        print("%s, %s" % (self.mType,self.__mTechnic))

# 继承自Country父类，就继承了父类中的所有(非私有)属性和(非私有)方法
class Japan(Country):
    # 子类继承了父类的初始化函数
    pass    # 占位符

jp = Japan("狗日的日本")
jp.ShowType()
# 狗日的日本, None
