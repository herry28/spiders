#导入随机模块
import random

#定义一个变量，用来记录用户的输入
# player=int(input("请输入：剪刀（0） 石头（1） 布（2）："))
# #定义一个变量，记录电脑的输入
# computer=random.randint(0,2)
#
# #以玩家为第一视角
# #假如玩家胜利（剪刀=布、石头=剪刀、布=石头）
# #假如玩家和电脑平局（玩家=电脑）
# #假如玩家失败（除了胜利和平局，全是败局）
#
# print("玩家：%d"%player)
# print("电脑：%d"%computer)
# if (player==0 and computer==2) or (player==1 and computer==0) or(player==2 and computer==1):
#     print("玩家胜利")
# elif(player==computer):
#     print("玩家与电脑平局")
# else:
#     print("玩家失败")


#死循环
print("马上开始游戏~~~~~~~~~~~~")
while True:
    player = int(input("请输入：剪刀（0） 石头（1） 布（2）："))
    computer = random.randint(0, 2)
    print("玩家：%d" % player)
    print("电脑：%d" % computer)
    if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print("玩家胜利")
    elif (player == computer):
        print("玩家与电脑平局")
    else:
        print("玩家失败")
    print("==========================")