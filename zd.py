import os
print('open os 终端 版本:1.0')
while True:
          sx = input('>>>')
          if sx == 'python':
                    os.system('python pypython.py')
          elif sx == 'open os':
                    print('open os 1  2023 window版')
          elif sx == 'q':
                    break
          elif sx == 'help':
                    print('python  使用python解释器')
                    print('open os 查看open os 版本')
                    print('xxgl 学生信息管理系统')
                    print('bfq 播放器')
                    print('game 游戏')
                    print('q 关闭终端')
          elif sx == 'game':
                    os.system('python game.py')
          elif sx == 'xxgl':
                    os.system('python xxg.py')
          elif sx == 'bfq':
                    os.system('python n.py')
          elif sx == 'gema':
                    os.system('python game.py')
          elif 1+1 == 2:
                    print(sx+'不是内部可运行文件也不是外部可运行文件或没有此命令')
