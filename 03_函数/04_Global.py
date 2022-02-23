sex = "None"
def GetSex(code):
    global sex
    if code == 1:
        sex = "man"
    elif code == 0:
        sex = "female"
    else:
        sex = "man"

print("调用之前sex=%s" %sex)
str=input("请输入性别编号(0：female  1:man):")
if str.isdigit():
    n=int(str)
else:
    n=0
GetSex(n)
print("调用之后sex=%s" %sex)
