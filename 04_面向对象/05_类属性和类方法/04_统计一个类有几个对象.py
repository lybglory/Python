class Perosn(object):
    count = 0;  # 类属性

    def __init__(self):
        Perosn.count += 1

    @classmethod  # 类方法
    def GetCount(cls):
        return cls.count

print(Perosn.GetCount()) # 0
p1 = Perosn()
p2 = Perosn()
p3 = Perosn()
n = Perosn.GetCount()
print("Person类实例化出了%d个对象" % n)
# Person类实例化出了3个对象
