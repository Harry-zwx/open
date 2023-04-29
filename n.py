from tkinter import *
from tkinter import filedialog
from win32com.client import Dispatch
import os
import threading
import n

def bfj():
    win = Tk()
    win.iconbitmap('picture.ico')
    win.title("音乐播放器")
    win.geometry('700x610+400+100')
    win.resizable(False, False)
    wmp = Dispatch("WMPlayer.OCX")

    #添加歌单
    def add_click():
        global folder
        folder = filedialog.askdirectory()
        musics = [folder + '\\' + music for music in os.listdir(folder) if music.endswith(('.mp3'))]
        ret = [] # 存放歌曲文件
        # 歌曲处理
        for i in musics:
            ret.append(i.split('\\')[1:])
            #设置播放文件
            name = wmp.newMedia(i)
            # 建立播放列表
            wmp.currentPlaylist.appendItem(name)
        var2 = StringVar()
        var2.set(ret)
        list0 = Listbox(win, listvariable=var2)
        list0.place(x=1, y=365, width=290, height=240)
        buttonPlay['state'] = 'normal' # 启用按钮
        pause_resume.set('播放')

    def lrc_name():
        global jndu
        # 建立字典存放歌词和时间,key表示时间,value表示歌词
        lrc_dict = {}
        # 获取正在播放的音乐名
        lrcname = folder + '/' + wmp.currentMedia.name + '.lrc'
        lrc_file = open(lrcname, 'r', encoding='utf-8')
        for i in lrc_file.readlines():
            lrc_word = i.replace("[", "]").strip().split("]")
            for j in range(len(lrc_word) - 1):
                if lrc_word[j]:
                    lrc_dict[lrc_word[j]] = lrc_word[-1]
        # 遍历字典,对字典的key进行排序,
        for key in lrc_dict.keys():
            keys = key.split('.')[0]
            if jndu == keys:
                lrc_Name.set(lrc_dict[key])
            else:
                continue
        lrc_file.close()
    # 获取正在播放的MP3
    def music_name():
        global jndu
        while wmp.playState != 1:
            # 正在播放的文件名
            musicName.set("%s" % wmp.currentMedia.name)
            # 播放进度
            progress_scal.set(int(wmp.controls.currentPosition))
            jndu = wmp.controls.currentPositionString
            progress_scal.config(label = jndu)
            progress_scal.config(to = wmp.currentMedia.duration)
            # 歌词
            lrc_name()
            
    # 点击播放
    def play_click():
        buttonNext['state'] = 'normal'
        buttonPrev['state'] = 'normal'

        if pause_resume.get() == '播放':
            wmp.controls.play()
            # 添加线程用以显示当前播放MP3名称
            t = threading.Thread(target=music_name)
            # 解决子线程无法关闭问题
            t.daemon = True
            t.start()
            # 循环播放
            wmp.settings.setMode("loop", True)
            pause_resume.set('暂停')
        elif pause_resume.get() == '暂停':
            wmp.controls.pause()
            pause_resume.set('继续')
        elif pause_resume.get() == '继续':
            wmp.controls.play()
            pause_resume.set('暂停')

    # 下一首
    def next_click():
        wmp.controls.next()
    #上一首
    def prev_click():
        wmp.controls.previous()

    # 音量
    def Volume_ctr(none):
        wmp.settings.Volume = vio_scale.get()
    def Volume_add(i=[0]):
        wmp.settings.Volume =wmp.settings.Volume+5
        i.append(wmp.settings.Volume)
        vio_scale.set(wmp.settings.Volume)
    def Volume_minus(i=[0]):
        wmp.settings.Volume = wmp.settings.Volume -5
        i.append(wmp.settings.Volume)
        vio_scale.set(wmp.settings.Volume)

    # 关闭窗口
    def close_window():
        win.destroy()

    # 歌名+播放进度
    progress_lab = LabelFrame(win,text = "播放进度")
    progress_lab.grid(row =1,column =0,sticky = "we",rowspan = 2)
    musicName = StringVar(progress_lab, value='没有播放音乐...')
    labelName = Label(win, textvariable=musicName, font='12', fg="green")
    labelName.grid(row=0,column=0)
    # 获取播放进度
    var_scale = DoubleVar()
    progress_scal = Scale(progress_lab,orient = HORIZONTAL,showvalue = 0,length =280,variable = var_scale)
    progress_scal.grid(row =2,column =0)
    # 添加歌单
    buttonAdd = Button(win, text='添加歌单', font='20', activeforeground='green', bg='sky blue', command=add_click)
    buttonAdd.place(x=1, y=101, width=140, height=80)
    # 播放
    pause_resume = StringVar(win, value="播放")
    buttonPlay = Button(win, textvariable=pause_resume, font='20', activeforeground='green', bg='sky blue', command=play_click)
    buttonPlay.place(x=150, y=101, width=140, height=80)
    buttonPlay['state'] = 'disabled'
    # 上一首
    buttonPrev = Button(win, text='上一首', font='20', activeforeground='green', bg='sky blue', command=prev_click)
    buttonPrev.place(x=1, y=191, width=140, height=80)
    buttonPrev['state'] = 'disabled'
    # 下一首
    buttonNext = Button(win, text='下一首', font='20', activeforeground='green', bg='sky blue', command=next_click)
    buttonNext.place(x=150, y=191, width=140, height=80)
    buttonNext['state'] = 'disabled'
    # 音量
    var_volume = IntVar()
    vioce_lab = Label(win,text = "")
    vioce_lab.place(x=1,y=275, width=400, height=100)
    vio_scale = Scale(vioce_lab,orient = HORIZONTAL,length =280,variable = var_volume,command =Volume_ctr)
    vio_scale.set(100)
    vio_scale.grid(row =0,column =0)
    vio_plus = Button(vioce_lab,width =8,text = "音量+",command =Volume_add)
    vio_plus.grid(row =9,column =0,sticky = "e")
    vio_minus = Button(vioce_lab,width =8,text ="音量-",command = Volume_minus)
    vio_minus.grid(row =9,column =0,sticky ="w")
    # 歌词
    lrc_lab = LabelFrame(win, text="歌词")
    lrc_lab.place(x=310, y=1, width=380, height=600)
    lrc_Name = StringVar(lrc_lab, value='没有歌词文件')
    lrc_label = Label(lrc_lab, textvariable=lrc_Name, font='10', fg="red")
    lrc_label.pack(fill="both", ipady=20)


    win.mainloop()

