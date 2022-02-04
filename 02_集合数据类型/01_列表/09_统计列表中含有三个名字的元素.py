list = ["小罗", "曾磨蹭", "朱娟儿", "小雨"]
sum=0
for e in list:
    if len(e)==3 :
        sum+=1
# 输出结果：含3个字的名字有2个
print("含3个字的名字有%d个" % sum)

ls =["罗贼贼", "阿莲", "娟娟", "小雨"]
print(ls)
for i in ls:
    if i in "小雨":
        ls.remove("小雨")
# 输出结果：['罗贼贼', '阿莲', '娟娟']
print(ls)


