str = "3 3 3 1 1"
ls = str.split(" ")
sum = 0
for e in ls:
    sum += int(e)
print("sum=%d" % sum)
