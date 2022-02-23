str = "None"
sx = "None"


# 缺省参数
def SetInfo(name, sex="man"):
    global str, sx
    str = name
    sx = sex


SetInfo("Messi")
print(str, sx)  # Messi man


def ShowInfo(name="NPC", sex="female", age=18):
    print(name, sex, age)

ShowInfo()  # NPC female 18
