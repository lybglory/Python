# 定义⼀个函数，有两个参数，start 和stop，start 代表开始范围，
# stop 代表终止范围，求这个范围中所有整数相加的和
def GetSum(start,stop):
    sum =0;
    while   start<=stop:
        sum+=start
        start+=1
    return  sum

print(GetSum(1,100)) #5 050