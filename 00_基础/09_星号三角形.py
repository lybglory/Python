'''
*
**
***
****
*****
'''
line =0
column = 0
while line< 5:
    column = 0
    while column <= line:
        print("*" , end ="")
        column+=1
    line +=1
    print()
