import random
n=random.randint(1,3)
if n==1:
    pc="石头"
elif n==2:
    pc="剪刀"
else:
    pc="布"

pl=input("请输入【石头、剪刀、布】：")
if pl=="石头" or pl=="剪刀" or pl=="布" :
    if (pl=="石头" and pc=="剪刀") or(pl=="剪刀" and pc=="布") or(pl=="布" and pc=="石头"):
        print("我出了%s,电脑出了%s,哥赢了" %(pl,pc))
    elif pl==pc:
        print("我出了%s,电脑出了%s,平局" % (pl, pc))
    else:
        print("我出了%s,电脑出了%s,哥输了" % (pl, pc))
else:
     print("输入有误！重新输入")


