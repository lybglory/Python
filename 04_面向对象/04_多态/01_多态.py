class Human:
    def __init__(self, peop):
        self.people=peop
    # 公共方法，用于子类重写
    def Say(self):
        pass

    # 用于子类调用各自重写的Say()方法，实现多态
    def Speak(self):
        self.Say()

class China(Human):
    # 重写父类公用的Say()方法
    def Say(self):
        print("%s is speaking" %self.people)

class Japan(Human):
    # 重写父类公用的Say()方法
    def Say(self):
        print("%s is speaking" %self.people)

cn=China("Chinese")
cn.Speak()  # 调用父类的Speak()方法
# Chinese is speaking

jp=Japan("小日本")
jp.Speak()  # 调用父类的Speak()方法
# Chinese is speaking
