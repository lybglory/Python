# encoding=utf-8
# 提示：0-石头，1-剪刀，2-布

# 导入random模块
import random

# 计算电脑出拳的随机数字
computer = random.randint(0, 2)
print(f"computer出{computer}")

player = int(input('请出拳：0-石头，1-剪刀，2-布：'))

# 玩家胜利 p0:c1 或 p1:c2 或 p2:c0
if ((player == 0) and (computer == 1)) \
        or ((player == 1) and (computer == 2)) \
        or ((player == 2) and (computer == 0)):
    print('玩家获胜')
    # 平局：玩家 == 电脑
elif player == computer:
    print('平局')
else:
    print('电脑获胜')
