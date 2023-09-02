import tkinter as tk
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pygame
import sys
import turtle
import random
from functools import partial
import datetime as d
import winsound
import datetime

from pygame.locals import QUIT,KEYDOWN
import urllib
from  urllib import request,parse
import json,hashlib
import tkinter.filedialog
from functools import partial
import webbrowser
import tkinter.simpledialog
import tkinter.colorchooser
import tkinter.filedialog
from PIL import ImageGrab,Image,ImageTk
import datetime
import threading
import tkinter.messagebox
import http.client
import hashlib
import json
import urllib.parse
import math, random,time
import threading
import re
from turtle import *
from math import cos, pi
from time import perf_counter as clock, sleep
from turtle import Screen, Turtle, mainloop
from time import perf_counter as clock, sleep
from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *
from PIL import Image,ImageTk
import tkinter.scrolledtext
import tkinter.simpledialog
from tkinter import *
import time
import tkinter as tk
import os
import platform
import tkinter as t
import psutil
import os
import datetime
import time
from tkinter import *
import pywifi,time,tkinter.filedialog,tkinter.messagebox
from pywifi import const
import calendar as d
import subprocess



def afg():
          filename_initStr = ''



          def wjss():
              

              def browseFiles():
                  filename = filedialog.askopenfilename(initialdir = "/",
                                                        title = "选择文件")
                                                        


                  label_file_explorer.configure(text="文件路径: "+filename)
              windowz = Tk()
              windowz.iconbitmap('picture.ico')
              windowz.title('文件路径搜索')
              windowz.geometry("700x120")
              windowz.config(background = "white")
              label_file_explorer = Label(windowz,
                                          text = "未选择！",
                                          width = 100, height = 4,
                                          fg = "blue")

              button_explore = Button(windowz,
                                      text = "选择文件",
                                      command = browseFiles)
              label_file_explorer.grid(column = 1, row = 1)

              button_explore.grid(column = 1, row = 2)
              windowz.mainloop()

          def ysb():
              win_width = 900
              win_height = 450


              class Application(Frame):

                  def __init__(self, master=None, bgcolor="#000000"):
                      super().__init__(master)
                      self.master = master
                      self.bgcolor = bgcolor
                      self.x = 0
                      self.y = 0
                      self.fgcolor = "#ff0000"
                      self.lastDraw = 0       
                      self.startDrawFlag = False
                      self.pack()
                      self.createWidget()

                  def createWidget(self):
                      self.drawpad = Canvas(root, width=win_width, height=win_height*0.9, bg=self.bgcolor)
                      self.drawpad.pack()
                      btn_pen = Button(root, text="画笔", name="pen")
                      btn_pen.pack(side="left", padx="10")
                      btn_rect = Button(root, text="矩形", name="rect")
                      btn_rect.pack(side="left", padx="10")
                      btn_clear = Button(root, text="清屏", name="clear")
                      btn_clear.pack(side="left", padx="10")
                      btn_eraser = Button(root, text="橡皮擦", name="eraser")
                      btn_eraser.pack(side="left", padx="10")
                      btn_line = Button(root, text="直线", name="line")
                      btn_line.pack(side="left", padx="10")
                      btn_lineArrow = Button(root, text="箭头直线", name="lineArrow")
                      btn_lineArrow.pack(side="left", padx="10")
                      btn_color = Button(root, text="颜色", name="color")
                      btn_color.pack(side="left", padx="10")
                      btn_pen.bind_class("Button", "<1>", self.eventManager)
                      self.drawpad.bind("<ButtonRelease-1>", self.stopDraw)
                      root.bind("<KeyPress-r>", self.kuaijiejian)
                      root.bind("<KeyPress-g>", self.kuaijiejian)
                      root.bind("<KeyPress-y>", self.kuaijiejian)
                  def eventManager(self, event):
                      name = event.widget.winfo_name()
                      if name == "line":
                          self.drawpad.bind("<B1-Motion>", self.myline)
                      elif name == "lineArrow":
                          self.drawpad.bind("<B1-Motion>", self.mylineArrow)
                      elif name == "rect":
                          self.drawpad.bind("<B1-Motion>", self.myRect)
                      elif name == "pen":
                          self.drawpad.bind("<B1-Motion>", self.myPen)
                      elif name == "eraser":
                          self.drawpad.bind("<B1-Motion>", self.myErasear)
                      elif name == "clear":
                          self.drawpad.delete("all")
                      elif name == "color":
                          c = askcolor(color=self.fgcolor, title="选择画笔颜色")
                          self.fgcolor = c[1]
                  def stopDraw(self, event):
                      self.startDrawFlag = False
                      self.lastDraw = 0

                  def startDraw(self,event):
                      self.drawpad.delete(self.lastDraw)

                      if not self.startDrawFlag:
                          self.startDrawFlag = True
                          self.x = event.x
                          self.y = event.y


                  def myline(self, event):
                      self.startDraw(event)
                      self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)

                  def mylineArrow(self, event):
                      self.startDraw(event)
                      self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=self.fgcolor)

                  def myRect(self, event):
                      self.startDraw(event)
                      self.lastDraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)

                  def myPen(self, event):
                      self.startDraw(event)
                      self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
                      self.x = event.x
                      self.y = event.y

                  def myErasear(self, event):
                      self.startDraw(event)
                      self.drawpad.create_line(self.x-50, self.y-50, event.x+50, event.y+50, fill=self.bgcolor)
                      self.x = event.x
                      self.y = event.y

                  def kuaijiejian(self, event):
                      if event.char == "r":
                          self.fgcolor = "#ff0000"
                      elif event.char == "g":
                          self.fgcolor = "#00ff00"
                      elif event.char == "y":
                          self.fgcolor = "#ffff00"


              if __name__ == '__main__':
                  root = Tk()
                  root.iconbitmap('picture.ico')
                  root.geometry(str(win_width)+"x"+str(win_height)+"+300+300")
                  root.title("演示板")
                  app = Application(master=root)
                  root.mainloop()

          def sd():
              class ColorTurtle(Turtle):

                  def __init__(self, x, y):
                      Turtle.__init__(self)
                      self.shape("turtle")
                      self.resizemode("user")
                      self.shapesize(3,3,5)
                      self.pensize(10)
                      self._color = [0,0,0]
                      self.x = x
                      self._color[x] = y
                      self.color(self._color)
                      self.speed(0)
                      self.left(90)
                      self.pu()
                      self.goto(x,0)
                      self.pd()
                      self.sety(1)
                      self.pu()
                      self.sety(y)
                      self.pencolor("gray25")
                      self.ondrag(self.shift)

                  def shift(self, x, y):
                      self.sety(max(0,min(y,1)))
                      self._color[self.x] = self.ycor()
                      self.fillcolor(self._color)
                      setbgcolor()

              def setbgcolor():
                  screen.bgcolor(red.ycor(), green.ycor(), blue.ycor())

              def main():
                  global screen, red, green, blue
                  screen = Screen()
                  screen.delay(0)
                  screen.setworldcoordinates(-1, -0.3, 3, 1.3)

                  red = ColorTurtle(0, .5)
                  green = ColorTurtle(1, .5)
                  blue = ColorTurtle(2, .5)
                  setbgcolor()

                  writer = Turtle()
                  writer.ht()
                  writer.pu()
                  writer.goto(1,1.15)
                  writer.write("DRAG!",align="center",font=("Arial",30,("bold","italic")))
                  return "EVENTLOOP"

              if __name__ == "__main__":
                  msg = main()
                  print(msg)
                  mainloop()

          def yh():
              Fireworks=[]
              maxFireworks=8
              height,width=600,600
              class firework(object):
                  def __init__(self,color,speed,width,height):
                      self.radius=random.randint(2,4)  
                      self.color=color  
                      self.speed=speed 
                      self.status=0 
                      self.nParticle=random.randint(20,30)  
                      self.center=[random.randint(0,width-1),random.randint(0,height-1)]  
                      self.oneParticle=[]  
                      self.rotTheta=random.uniform(0,2*math.pi)
                      self.ellipsePara=[random.randint(30,40),random.randint(20,30)]   
                      theta=2*math.pi/self.nParticle
                      for i in range(self.nParticle):
                          t=random.uniform(-1.0/16,1.0/16)
                          x,y=self.ellipsePara[0]*math.cos(theta*i+t), self.ellipsePara[1]*math.sin(theta*i+t) 
                          xx,yy=x*math.cos(self.rotTheta)-y*math.sin(self.rotTheta),  y*math.cos(self.rotTheta)+x*math.sin(self.rotTheta)    
                          self.oneParticle.append([xx,yy])
                      self.curParticle=self.oneParticle[0:]   
                      self.thread=threading.Thread(target=self.extend)          
                  def extend(self):       
                      for i in range(100):
                          self.status+=1  
                          self.curParticle=[[one[0]*self.status/100, one[1]*self.status/100] for one in self.oneParticle]  
                          time.sleep(self.speed/50)
                  
                  def explode(self):
                      self.thread.start()   
                          

                  def __repr__(self):
                      return ('color:{color}\n'  
                              'speed:{speed}\n'
                              'number of particle: {np}\n'
                              'center:[{cx} , {cy}]\n'
                              'ellipse:a={ea} , b={eb}\n'
                              'particle:\n{p}\n'
                              ).format(color=self.color,speed=self.speed,np=self.nParticle,cx=self.center[0],cy=self.center[1],p=str(self.oneParticle),ea=self.ellipsePara[0],eb=self.ellipsePara[1])


              def colorChange(fire):
                  rgb=re.findall(r'(.{2})',fire.color[1:])
                  cs=fire.status
                  
                  f=lambda x,c: hex(int(int(x,16)*(100-c)/30))[2:] 
                  if cs>70:
                      ccr,ccg,ccb=f(rgb[0],cs),f(rgb[1],cs),f(rgb[2],cs)
                  else:
                      ccr,ccg,ccb=rgb[0],rgb[1],rgb[2]
                      
                  return '#{0:0>2}{1:0>2}{2:0>2}'.format(ccr,ccg,ccb)



              def appendFirework(n=1): 
                  if n>maxFireworks or len(Fireworks)>maxFireworks:
                      pass
                  elif n==1:
                      cl='#{0:0>6}'.format(hex(int(random.randint(0,16777215)))[2:])  
                      a=firework(cl,random.uniform(1.5,3.5),width,height)
                      Fireworks.append( {'particle':a,'points':[]} )  
                      a.explode()
                  else:
                      appendFirework()
                      appendFirework(n-1)


              def show(c):
                  for p in Fireworks:               
                      for pp in p['points']:
                          c.delete(pp)
                  
                  for p in Fireworks:             
                      oneP=p['particle']
                      if oneP.status==100:        
                          Fireworks.remove(p)     
                          appendFirework()         
                          continue
                      else:
                          li=[[int(cp[0]*2)+oneP.center[0],int(cp[1]*2)+oneP.center[1]] for cp in oneP.curParticle]    
                          color=colorChange(oneP)  
                          for pp in li:
                              p['points'].append(c.create_oval(pp[0]-oneP.radius,  pp[1]-oneP.radius,  pp[0]+oneP.radius,  pp[1]+oneP.radius,  fill=color))  
                  root.after(50, show,c)
              if __name__=='__main__':
                  appendFirework(maxFireworks)
                  root = tk.Tk()
                  root.title('烟花')
                  cv = tk.Canvas(root, height=height, width=width)
                  cv.create_rectangle(0, 0, width, height, fill="black")
                  cv.pack()
                  root.after(50, show,cv)
                  root.mainloop()

          def ds():
              turtle.bgcolor('black')
              turtle.hideturtle()
              turtle.speed(0)
              turtle.delay(0)
               
              turtle.penup()
              turtle.goto(320,180)
              turtle.pendown()
              turtle.pencolor("white")
              turtle.write("游戏说明：\n控制键：\n↑ 打上面地鼠\n↓ 打下面地鼠\n← 打左面地鼠\n→ 打右面地鼠\n",align="right",font=("楷体", 14,"normal"))
              turtle.pencolor("black")
               
              def chuizi():
                  turtle.hideturtle()
                  turtle.begin_fill()
                  turtle.fillcolor("#804000")
                  turtle.left(135)
                  turtle.forward(50)
                  turtle.left(90)
                  turtle.forward(30)
                  turtle.right(90)
                  turtle.forward(30)
                  turtle.right(90)
                  turtle.forward(65)
                  turtle.right(90)
                  turtle.forward(30)
                  turtle.right(90)
                  turtle.forward(30)
                  turtle.left(90)
                  turtle.forward(50)
                  turtle.right(90)
                  turtle.forward(5)
                  turtle.end_fill()
                  turtle.penup()
                  turtle.home()
               
              def laoshu():
                  turtle.begin_fill()
                  turtle.fillcolor("#D3D3D3")
                  turtle.forward(50)
                  turtle.left(90)
                  turtle.forward(60)
                  turtle.circle(25, 180)
                  turtle.forward(60)
                  turtle.right(180)
                  turtle.forward(60)
                  turtle.right(90)
                  turtle.end_fill()
                  turtle.penup()
                  turtle.forward(15)
                  turtle.pendown()
                  turtle.begin_fill()
                  turtle.fillcolor("black")
                  turtle.circle(3)
                  turtle.end_fill()
                  turtle.penup()
                  turtle.forward(18)
                  turtle.pendown()
                  turtle.begin_fill()
                  turtle.fillcolor("black")
                  turtle.circle(3)
                  turtle.end_fill()
                  turtle.penup()
                  turtle.right(180)
                  turtle.forward(6)
                  turtle.left(90)
                  turtle.forward(5)
                  turtle.pendown()
                  turtle.right(90)
                  turtle.forward(6)
                  turtle.right(180)
                  turtle.forward(3)
                  turtle.right(90)
                  turtle.forward(5)
                  turtle.circle(3, 180)
                  turtle.penup()
                  turtle.left(90)
                  turtle.forward(12)
                  turtle.left(90)
                  turtle.pendown()
                  turtle.circle(3, 180)
                  turtle.penup()
                  turtle.home()
               
              def shang():
                  turtle.penup()
                  turtle.goto(100,200)
                  chuizi()
                  time.sleep(0.5)
                  turtle.pendown()
                  turtle.pencolor('black')
                  turtle.color('black')
                  turtle.begin_fill()
                  turtle.circle(150)
                  turtle.end_fill()
                  turtle.penup()
                  turtle.home()
               
              def xia():
                  turtle.penup()
                  turtle.goto(100,-200)
                  turtle.pendown()
                  chuizi()
                  time.sleep(0.5)
                  turtle.penup()
                  turtle.goto(50, -300)
                  turtle.pendown()
                  turtle.pencolor('black')
                  turtle.color('black')
                  turtle.begin_fill()
                  turtle.circle(150)
                  turtle.end_fill()
                  turtle.penup()
                  turtle.home()
               
              def zuo():
                  turtle.penup()
                  turtle.goto(-100,0)
                  turtle.pendown()
                  chuizi()
                  time.sleep(0.5)
                  turtle.penup()
                  turtle.goto(-100,-50)
                  turtle.pendown()
                  turtle.pencolor('black')
                  turtle.color('black')
                  turtle.begin_fill()
                  turtle.circle(130)
                  turtle.end_fill()
                  turtle.penup()
                  turtle.home()
               
              def you():
                  turtle.penup()
                  turtle.goto(300,0)
                  turtle.pendown()
                  chuizi()
                  time.sleep(0.5)
                  turtle.penup()
                  turtle.goto(250,-100)
                  turtle.pendown()
                  turtle.pencolor('black')
                  turtle.color('black')
                  turtle.begin_fill()
                  turtle.circle(150)
                  turtle.end_fill()
                  turtle.penup()
                  turtle.home()
               
               
              turtle.listen()
              turtle.onkey(lambda :shang(),'Up')
              turtle.onkey(lambda :xia(),'Down')
              turtle.onkey(lambda :zuo(),'Left')
              turtle.onkey(lambda :you(),'Right')
               
              def huayuan():
                  colors = random.choice(["pink", "yellow", "white", "red", "green"])
                  x=random.choice([0,-200,200])
                  if x==0:
                      y=random.choice([-200,200])
                  else:
                      y=0
                  turtle.penup()
                  turtle.goto(x,y)
                  turtle.pendown()
                  laoshu()
               
              for i in range(10):
                  huayuan()
                  time.sleep(2)
                  turtle.penup()
                  turtle.home()
              turtle.done()

          def mz():
              root = tk.Tk()
              root.title('名字设计')
              inp1 = tk.Entry(root)
              inp1.place(relx=0.009, rely=0.1, relwidth=0.5, relheight=0.1)
              tk.Label(root,text='名字:').place(x=0.2,y=0.09)
              def rot():
                  root1 = inp1.get()
                  top = tk.Tk()
                  top.title('设计名字')
                  tk.Label(top,text=root1,font=("华文行楷",60)).pack()
                  tk.mainloop()
              tk.Button(root,text='华文行楷',command=rot).place(x=0.01,y=40)
              root.mainloop()
              
          def yy():
              engine=pyttsx3.init()
              def say():
                  engine.setProperty('voice','zh')
                  text=edit.get('0.0','end')
                  engine.setProperty('rate',scale.get())
                  engine.say(text,'fox')
                  engine.runAndWait()
              def save_file():
                  file=f'{int(time.time())}.mp3'
                  engine.save_to_file(edit.get('0.0','end'),file)
                  engine.runAndWait()
                  tkinter.messagebox.showinfo('文件保存成功：',file)
              def thread_it(func,*args):
                  t=threading.Thread(target=func,args=args)
                  t.setDaemon(True)
                  t.start()
              window=tk.Tk()
              window.iconbitmap('picture.ico')
              window.geometry('400x500')
              window.title("文字转语音助手")
              window.resizable(width=False,height=False)
              edit=tk.Text(window,height=15,width=40,highlightcolor='blue',bd=1,highlightthickness=1)
              edit.pack(pady=25)
              scale=tk.Scale(window,bg='gray',fg='red',length=300,label='语速控制：',from_=0,to=300,resolution=1,orient=tk.HORIZONTAL)
              scale.set(163)
              scale.pack(pady=4)
              button=tk.Button(window,fg='blue',font=('仿宋',15),bg='orange',bd=5,width=35,text='试 听',command=lambda:thread_it(say))
              button.pack(pady=15)
              button1=tk.Button(window,fg='blue',font=('仿宋',15),bg='orange',bd=5,width=35,text='保 存',
              command=lambda:thread_it(save_file))
              button1.pack(pady=3)
              window.mainloop()

          def jsq():
              def get_input(entry, argu):
                  input_data = entry.get()
                  if (input_data[-1:] == '+') and (argu == '+'):
                      return
                  if (input_data[-2:] == '+-') and (argu == '-'):
                      return
                  if (input_data[-2:] == '--') and (argu in ['-', '+']):
                      return
                  if (input_data[-2:] == '**') and (argu in ['*', '/']):
                      return
                  entry.insert("end", argu)
              def backspace(entry):
                  input_len = len(entry.get())
                  entry.delete(input_len - 1)
              def clear(entry):
                  entry.delete(0, "end")
              def calc(entry):
                  input_data = entry.get()
                  if not input_data:
                      return
                  clear(entry)
                  try:
                      output_data = str(eval(input_data))
                  except Exception:
                      entry.insert("end", "Calculation error")
                  else:
                      if len(output_data) > 20:
                          entry.insert("end", "Value overflow")
                      else:
                          entry.insert("end", output_data)


              if __name__ == '__main__':

                  root = tkinter.Tk()
                  root.title("计算器")
                  root.iconbitmap('picture.ico')
                  root.resizable(0, 0)
                  button_bg = 'gray'
                  math_sign_bg = 'DarkTurquoise'
                  cal_output_bg = 'Yellow'
                  button_active_bg = 'gray'
                  entry = tkinter.Entry(root, justify="right", font=1)
                  entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

                  def place_button(text, func, func_params, bg=button_bg, **place_params):
                      my_button = partial(tkinter.Button, root, bg=button_bg, padx=10, pady=3, activebackground=button_active_bg)
                      button = my_button(text=text, bg=bg, command=lambda: func(*func_params))
                      button.grid(**place_params)
                  place_button('7', get_input, (entry, '7'), row=1, column=0, ipadx=5, pady=5)
                  place_button('8', get_input, (entry, '8'), row=1, column=1, ipadx=5, pady=5)
                  place_button('9', get_input, (entry, '9'), row=1, column=2, ipadx=5, pady=5)
                  place_button('4', get_input, (entry, '4'), row=2, column=0, ipadx=5, pady=5)
                  place_button('5', get_input, (entry, '5'), row=2, column=1, ipadx=5, pady=5)
                  place_button('6', get_input, (entry, '6'), row=2, column=2, ipadx=5, pady=5)
                  place_button('1', get_input, (entry, '1'), row=3, column=0, ipadx=5, pady=5)
                  place_button('2', get_input, (entry, '2'), row=3, column=1, ipadx=5, pady=5)
                  place_button('3', get_input, (entry, '3'), row=3, column=2, ipadx=5, pady=5)
                  place_button('0', get_input, (entry, '0'), row=4, column=0, padx=8, pady=5,
                               columnspan=2, sticky=tkinter.E + tkinter.W + tkinter.N + tkinter.S)
                  place_button('.', get_input, (entry, '.'), row=4, column=2, ipadx=7, padx=5, pady=5)
                  place_button('+', get_input, (entry, '+'), bg=math_sign_bg, row=1, column=3, ipadx=5, pady=5)
                  place_button('-', get_input, (entry, '-'), bg=math_sign_bg, row=2, column=3, ipadx=5, pady=5)
                  place_button('*', get_input, (entry, '*'), bg=math_sign_bg, row=3, column=3, ipadx=5, pady=5)
                  place_button('/', get_input, (entry, '/'), bg=math_sign_bg, row=4, column=3, ipadx=5, pady=5)
                  place_button('<-', backspace, (entry,), row=5, column=0, ipadx=5, padx=5, pady=5)
                  place_button('C', clear, (entry,), row=5, column=1, pady=5, ipadx=5)
                  place_button('=', calc, (entry,), bg=cal_output_bg, row=5, column=2, ipadx=5, padx=5, pady=5,
                               columnspan=2, sticky=tkinter.E + tkinter.W + tkinter.N + tkinter.S)

                  root.mainloop()
                  

          def new_file():
              global top, filename_initStr, text_more_lines
              top.title("未命名文件   -Mountain Stream Office - 2023")

              filename_initStr = None
              text_more_lines.delete(1.0, tk.END)

          def open_file():
              global filename_initStr
              filename_initStr = filedialog.askopenfilename(defaultextension="")

              if filename_initStr == "":
                  filename_initStr = None
              else:
                  top.title("" + os.path.basename(filename_initStr)+"   -Mountain Stream Office - 2023")
                  text_more_lines.delete(1.0, tk.END)
                  file = open(filename_initStr, 'r', encoding="utf-8")
                  text_more_lines.insert(1.0, file.read())
                  file.close()

          def save():
              try:
                  open_File = open(filename_initStr, 'w', encoding="utf-8")
                  msg = text_more_lines.get(1.0, 'end')
                  open_File.write(msg)
                  open_File.close()
              except:
                  save_additionally()

          def save_additionally():
              try:
                  NewFile = filedialog.asksaveasfilename(initialfile="", defaultextension="")
                  create_new_file = open(NewFile, 'w', encoding="utf-8")
                  msg = text_more_lines.get(1.0, tk.END)
                  create_new_file.write(msg)
                  create_new_file.close()
                  top.title("" + os.path.basename(NewFile))
              except:
                  pass
          def mz():
              root = tk.Tk()
              root.title('名字设计')
              tk.Label(root,text='名字:').pack()
              inp1 = tk.Entry(root)
              inp1.pack()
              def rot():
                  root1 = inp1.get()
                  top = tk.Tk()
                  top.title('设计名字')
                  tk.Label(top,text=root1,font=("华文行楷",60)).pack()
                  tk.mainloop()
              def rot1():
                  root1 = inp1.get()
                  top = tk.Tk()
                  top.title('设计名字')
                  tk.Label(top,text=root1,font=("中华仿宋",60)).pack()
                  tk.mainloop()
              def rot2():
                  root1 = inp1.get()
                  top = tk.Tk()
                  top.title('设计名字')
                  tk.Label(top,text=root1,font=("华文楷体",60)).pack()
                  tk.mainloop()
              tk.Button(root,text='华文行楷',command=rot).pack()
              tk.Button(root,text='中华仿宋',command=rot1).pack()
              tk.Button(root,text='华文楷体',command=rot).pack()
              root.mainloop()

          def gb():
              top.after(1,top.destroy)
          def copy():
              text_more_lines.event_generate("<<Copy>>")

          def paste():
              text_more_lines.event_generate("<<Paste>>")

          def cut():
              text_more_lines.event_generate("<<Cut>>")

          def select_all():
              text_more_lines.tag_add("sel", "1.0", "end")

          def program_createTime(): 
              dbg1 = tk.Tk()
              dbg1.iconbitmap('picture.ico')
              dbg1.title('程序创建时间 Program creation time')
              dbg = tk.Text(dbg1)
              dbg.pack()
              dbg.insert(tk.END,'2023 2 21 20:43 若发现漏洞请拨打：17092611786 我们将进行修改')
              def gb2():
                              dbg1.after(0,dbg1.destroy)
              tk.Button(dbg1,text='关闭',command=gb2).pack()
              dbg1.mainloop()
          def Author():
              dbg1 = tk.Tk()
              dbg1.iconbitmap('picture.ico')
              dbg1.title('版权信息 Copyright Information')
              dbg = tk.Text(dbg1)
              dbg.pack()
              dbg.insert(tk.END,'作者：\n朱浩宇\n保留所有权利，允许用于商业或转载，\n若功能一致纯属巧合，允许进行开发。')
              def gb2():
                              dbg1.after(0,dbg1.destroy)
              tk.Button(dbg1,text='关闭',command=gb2).pack()
              dbg1.mainloop()
          if a == a:
              top = tk.Tk()
              top.title("open os 文本笔记本 - 2023 2.0.1")
              top.geometry("350x500+450+130")
              top.iconbitmap('picture.ico')
              top_menu_Bar = tk.Menu(top)
              file_of_menu = tk.Menu(top)
              file_of_menu.add_command(label="新建", accelerator="Ctrl+n", command=new_file)
              file_of_menu.add_command(label="打开", accelerator="Ctrl+o", command=open_file)
              file_of_menu.add_command(label="保存", accelerator="Ctrl+s", command=save)
              file_of_menu.add_command(label="另存为", accelerator="Ctrl+shift+s", command=save_additionally)
              file_of_menu.add_separator()
              file_of_menu.add_command (label="关闭 open os 文本笔记本",command=gb)
              top_menu_Bar.add_cascade(label="文件", menu=file_of_menu)
              edit_of_menu = tk.Menu(top)
              edit_of_menu.add_command(label="复制", accelerator="Ctrl+c", command=copy)
              edit_of_menu.add_command(label="粘贴", accelerator="Ctrl+v", command=paste)
              edit_of_menu.add_command(label="剪切", accelerator="Ctrl+x", command=cut)
              edit_of_menu.add_separator()
              edit_of_menu.add_command(label="全选", accelerator="Ctrl+a", command=select_all)
              top_menu_Bar.add_cascade(label="编辑", menu=edit_of_menu)
              file_of_menu = tk.Menu(top)
              file_of_menu.add_command(label="网站", command=wz)
              file_of_menu.add_command(label="文字转语音助手", command=yy)
              file_of_menu.add_command(label="演示板", command=ysb)
              file_of_menu.add_command(label="计算器", command=jsq)
              file_of_menu.add_command(label="文件路径搜索", command=wjss)
              top_menu_Bar.add_cascade(label="工具", menu=file_of_menu)
              file_of_menu = tk.Menu(top)
              file_of_menu.add_command(label="烟花", command=yh)
              file_of_menu.add_command(label="打地鼠", command=ds)
              file_of_menu.add_command(label="色调", command=sd)
              
              file_of_menu.add_command(label="名字设计", command=mz)
              top_menu_Bar.add_cascade(label="娱乐", menu=file_of_menu)
              about_of_menu = tk.Menu(top)
              about_of_menu.add_command(label="关于", command=program_createTime)
              about_of_menu.add_command(label="版权", command=Author)
              top_menu_Bar.add_cascade(label="关于", menu=about_of_menu)
              popupmenu = tk.Menu(top,tearoff=0)
              popupmenu.add_command (label="复制",command=copy)
              popupmenu.add_command (label="粘贴",command=paste)
              popupmenu.add_command (label="剪切",command=cut)
              popupmenu.add_command (label="全选",command=select_all)
              popupmenu.add_separator()
              popupmenu.add_command (label="关闭 open os 文本笔记本",command=gb)
              popupmenu.add_separator()
              popupmenu.add_command (label="文字转语音助手",command=yy)
              popupmenu.add_command (label="计算器",command=jsq)
              popupmenu.add_command (label="名字设计",command=mz)
              def showPopUpMenu(event) :
                  popupmenu .post (event.x_root, event.y_root)
              top.bind("<Button-3>", showPopUpMenu)
              top['menu'] = top_menu_Bar
              text_more_lines = tk.Text(top, padx=5, pady=5)
              text_more_lines.pack(expand=True, fill=tk.BOTH)
              scroll = tk.Scrollbar(master=text_more_lines)
              text_more_lines.config(yscrollcommand=scroll.set)
              scroll.config(command=text_more_lines.yview)
              scroll.pack(side=tk.RIGHT, fill=tk.Y)
              text_more_lines.bind("<Control-N>", new_file)
              text_more_lines.bind("<Control-n>", new_file)
              text_more_lines.bind("<Control-O>", open_file)
              text_more_lines.bind("<Control-o>", open_file)
              text_more_lines.bind("<Control-S>", save)
              text_more_lines.bind("<Control-s>", save)
              text_more_lines.bind("<Control-Shift-s>", save_additionally)
              text_more_lines.bind("<Control-Shift-S>", save_additionally)
              text_more_lines.bind("<Control-c>", copy)
              text_more_lines.bind("<Control-C>", copy)
              text_more_lines.bind("<Control-v>", paste)
              text_more_lines.bind("<Control-V>", paste)
              text_more_lines.bind("<Control-x>", cut)
              text_more_lines.bind("<Control-X>", cut)
              text_more_lines.bind("<Control-A>", select_all)
              text_more_lines.bind("<Control-a>", select_all)
              top.mainloop()

win = tk.Tk()
win.title('open os')
a1 = tk.Button(win,text='文件',command=afg)
a1.place(x=10,y=10)
def n():
          subprocess.Popen('n.exe')
a2 = tk.Button(win,text='播放器',command=n)
a2.place(x=10,y=50)
def gettime():
                    var.set(time.strftime("%Y\%m\%d\%A\n%p   %H:%M:%S"))
                    win.after(1000,gettime) 
var=tk.StringVar()
lb = tk.Label(win,textvariable=var,fg='black',font=("楷体",15))
lb.place(x=1000,y=650)
gettime()

def ks():
          def jsq():
              def get_input(entry, argu):
                  input_data = entry.get()
                  if (input_data[-1:] == '+') and (argu == '+'):
                      return
                  if (input_data[-2:] == '+-') and (argu == '-'):
                      return
                  if (input_data[-2:] == '--') and (argu in ['-', '+']):
                      return
                  if (input_data[-2:] == '**') and (argu in ['*', '/']):
                      return
                  entry.insert("end", argu)
              def backspace(entry):
                  input_len = len(entry.get())
                  entry.delete(input_len - 1)
              def clear(entry):
                  entry.delete(0, "end")
              def calc(entry):
                  input_data = entry.get()
                  if not input_data:
                      return
                  clear(entry)
                  try:
                      output_data = str(eval(input_data))
                  except Exception:
                      entry.insert("end", "Calculation error")
                  else:
                      if len(output_data) > 20:
                          entry.insert("end", "Value overflow")
                      else:
                          entry.insert("end", output_data)


              if __name__ == '__main__':

                  root = tkinter.Tk()
                  root.title("计算器")
                  root.iconbitmap('picture.ico')
                  root.resizable(0, 0)
                  button_bg = 'gray'
                  math_sign_bg = 'DarkTurquoise'
                  cal_output_bg = 'Yellow'
                  button_active_bg = 'gray'
                  entry = tkinter.Entry(root, justify="right", font=1)
                  entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

                  def place_button(text, func, func_params, bg=button_bg, **place_params):
                      my_button = partial(tkinter.Button, root, bg=button_bg, padx=10, pady=3, activebackground=button_active_bg)
                      button = my_button(text=text, bg=bg, command=lambda: func(*func_params))
                      button.grid(**place_params)
                  place_button('7', get_input, (entry, '7'), row=1, column=0, ipadx=5, pady=5)
                  place_button('8', get_input, (entry, '8'), row=1, column=1, ipadx=5, pady=5)
                  place_button('9', get_input, (entry, '9'), row=1, column=2, ipadx=5, pady=5)
                  place_button('4', get_input, (entry, '4'), row=2, column=0, ipadx=5, pady=5)
                  place_button('5', get_input, (entry, '5'), row=2, column=1, ipadx=5, pady=5)
                  place_button('6', get_input, (entry, '6'), row=2, column=2, ipadx=5, pady=5)
                  place_button('1', get_input, (entry, '1'), row=3, column=0, ipadx=5, pady=5)
                  place_button('2', get_input, (entry, '2'), row=3, column=1, ipadx=5, pady=5)
                  place_button('3', get_input, (entry, '3'), row=3, column=2, ipadx=5, pady=5)
                  place_button('0', get_input, (entry, '0'), row=4, column=0, padx=8, pady=5,
                               columnspan=2, sticky=tkinter.E + tkinter.W + tkinter.N + tkinter.S)
                  place_button('.', get_input, (entry, '.'), row=4, column=2, ipadx=7, padx=5, pady=5)
                  place_button('+', get_input, (entry, '+'), bg=math_sign_bg, row=1, column=3, ipadx=5, pady=5)
                  place_button('-', get_input, (entry, '-'), bg=math_sign_bg, row=2, column=3, ipadx=5, pady=5)
                  place_button('*', get_input, (entry, '*'), bg=math_sign_bg, row=3, column=3, ipadx=5, pady=5)
                  place_button('/', get_input, (entry, '/'), bg=math_sign_bg, row=4, column=3, ipadx=5, pady=5)
                  place_button('<-', backspace, (entry,), row=5, column=0, ipadx=5, padx=5, pady=5)
                  place_button('C', clear, (entry,), row=5, column=1, pady=5, ipadx=5)
                  place_button('=', calc, (entry,), bg=cal_output_bg, row=5, column=2, ipadx=5, padx=5, pady=5,
                               columnspan=2, sticky=tkinter.E + tkinter.W + tkinter.N + tkinter.S)

                  root.mainloop()
          def ysb():
              win_width = 900
              win_height = 450


              class Application(Frame):

                  def __init__(self, master=None, bgcolor="#000000"):
                      super().__init__(master)
                      self.master = master
                      self.bgcolor = bgcolor
                      self.x = 0
                      self.y = 0
                      self.fgcolor = "#ff0000"
                      self.lastDraw = 0       
                      self.startDrawFlag = False
                      self.pack()
                      self.createWidget()

                  def createWidget(self):
                      self.drawpad = Canvas(root, width=win_width, height=win_height*0.9, bg=self.bgcolor)
                      self.drawpad.pack()
                      btn_pen = Button(root, text="画笔", name="pen")
                      btn_pen.pack(side="left", padx="10")
                      btn_rect = Button(root, text="矩形", name="rect")
                      btn_rect.pack(side="left", padx="10")
                      btn_clear = Button(root, text="清屏", name="clear")
                      btn_clear.pack(side="left", padx="10")
                      btn_eraser = Button(root, text="橡皮擦", name="eraser")
                      btn_eraser.pack(side="left", padx="10")
                      btn_line = Button(root, text="直线", name="line")
                      btn_line.pack(side="left", padx="10")
                      btn_lineArrow = Button(root, text="箭头直线", name="lineArrow")
                      btn_lineArrow.pack(side="left", padx="10")
                      btn_color = Button(root, text="颜色", name="color")
                      btn_color.pack(side="left", padx="10")
                      btn_pen.bind_class("Button", "<1>", self.eventManager)
                      self.drawpad.bind("<ButtonRelease-1>", self.stopDraw)
                      root.bind("<KeyPress-r>", self.kuaijiejian)
                      root.bind("<KeyPress-g>", self.kuaijiejian)
                      root.bind("<KeyPress-y>", self.kuaijiejian)
                  def eventManager(self, event):
                      name = event.widget.winfo_name()
                      if name == "line":
                          self.drawpad.bind("<B1-Motion>", self.myline)
                      elif name == "lineArrow":
                          self.drawpad.bind("<B1-Motion>", self.mylineArrow)
                      elif name == "rect":
                          self.drawpad.bind("<B1-Motion>", self.myRect)
                      elif name == "pen":
                          self.drawpad.bind("<B1-Motion>", self.myPen)
                      elif name == "eraser":
                          self.drawpad.bind("<B1-Motion>", self.myErasear)
                      elif name == "clear":
                          self.drawpad.delete("all")
                      elif name == "color":
                          c = askcolor(color=self.fgcolor, title="选择画笔颜色")
                          self.fgcolor = c[1]
                  def stopDraw(self, event):
                      self.startDrawFlag = False
                      self.lastDraw = 0

                  def startDraw(self,event):
                      self.drawpad.delete(self.lastDraw)

                      if not self.startDrawFlag:
                          self.startDrawFlag = True
                          self.x = event.x
                          self.y = event.y


                  def myline(self, event):
                      self.startDraw(event)
                      self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)

                  def mylineArrow(self, event):
                      self.startDraw(event)
                      self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=self.fgcolor)

                  def myRect(self, event):
                      self.startDraw(event)
                      self.lastDraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)

                  def myPen(self, event):
                      self.startDraw(event)
                      self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
                      self.x = event.x
                      self.y = event.y

                  def myErasear(self, event):
                      self.startDraw(event)
                      self.drawpad.create_line(self.x-50, self.y-50, event.x+50, event.y+50, fill=self.bgcolor)
                      self.x = event.x
                      self.y = event.y

                  def kuaijiejian(self, event):
                      if event.char == "r":
                          self.fgcolor = "#ff0000"
                      elif event.char == "g":
                          self.fgcolor = "#00ff00"
                      elif event.char == "y":
                          self.fgcolor = "#ffff00"


              if __name__ == '__main__':
                  root = Tk()
                  root.iconbitmap('picture.ico')
                  root.geometry(str(win_width)+"x"+str(win_height)+"+300+300")
                  root.title("open os演示板")
                  app = Application(master=root)
                  root.mainloop()
          def gj():
                    os.system('shutdown -s -t 00')
          def cq():
                    os.system('shutdown -s -r 00')
          def wz():
                    webbrowser.open('https://www.baidu.com')
          def yy():
              engine=pyttsx3.init()
              def say():
                  engine.setProperty('voice','zh')
                  text=edit.get('0.0','end')
                  engine.setProperty('rate',scale.get())
                  engine.say(text,'fox')
                  engine.runAndWait()
              def save_file():
                  file=f'{int(time.time())}.mp3'
                  engine.save_to_file(edit.get('0.0','end'),file)
                  engine.runAndWait()
                  tkinter.messagebox.showinfo('文件保存成功：',file)
              def thread_it(func,*args):
                  t=threading.Thread(target=func,args=args)
                  t.setDaemon(True)
                  t.start()
              window=tk.Tk()
              window.iconbitmap('picture.ico')
              window.geometry('400x500')
              window.title("文字转语音助手")
              window.resizable(width=False,height=False)
              edit=tk.Text(window,height=15,width=40,highlightcolor='blue',bd=1,highlightthickness=1)
              edit.pack(pady=25)
              scale=tk.Scale(window,bg='gray',fg='red',length=300,label='语速控制：',from_=0,to=300,resolution=1,orient=tk.HORIZONTAL)
              scale.set(163)
              scale.pack(pady=4)
              button=tk.Button(window,fg='blue',font=('仿宋',15),bg='orange',bd=5,width=35,text='试 听',command=lambda:thread_it(say))
              button.pack(pady=15)
              button1=tk.Button(window,fg='blue',font=('仿宋',15),bg='orange',bd=5,width=35,text='保 存',
              command=lambda:thread_it(save_file))
              button1.pack(pady=3)
              window.mainloop()
          def pythm1():
                    os.system('python pypython.py')
          def pyexe():
                    os.system('python pyexe.py')
          def sz():
                    root = tk.Tk()
                    root.iconbitmap('picture.ico')
                    root.title('open os 设置')
                    root.geometry('700x390')
                    la = tk.Label(root,text='o\np\ne\nn\n \no\ns',font=('楷体',20),fg='blue').place(x=670,y=50)
                    global xxt
                    xxt = tk.Text(root)
                    xxt.place(x=100,y=0)
                    def printf(txt, color='black'):
                              global xxt
                              if xxt != None:
                                        if color != 'black':
                                                  xxt.tag_config(color, foreground=color)
                              xxt.insert(tk.END, txt, color)
                              xxt.see(tk.END)
                    def xx():
                              xxt.delete(1.0, tk.END)
                              printf('open os 信息','blue')
                              xxt.insert(tk.END,'\n版本:open os 1.01\n系统类型:子系统\n底层代码编写语言:python\n编写人员:朱浩宇(harry.vai or harry.hei)\n维护人员:朱浩宇(harry.vai or harry.hei)\n可运行系统:windows\n开发时间:2023.4.30')
                              xxt.see(tk.END)
                    def xz():
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

                              b1=t.Button(root,text=' 汇总/刷新',command=yy)
                              b2=t.Button(root,text='进程',command=jc)
                              b3=t.Button(root,text='服务',command=fw)
                              b5=t.Button(root,text='联网',command=lw)
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

                    def sj():
                              xxt.delete(1.0, tk.END)
                              ad = int(time.strftime("%Y"))
                              ax = int(time.strftime("%m"))
                              ac = time.strftime("%Y.%m.%d")
                              printf(d.month(ad,ax),'blue')
                              ac = '\n\n' + '现在时间:' + ac
                              printf(ac,'blue')
                    bot = tk.Button(root,text='open os 信息',command=xx)
                    bot.place(x=10,y=10)
                    bot1 = tk.Button(root,text='系统现状',command=xz)
                    bot1.place(x=10,y=40)
                    bot2 = tk.Button(root,text='时间',command=sj)
                    bot2.place(x=10,y=70)
                    root.mainloop()
          def xz():
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

                    b1=t.Button(root,text=' 汇总/刷新',command=yy)
                    b2=t.Button(root,text='进程',command=jc)
                    b3=t.Button(root,text='服务',command=fw)
                    b5=t.Button(root,text='联网',command=lw)
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
          def rl():
                    subprocess.Popen('rl.exe')
          win1 = tk.Tk()
          win1.iconbitmap('picture.ico')
          win1.geometry('200x470')
          win1.title('开始')
          win1.lift()
          az = tk.Button(win1,text='关机',command=gj)
          az.place(x=10,y=0)
          az1 = tk.Button(win1,text='重启',command=cq)
          az1.place(x=10,y=30)
          def n():
                    subprocess.Popen('n.exe')
          az2 = tk.Button(win1,text='open os播放器',command=n)
          az2.place(x=10,y=60)
          az3 = tk.Button(win1,text='open os文本笔记本',command=afg)
          az3.place(x=10,y=90)
          az4 = tk.Button(win1,text='open os计算器',command=jsq)
          az4.place(x=10,y=120)
          az5 = tk.Button(win1,text='open os演示板',command=ysb)
          az5.place(x=10,y=150)
          az7 = tk.Button(win1,text='open os文字转语音助手',command=yy)
          az7.place(x=10,y=180)
          az6 = tk.Button(win1,text='网站',command=wz)
          az6.place(x=10,y=240)
          az8 = tk.Button(win1,text='文件路径搜索',command=wjss)
          az8.place(x=10,y=210)
          tk.Label(win1,text='编程工具').place(x=10,y=270)
          az9 = tk.Button(win1,text='pypython',command=pythm1)
          az9.place(x=10,y=300)
          az10 = tk.Label(win1,text='系统')
          az10.place(x=10,y=330)
          az11 = tk.Button(win1,text='设置',command=sz)
          az11.place(x=10,y=360)
          az12 = tk.Button(win1,text='任务管理器',command=xz)
          az12.place(x=10,y=390)
          az13 = tk.Button(win1,text='日历',command=rl)
          az13.place(x=10,y=420)
          la = tk.Label(win1,text='o\np\ne\nn\n \no\ns',font=('楷体',20),fg='blue').place(x=170,y=30)
          win1.mainloop()
def jsq():
              def get_input(entry, argu):
                  input_data = entry.get()
                  if (input_data[-1:] == '+') and (argu == '+'):
                      return
                  if (input_data[-2:] == '+-') and (argu == '-'):
                      return
                  if (input_data[-2:] == '--') and (argu in ['-', '+']):
                      return
                  if (input_data[-2:] == '**') and (argu in ['*', '/']):
                      return
                  entry.insert("end", argu)
              def backspace(entry):
                  input_len = len(entry.get())
                  entry.delete(input_len - 1)
              def clear(entry):
                  entry.delete(0, "end")
              def calc(entry):
                  input_data = entry.get()
                  if not input_data:
                      return
                  clear(entry)
                  try:
                      output_data = str(eval(input_data))
                  except Exception:
                      entry.insert("end", "Calculation error")
                  else:
                      if len(output_data) > 20:
                          entry.insert("end", "Value overflow")
                      else:
                          entry.insert("end", output_data)


              if __name__ == '__main__':

                  root = tkinter.Tk()
                  root.title("计算器")
                  root.iconbitmap('picture.ico')
                  root.resizable(0, 0)
                  button_bg = 'gray'
                  math_sign_bg = 'DarkTurquoise'
                  cal_output_bg = 'Yellow'
                  button_active_bg = 'gray'
                  entry = tkinter.Entry(root, justify="right", font=1)
                  entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

                  def place_button(text, func, func_params, bg=button_bg, **place_params):
                      my_button = partial(tkinter.Button, root, bg=button_bg, padx=10, pady=3, activebackground=button_active_bg)
                      button = my_button(text=text, bg=bg, command=lambda: func(*func_params))
                      button.grid(**place_params)
                  place_button('7', get_input, (entry, '7'), row=1, column=0, ipadx=5, pady=5)
                  place_button('8', get_input, (entry, '8'), row=1, column=1, ipadx=5, pady=5)
                  place_button('9', get_input, (entry, '9'), row=1, column=2, ipadx=5, pady=5)
                  place_button('4', get_input, (entry, '4'), row=2, column=0, ipadx=5, pady=5)
                  place_button('5', get_input, (entry, '5'), row=2, column=1, ipadx=5, pady=5)
                  place_button('6', get_input, (entry, '6'), row=2, column=2, ipadx=5, pady=5)
                  place_button('1', get_input, (entry, '1'), row=3, column=0, ipadx=5, pady=5)
                  place_button('2', get_input, (entry, '2'), row=3, column=1, ipadx=5, pady=5)
                  place_button('3', get_input, (entry, '3'), row=3, column=2, ipadx=5, pady=5)
                  place_button('0', get_input, (entry, '0'), row=4, column=0, padx=8, pady=5,
                               columnspan=2, sticky=tkinter.E + tkinter.W + tkinter.N + tkinter.S)
                  place_button('.', get_input, (entry, '.'), row=4, column=2, ipadx=7, padx=5, pady=5)
                  place_button('+', get_input, (entry, '+'), bg=math_sign_bg, row=1, column=3, ipadx=5, pady=5)
                  place_button('-', get_input, (entry, '-'), bg=math_sign_bg, row=2, column=3, ipadx=5, pady=5)
                  place_button('*', get_input, (entry, '*'), bg=math_sign_bg, row=3, column=3, ipadx=5, pady=5)
                  place_button('/', get_input, (entry, '/'), bg=math_sign_bg, row=4, column=3, ipadx=5, pady=5)
                  place_button('<-', backspace, (entry,), row=5, column=0, ipadx=5, padx=5, pady=5)
                  place_button('C', clear, (entry,), row=5, column=1, pady=5, ipadx=5)
                  place_button('=', calc, (entry,), bg=cal_output_bg, row=5, column=2, ipadx=5, padx=5, pady=5,
                               columnspan=2, sticky=tkinter.E + tkinter.W + tkinter.N + tkinter.S)

                  root.mainloop()
def wz():
          webbrowser.open('https://www.baidu.com')
def ysb():
              win_width = 900
              win_height = 450


              class Application(Frame):

                  def __init__(self, master=None, bgcolor="#000000"):
                      super().__init__(master)
                      self.master = master
                      self.bgcolor = bgcolor
                      self.x = 0
                      self.y = 0
                      self.fgcolor = "#ff0000"
                      self.lastDraw = 0       
                      self.startDrawFlag = False
                      self.pack()
                      self.createWidget()

                  def createWidget(self):
                      self.drawpad = Canvas(root, width=win_width, height=win_height*0.9, bg=self.bgcolor)
                      self.drawpad.pack()
                      btn_pen = Button(root, text="画笔", name="pen")
                      btn_pen.pack(side="left", padx="10")
                      btn_rect = Button(root, text="矩形", name="rect")
                      btn_rect.pack(side="left", padx="10")
                      btn_clear = Button(root, text="清屏", name="clear")
                      btn_clear.pack(side="left", padx="10")
                      btn_eraser = Button(root, text="橡皮擦", name="eraser")
                      btn_eraser.pack(side="left", padx="10")
                      btn_line = Button(root, text="直线", name="line")
                      btn_line.pack(side="left", padx="10")
                      btn_lineArrow = Button(root, text="箭头直线", name="lineArrow")
                      btn_lineArrow.pack(side="left", padx="10")
                      btn_color = Button(root, text="颜色", name="color")
                      btn_color.pack(side="left", padx="10")
                      btn_pen.bind_class("Button", "<1>", self.eventManager)
                      self.drawpad.bind("<ButtonRelease-1>", self.stopDraw)
                      root.bind("<KeyPress-r>", self.kuaijiejian)
                      root.bind("<KeyPress-g>", self.kuaijiejian)
                      root.bind("<KeyPress-y>", self.kuaijiejian)
                  def eventManager(self, event):
                      name = event.widget.winfo_name()
                      if name == "line":
                          self.drawpad.bind("<B1-Motion>", self.myline)
                      elif name == "lineArrow":
                          self.drawpad.bind("<B1-Motion>", self.mylineArrow)
                      elif name == "rect":
                          self.drawpad.bind("<B1-Motion>", self.myRect)
                      elif name == "pen":
                          self.drawpad.bind("<B1-Motion>", self.myPen)
                      elif name == "eraser":
                          self.drawpad.bind("<B1-Motion>", self.myErasear)
                      elif name == "clear":
                          self.drawpad.delete("all")
                      elif name == "color":
                          c = askcolor(color=self.fgcolor, title="选择画笔颜色")
                          self.fgcolor = c[1]
                  def stopDraw(self, event):
                      self.startDrawFlag = False
                      self.lastDraw = 0

                  def startDraw(self,event):
                      self.drawpad.delete(self.lastDraw)

                      if not self.startDrawFlag:
                          self.startDrawFlag = True
                          self.x = event.x
                          self.y = event.y


                  def myline(self, event):
                      self.startDraw(event)
                      self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)

                  def mylineArrow(self, event):
                      self.startDraw(event)
                      self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=self.fgcolor)

                  def myRect(self, event):
                      self.startDraw(event)
                      self.lastDraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)

                  def myPen(self, event):
                      self.startDraw(event)
                      self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
                      self.x = event.x
                      self.y = event.y

                  def myErasear(self, event):
                      self.startDraw(event)
                      self.drawpad.create_line(self.x-50, self.y-50, event.x+50, event.y+50, fill=self.bgcolor)
                      self.x = event.x
                      self.y = event.y

                  def kuaijiejian(self, event):
                      if event.char == "r":
                          self.fgcolor = "#ff0000"
                      elif event.char == "g":
                          self.fgcolor = "#00ff00"
                      elif event.char == "y":
                          self.fgcolor = "#ffff00"


              if __name__ == '__main__':
                  root = Tk()
                  root.iconbitmap('picture.ico')
                  root.geometry(str(win_width)+"x"+str(win_height)+"+300+300")
                  root.title("open os演示板")
                  app = Application(master=root)
                  root.mainloop()
def wjss():
              

              def browseFiles():
                  filename = filedialog.askopenfilename(initialdir = "/",
                                                        title = "选择文件")
                                                        


                  label_file_explorer.configure(text="文件路径: "+filename)
              windowz = Tk()
              windowz.iconbitmap('picture.ico')
              windowz.title('文件路径搜索')
              windowz.geometry("700x120")
              windowz.config(background = "white")
              label_file_explorer = Label(windowz,
                                          text = "未选择！",
                                          width = 100, height = 4,
                                          fg = "blue")

              button_explore = Button(windowz,
                                      text = "选择文件",
                                      command = browseFiles)
              label_file_explorer.grid(column = 1, row = 1)

              button_explore.grid(column = 1, row = 2)
              windowz.mainloop()
def pythm():
          subprocess.Popen('pypython.exe')
def zd():
          subprocess.Popen('zd.exe')
def xxs():
          os.system('python xxg.py')
def pyexe():
          os.system('python pyexe.pyw')
def sz():
          root = tk.Tk()
          root.iconbitmap('picture.ico')
          root.title('open os 设置')
          root.geometry('700x390')
          la = tk.Label(root,text='o\np\ne\nn\n \no\ns',font=('楷体',20),fg='blue').place(x=670,y=50)
          global xxt
          xxt = tk.Text(root)
          xxt.place(x=100,y=0)
          def printf(txt, color='black'):
                    global xxt
                    if xxt != None:
                              if color != 'black':
                                        xxt.tag_config(color, foreground=color)
                    xxt.insert(tk.END, txt, color)
                    xxt.see(tk.END)
          def xx():
                    xxt.delete(1.0, tk.END)
                    printf('open os 信息','blue')
                    xxt.insert(tk.END,'\n版本:open os 1.01\n系统类型:子系统\n底层代码编写语言:python\n编写人员:朱浩宇(harry.vai or harry.hei)\n维护人员:朱浩宇(harry.vai or harry.hei)\n可运行系统:windows\n开发时间:2023.4.30')
                    xxt.see(tk.END)
          def xz():
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

                    b1=t.Button(root,text=' 汇总/刷新',command=yy)
                    b2=t.Button(root,text='进程',command=jc)
                    b3=t.Button(root,text='服务',command=fw)
                    b5=t.Button(root,text='联网',command=lw)
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

          def sj():
                    xxt.delete(1.0, tk.END)
                    ad = int(time.strftime("%Y"))
                    ax = int(time.strftime("%m"))
                    ac = time.strftime("%Y.%m.%d")
                    printf(d.month(ad,ax),'blue')
                    ac = '\n\n' + '现在时间:' + ac
                    printf(ac,'blue')
          def rl():
                    subprocess.Popen('rl.exe')
          bot = tk.Button(root,text='open os 信息',command=xx)
          bot.place(x=10,y=10)
          bot1 = tk.Button(root,text='系统现状',command=xz)
          bot1.place(x=10,y=40)
          bot2 = tk.Button(root,text='时间',command=sj)
          bot2.place(x=10,y=70)
          bot3 = tk.Button(root,text='日历',command=rl)
          bot3.place(x=10,y=100)
          root.mainloop()
def xz():
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

          b1=t.Button(root,text=' 汇总/刷新',command=yy)
          b2=t.Button(root,text='进程',command=jc)
          b3=t.Button(root,text='服务',command=fw)
          b5=t.Button(root,text='联网',command=lw)
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
import subprocess
def rl():
          subprocess.Popen('rl.exe')
def zd():
          subprocess.Popen('zd.exe')
a = tk.Button(win,text='开始',command=ks)
a.place(x=500,y=670)
azx = tk.Button(win,text='计算器',command=jsq)
azx.place(x=10,y=90)
a5 = tk.Button(win,text='访问',command=wz)
a5.place(x=10,y=130)
a6 = tk.Button(win,text='演示板',command=ysb)
a6.place(x=10,y=170)
a7 = tk.Button(win,text='文件路径搜索',command=wjss)
a7.place(x=10,y=210)
a8 = tk.Button(win,text='pypython',command=pythm)
a8.place(x=10,y=250)
a9 = tk.Button(win,text='终端',command=zd)
a9.place(x=540,y=670)
a8 = tk.Button(win,text='pypython',command=pythm)
a8.place(x=580,y=670)
a10 = tk.Button(win,text='学生信息管理系统',command=xxs)
a10.place(x=10,y=290)
a11 = tk.Button(win,text='学生信息管理系统',command=xxs)
a11.place(x=650,y=670)
a12 = tk.Label(win,text='______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________')
a12.place(x=0,y=540)
a13 = tk.Label(win,text='______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________')
a13.place(x=0,y=590)
a14 = tk.Label(win,text='系统')
a14.place(x=0,y=530)
a15 = tk.Button(win,text='pyexe',command=pyexe)
a15.place(x=10,y=330)
a16 = tk.Button(win,text='设置',command=sz)
a16.place(x=5,y=570)
a17 = tk.Button(win,text='任务管理器',command=xz)
a17.place(x=50,y=570)
a18 = tk.Button(win,text='日历',command=rl)
a18.place(x=130,y=570)
def sd():
          subprocess.Popen('sd.exe')
a19 = tk.Button(win,text='连网',command=sd)
a19.place(x=170,y=570)
la = tk.Label(win,text='o\np\ne\nn\n \no\ns\n\n9\n0\n0',font=('楷体',30),fg='blue').place(x=1170,y=50)
win.iconbitmap('picture.ico')
win.resizable(False,True)
win.geometry('1200x700')
win.mainloop()
