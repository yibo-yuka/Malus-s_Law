# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 19:08:33 2021

@author: 曲采妮

做出一個計算介面，判斷兩個偏振片是否垂直，若垂直則光不會透過檢偏器。
"""


import tkinter as tk
from tkinter import Canvas
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageTk

malus = tk.Tk()
malus.geometry('750x700')
malus.resizable(width = True, height = True)
malus.title("Malus's Law") #視窗標題名稱

#初始化區

Io = 1 #假設入射第一片偏振片(起偏器)的光強度為1
Ip = 0.5*Io #自然光經過起偏器剩二分之一的原有光強度

if_can_draw = False

#matplotlib 區
def plot_relation():
    global Io,Ip
    
    Io = float(e3.get()) #可自己設定原光強度
    Ip = 0.5*Io #自然光經過起偏器剩二分之一的原有光強度

    theta = np.arange(-2*np.pi,2*np.pi,0.01)
    I = Ip * (np.cos(theta*(np.pi/180)))**2 #將角度換徑度 : 角度乘以 pi/180 

    plt.plot(theta,I,color = 'red',linewidth = 2.0, linestyle = '-')
    plt.xlim(-10,10)
    plt.ylim(0,1)
    plt.xlabel("theta")
    plt.ylabel("I = 0.5 * Io * (cos(theta))^2")
    plt.title("Malus's Law")
    plt.savefig('C:\\Users\\曲采妮\\Desktop\\python program\\tkinter_optic\\matplotlib 圖片\\test.png')
    plt.show()
    
    open_img = Image.open('test.png')
    rela_pho = ImageTk.PhotoImage(open_img)
    relation_photo = tk.Label(relation_region,image = rela_pho)
    relation_photo.grid(row = 5, column = 0)

calcu = Canvas(malus, width = 500, height = 500, background = '#aaddff') #創造一個背景全黑的畫布
calcu.grid(row = 0,column = 0)
relation_region = Canvas(calcu, width = 300, height = 300, background = '#aaddff') #創造一個背景全黑的畫布
relation_region.grid(row = 0,column = 1)
input_region = Canvas(calcu, width = 300, height = 300, background = '#aaddff') #創造一個背景全黑的畫布
input_region.grid(row = 1,column = 1)
struc = Canvas(calcu, width = 300, height = 300, background = '#000') #創造一個背景全黑的畫布
struc.grid(row = 0,column = 0)
output_region = Canvas(calcu, width = 300, height = 300, background = '#aaddff') #創造一個背景全黑的畫布
output_region.grid(row = 2 ,column = 1)
draw_region = Canvas(calcu, width = 300, height = 300, background = '#ddd') #創造一個背景全黑的畫布
draw_region.grid(row = 1,column = 0)

#標籤區
tk.Label(input_region, text = 'polarizer',bg = '#ffffaa').grid(row = 0,column = 0)
tk.Label(input_region, text = 'analyzer',bg = '#ffffaa').grid(row = 0,column = 1)
tk.Label(output_region, text = "theta = polarizer's theta - analyzer's theta",bg = '#ddffaa').grid(row = 0,column = 1)
tk.Label(output_region, text = "Malus's Law = Io * (cos(theta))^2",bg = '#ddffaa').grid(row = 2,column = 1)
tk.Label(input_region, text = 'original intensity',bg = '#ffffaa').grid(row = 0,column = 2)

Io = 1 #假設入射第一片偏振片(起偏器)的光強度為1
Ip = 0.5*Io #自然光經過起偏器剩二分之一的原有光強度

if_can_draw = False

def enter_polarizer_th_minu_analyzer_th() : #算出角度差，允許畫出結構圖
    global if_can_draw #在此函式中可以改變列舉的變數
    p = float(e1.get()) 
    a = float(e2.get())
    t1.insert('end', p-a)
    if_can_draw = True
    
def enter_iocos() : #算出過檢偏器的光強度
    
    global Io, Ip
    p = float(e1.get()) #輸入到e1的起偏器角度
    a = float(e2.get()) #輸入到e2的檢偏器角度
    I = Ip * (np.cos((p-a)*(np.pi/180)))**2 #將角度換徑度 : 角度乘以 pi/180
    t2.insert('end',round(I,3)) #將四捨五入後的I到t2裡輸出
    
def draw(): #畫出對應結構圖
    global Io, Ip
    
    if if_can_draw == True :
        p = float(e1.get())
        a = float(e2.get())
        I = Ip * (np.cos((p-a)*(np.pi/180)))**2 #將角度換徑度 : 角度乘以 pi/180
        if round(I,3) == 0.0 : #如果兩片偏振片夾角為90度，則光無法通過檢偏器。       
            struc.create_line(25,200,98,200, fill = '#ff4433', width = 10)
            struc.create_line(102,200,198,200, fill = '#ff4433', width = 5)
    
        else :#如果兩片偏振片夾角不為90度，則光可通過檢偏器。
            struc.create_line(25,200,98,200, fill = '#ff4433', width = 10)
            struc.create_line(102,200,198,200, fill = '#ff4433', width = 5)
            struc.create_line(202,200,290,200, fill = '#ff4433', width = 5)
        
def clean(): #清除輸入及輸出
    t1.delete(0.0, 'end')
    t2.delete(0.0, 'end')
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    
def clean_struc(): #清除結構圖
    
    global if_can_draw ,a,p
    struc.create_text(100,100,text = 'polarizer',fill = '#ffffff')
    struc.create_line(100,150,100,250, fill = '#ffff33', width = 4)
    struc.create_text(200,100,text = 'analyzer',fill = '#ffffff')
    struc.create_line(200,150,200,250, fill = '#ffff33', width = 4)
    struc.create_line(25,200,98,200, fill = '#000', width = 10)
    struc.create_line(102,200,198,200, fill = '#000', width = 5)
    struc.create_line(202,200,290,200, fill = '#000', width = 5)
    
    if_can_draw = False #結構圖回到不能畫的狀態
    p = 0 
    a = 0
    #將p、a存的值歸零

#輸入區
e1 = tk.Entry(input_region)
e1.grid(row = 1,column = 0)
e2 = tk.Entry(input_region)
e2.grid(row = 1,column = 1)
e3 = tk.Entry(input_region)
e3.grid(row = 1,column = 2)

#輸出區
t1 = tk.Text(output_region,width = 20,height = 2)
t1.grid(row = 1,column = 1)
t2 = tk.Text(output_region,width = 20,height = 2)
t2.grid(row = 3,column = 1)

#按鈕區
b1 = tk.Button(output_region, text = 'theta', width = 20 ,height = 2, command = enter_polarizer_th_minu_analyzer_th)
b1.grid(row = 1,column = 0)
b2 = tk.Button(output_region, text = 'Io*(cos(theta))^2', width = 20 ,height = 2, command = enter_iocos)
b2.grid(row = 3,column = 0)
b3 = tk.Button(draw_region, text = 'draw', width = 10 ,height = 2, command = draw)
b3.grid(row = 1,column = 0)
b4 = tk.Button(draw_region, text = ' all clean', width = 10 ,height = 2, command = clean)
b4.grid(row = 3,column = 0)
b5 = tk.Button(draw_region, text = 'clean struction', width = 15 ,height = 2, command = clean_struc)
b5.grid(row = 2,column = 0)
#b6 = tk.Button(draw_region, text = 'plot_relation', width = 15 ,height = 2, command = plot_relation)
#b6.grid(row = 4,column = 0)

#結構圖
struc.create_text(100,100,text = 'polarizer',fill = '#ffffff')
polarizer_position = struc.create_line(100,150,100,250, fill = '#ffff33', width = 4)
struc.create_text(200,100,text = 'analyzer',fill = '#ffffff')
analyzer_position = struc.create_line(200,150,200,250, fill = '#ffff33', width = 4)


    
malus.mainloop()