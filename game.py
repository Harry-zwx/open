import random

print("""----------------------
游戏菜单
1.猜数字游戏
2.剪刀石头布
----------------------""")
while True:
    option = int(input("请输入你要玩的游戏编号:"))
    if option == 1:
        computer = random.randint(1,100)
        while True:
            number = int(input("请输入100以内的整数:"))
            if number == computer:
                print("恭喜你赢了")
                break
            elif number < computer:
                print("小了")
            else:
                print("大了")
    elif option == 2:
        guess_list = ["石头","剪刀","布"]
        while True:
            computer = random.choice(guess_list)
            people = input("请选择石头，剪刀，布：")
            if people not in guess_list:
                continue
            elif computer == people:
                print("平手")
            elif (computer == "石头" and people == "剪刀") or (computer == "布" and people == "石头") or (computer == "剪刀" and people == "布"):
                print("电脑获胜!")
            else:
                print("人获胜!")
                break

                
    else:       #如果输入数字不是1或2那么重新输入直到合理为止
        break
