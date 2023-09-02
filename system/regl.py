import tkinter as t
import psutil
import os
import datetime
import time




root = t.Tk()
root.iconbitmap('picture.ico')
la = t.Label(root,text='o\np\ne\nn\n \no\ns',font=('楷体',20),fg='blue').place(x=750,y=50)
root.geometry('800x600+500+200')
root.title('open os 任务管理器')
m=t.Menu(root)
root.configure(menu=m)
def yy():
          text.delete(1.0,'end')
          l1=t.Label(root,text='开机时间：')
          tm=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
          l2=t.Label(root,text=str(tm))
          l3=t.Label(root,text='当前时间：')
          l4=t.Label(root,text='')
          dq=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
          l4.configure(text=str(dq))
          l5=t.Label(root,text='物理内存使用情况(MB)：')
          l6=t.Label(root,text='')
          jh=psutil.virtual_memory() #物理内存
          tt=int((jh.total)/1024/1024) #总量
          us=int((jh.used)/1024/1024) #使用量
          fr=int((jh.free)/1024/1024) #剩余量
          l6.configure(text='总量：' + str(tt) +'\n'+'使用：'+str(us) +'\n'+'剩余：'+str(fr))
          l7=t.Label(root,text='交换内存使用情况(MB)：')
          l8=t.Label(root,text='')
          hj=psutil.swap_memory() #交换内存
          ht=int((hj.total)/1024/1024)
          hu=int((hj.used)/1024/1024)
          hf=int((hj.free)/1024/1024)
          l8.configure(text='总量：' + str(ht) + '  '+'使用：'+str(hu) +'  '+'剩余：'+str(hf))
          text.window_create('insert',window=l1) #添加组件到多行文本框
          text.window_create('insert',window=l2)
          text.insert('insert','\n\n')
          text.window_create('insert',window=l3)
          text.window_create('insert',window=l4)
          text.insert('insert','\n\n')
          text.window_create('insert',window=l5)
          text.window_create('insert',window=l6)
          text.insert('insert','\n\n')
          text.window_create('insert',window=l7)
          text.window_create('insert',window=l8)
          n = psutil.net_io_counters()
          r=str(float(n.bytes_recv / 1024 / 1024))+'MB'
          s= str(float(n.bytes_sent / 1024 / 1024))+'MB'
          text.insert('insert','\n网卡接收流量: '+str(r)+'\n'+'网卡发送流量：'+str(s)+'\n')
def jc():
          text.delete(1.0,'end')
          text.insert('insert','进程号   '+'进程名      '+'  进程文件路径'+'\n')
          for y in psutil.pids():
                    a=psutil.Process(y)
                    if a.name()=='System Idle Process':
                              continue
                    else:
                              text.insert('insert',str(y)+'     '+a.name()+'   '+a.exe()+'\n\n')
def fw():
          text.delete(1.0,'end')
          mm=os.popen('sc query type= service')
          text.insert('insert',mm.read())
def lw():
          text.delete(1.0,'end')
          n = psutil.net_io_counters()
          r=str(float(n.bytes_recv / 1024 / 1024))+'MB'
          s= str(float(n.bytes_sent / 1024 / 1024))+'MB'
          text.insert('insert','网卡接收流量: '+str(r)+'\n'+'网卡发送流量：'+str(s)+'\n')  
def yh():
          text.delete(1.0,'end')
          use='    用户'+'      '+'     状态'+'\n'
          text.insert('insert',use)
          for y in psutil.users():
                    text.insert('2.0',str(y.name)+'  '+'运行中。。。。'+'\n')
b1=t.Button(root,text='  汇总/刷新',command=yy)
b2=t.Button(root,text='进程',command=jc)
b3=t.Button(root,text='服务',command=fw)
b5=t.Button(root,text='网络',command=lw)
b6=t.Button(root,text='用户',command=yh)
b1.place(x=10,y=15,height=20,width=60)
b2.place(x=70,y=15,height=20,width=60)
b3.place(x=130,y=15,height=20,width=60)
b5.place(x=190,y=15,height=20,width=60)
b6.place(x=250,y=15,height=20,width=60)
text=t.Text(root,width=100,height=40)
text.place(x=10,y=36)
sb=t.Scrollbar(root)
sb.pack(side='left',fill='y')
text=t.Text(root,width=100,height=40)
text.place(x=10,y=36)
sb.config(command=text.yview) #文本框内容随滚动条滚动
text.config(yscrollcommand=sb.set(0.1,0.3)) #Y轴填充
yy()
root.mainloop()
