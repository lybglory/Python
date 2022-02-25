class Animal(object):
    # 类属性
    mName = "Animal"

    def __init__(self, age=0):
        # 对象的属性
        self.mAge = age

# 通过类名访问类属性
print(Animal.mName)  # Animal

# 对象的属性，只能通过对象来调用
a = Animal( 2)
print(a.mAge) # 2
