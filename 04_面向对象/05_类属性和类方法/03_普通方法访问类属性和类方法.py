class Animal(object):
    mName="Animal"  # 类属性
    @classmethod    # 类方法
    def ShowName(cls):
        print("name=%s" %cls.mName)

    def SetName(self,name):
        # 普通方法可以通过类名访问类属性/方法
        Animal.mName=name

Animal.mName="福来"
Animal.ShowName()   # name=福来
a= Animal()
a.SetName("黑虎")
Animal.ShowName()   # name=黑虎