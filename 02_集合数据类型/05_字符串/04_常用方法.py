str = "Happy TigerYear"
# 通过下标访问字符
print("str[6]=%c" % (str[6]));

# 判断字符串是否由纯字母组成
# 如果条件成立,返回True,否则返回False
# (有空格的话返回false)
if str.isalpha():
    print("字符串都是纯字母组成")
else:
    print("字符串不是纯字母组成")

# 判断字符串是否由纯数字组成
str2 = "20220220"
if str2.isdigit():
    print("字符串是纯数字组成的")

# 判断字符串是否全部大写
str3 = "TIGER YEAR"
if str3.isupper():
    print("字符串'%s'全是大写组成" % (str3))
# 判断字符串是否全部小写组成
str4 = "tiger year"
if str4.islower():
    print("字符串'%s'全是小写组成" % (str4))

# 查找子串在字符串中的下标位置
# 找不到返回-1,找到返回子串的位置
str5 = "Happy Tiger Year"
pos = str5.find("Tiger")
print("Tiger的起始位置=%d" % pos)

# 替换子串
str6 = "Happy Tiger Year"
newStr=str6.replace("Tiger","New")
print(newStr)

 # 统计字串出现的次数
str7 =  "happy new year"
print(str7.count("e"))
# 大小写转换
str8 = "TigerYear"
print(str8)
print(str8.upper())
print(str8.lower())
print(str8.swapcase())

str9 ="  Tiger Year  "
print("'%s'" %(str9.lstrip()))
print("'%s'" %(str9.rstrip()))
print("'%s'" %(str9.strip()))
# 根据子串拆分字符串,拆分后的结果,放到一个列表中
str10="I'm_an_engineer"
print(str10.split("_"))
# 输出结果：["I'm", 'an', 'engineer']