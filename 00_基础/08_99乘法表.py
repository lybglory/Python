# endcoding=utf-8
line = 1  # 当前行
column = 1  # 当前列
while line <= 9:
    while column <= line:
        # 列 * 行 = 积
        print('{}*{}={}'.format(column, line, (column * line)), end=" ")
        column += 1
    line += 1   # 行数+1
    column = 1  # 列数重置1
    print()     # 换行
