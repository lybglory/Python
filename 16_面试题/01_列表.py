ls = ['a', 'b', 'a', 'c', 'd', 'a', 'e', 'a']
print("a的个数=%d" %(ls.count('a')) )

for i in range(len(ls)):
    if ls[i] == 'a':
        print('{0}的下标={1}'.format(ls[i], i))
