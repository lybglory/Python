class Country:
    def __init__(self,name="China"):
        self.mName=name

    def ShowInfo(self):
        print("Country=%s" %self.mName)

class CN(Country):
    # 重写父类的方法
    def ShowInfo(self, des="Chinese"):
        super().ShowInfo()
        print("%s,%s" % (self.mName, des))

cn=CN()
cn.ShowInfo("热爱和平")
# Country=China
# China,热爱和平