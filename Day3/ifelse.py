"""
Created on 2025-01-05
"""

# Your code starts here
import random


def word(a):
    if a == 0:
        return '石头'
    elif a == 1:
        return '剪刀'
    elif a == 2:
        return '布'


# 石头剪刀布
# 0 石头 1 剪刀 2 布
def game():
    player = int(input("请输入你的选择：石头（0），剪刀（1），布（2）\n"))
    computer = random.randint(0, 2)
    print('playernum=%d computernum=%d' % (player, computer))
    print('玩家的选择是%s,电脑的选择是%s' % (word(player), word(computer)))
    print(f'玩家的选择是{word(player)},电脑的选择是{word(computer)}')
    if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        print("恭喜获胜")
    elif player == computer:
        print("你与电脑达成平局")
    else:
        print("你被电脑打败了")


game()
