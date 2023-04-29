import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import *
import tkinter.messagebox
import idlelib.colorizer as idc
import idlelib.percolator as idp



root = tk.Tk()
root.iconbitmap('picture.ico')
root.title('pyexea')
root.geometry('900x700')
frame = tk.Frame(root)
button = tk.Button(frame, text='Exit IDEA',bg='#252424',fg='white')
button1 = tk.Button(frame, text='New file',bg='#252424',fg='white')
button2 = tk.Button(frame, text='Open file',bg='#252424',fg='white')
button3 = tk.Button(frame, text='Save file',bg='#252424',fg='white')
button4 = tk.Button(frame, text='run',bg='#252424',fg='#41cc32')
button5 = tk.Button(frame, text='Clean python 3.10',bg='#252424',fg='white')
button.pack(side=tk.LEFT)
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.LEFT)
button4.pack(side=tk.LEFT)
button5.pack(side=tk.RIGHT)
frame.pack(side=tk.TOP, fill=tk.BOTH)
global textPad
textPad = ScrolledText(fg='white')
textPad.pack(fill=tk.BOTH, expand=1)
textPad.focus_set()
global filename
filename = '未命名.py'


def btnfunc01():
          global textPad, filename
          textPad.delete(1.0, tk.END)
          filename = '未命名.py'
def btnfunc02():
          global textPad, filename
          filename2 = askopenfilename(defaultextension='')
          if filename2 != '':
                    textPad.delete(1.0, tk.END)
                    f = open(filename2, 'r', encoding='utf-8', errors='ignore')
                    textPad.insert(1.0, f.read())
                    f.close()
                    filename = filename2
def btnfunc03():
          global textPad, filename
          filename = asksaveasfilename(initialfile=filename, defaultextension='')
          if filename != '':
                    fh = open(filename, 'w', encoding='utf-8', errors='ignore')
                    msg = textPad.get(1.0, tk.END)
                    fh.write(msg)
                    fh.close()
button['command'] = lambda: root.destroy()
button1['command'] = lambda: btnfunc01()
button2['command'] = lambda: btnfunc02()
button3['command'] = lambda: btnfunc03()
frame2 = tk.LabelFrame(root, text='pyexea 1.0.1', height=100)
frame2.pack(fill=tk.BOTH, expand=1)
global textMess
textMess = ScrolledText(frame2, bg='#252424', height=10,fg='white')
textMess.pack(fill=tk.BOTH, expand=1)
def clearMess():
          global textMess
          textMess.delete(1.0, tk.END)
          printf('人生短苦，我用python！','blue')
          printf('\n朱浩宇python编辑器 1.0.1 Windows（64位）保留所有权利\n说明：\n1.python中的任何输入方式未实现！可保存后用python LDLE执行！\n2.本编辑器仅能看到运行结果不能操作\n3.程序过于复杂会出现未响应\n','black')
def input():
          printf('\ninput函数未实现！可保存后用python LDLE执行！','blue')
def print(txt,color='blue'):
    global textMess
    if textMess != None :
        textMess.tag_config(color, foreground=color)
        zv = '\n' + txt
        textMess.insert(tk.END, zv,color)
        textMess.see(tk.END)
def printf(txt, color='black'):
          global textMess
          if textMess != None:
                    if color != 'black':
                              textMess.tag_config(color, foreground=color)
          textMess.insert(tk.END, txt, color)
          textMess.see(tk.END)
printf('人生短苦，我用python！','blue')
printf('\n朱浩宇python编辑器 1.0.1 Windows（64位）保留所有权利\n说明：\n1.python中的任何输入方式未实现！可保存后用python LDLE执行！\n2.本编辑器仅能看到运行结果不能操作\n3.程序过于复杂会出现未响应\n','black')
def goto():
    global textPad,textMess
    printf('\n========================执行中......=======================','black')
    try:
        msg = textPad.get(1.0,tk.END)
        mg=globals()
        ml=locals()
        exec(msg,mg,ml)
        printf('\n========================执行结束=======================','black')
    except Exception as e:
        printf('\n'+'报错:'+str(e),'red')
        printf('\n========================执行结束=======================','black')
def gb():
    root.after(1,root.destroy)
def copy():
    textPad.event_generate("<<Copy>>")
def paste():
    textPad.event_generate("<<Paste>>")
def cut():
    textPad.event_generate("<<Cut>>")
def select_all():
    textPad.tag_add("sel", "1.0", "end")
def popup(event):
    editmenu.post(event.x_root, event.y_root) 
m = Menu(root)
editmenu = Menu(m)
editmenu.add_command(label = '复制',command=copy)
editmenu.add_command(label = '剪切',command=cut)
editmenu.add_command(label = '粘贴',command=paste)
editmenu.add_separator()
editmenu.add_command(label = 'run',command=goto)
editmenu.add_command(label = '关闭pyexea编辑器',command=gb)
m.add_cascade(label = '', menu = editmenu)
root.bind('<Button-3>',popup)
     
def key(event):
          goto()
button4['command'] = lambda: goto()
button5['command'] = lambda: clearMess()

root.bind('<F11>',key)
idc.color_config(textPad)
textPad.focus_set()
textPad.config(bg='white',fg='black')
p = idp.Percolator(textPad)
d = idc.ColorDelegator()
p.insertfilter(d)
root.mainloop()
