# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:44:42 2021

@author: 曲采妮
"""

import tkinter as tk
from tkinter import Canvas
import numpy as np

malus = tk.Tk()

malus.title("Malus's Law")

struc = Canvas(malus, width = 500, height = 500, background = '#000000') #創造一個背景全黑的畫布
struc.grid(row = 0,column = 0)

#test = input ('測試數字 :')
Io = 1 #假設入射第一片偏振片(起偏器)的光強度為1
Ip = 0.5*Io #自然光經過起偏器剩二分之一的原有光強度
polarizer_th = float(input("請輸入起偏器角度?")) #第一片偏振片(起偏器)與垂直軸的角度
analyzer_th = float(input("請輸入檢偏器角度?")) #第二片偏振片(檢偏器)與垂直軸的角度
theta = polarizer_th - analyzer_th #求兩片偏振片角度差
I = Ip * ((np.cos(theta*(np.pi/180)))**2) #將角度換徑度 : 角度乘以 pi/180
print(round(I,3),'*Io',sep = '') #round(要取四捨五入的數字，要取到哪一位)，sep=''會將字串黏在一起
#print(I)

struc.create_text(150,100,text = 'polarizer',fill = '#ffffff')
polarizer_position = struc.create_line(150,150,150,350, fill = '#ffff33', width = 4)
struc.create_text(300,100,text = 'analyzer',fill = '#ffffff')
analyzer_position = struc.create_line(300,150,300,350, fill = '#ffff33', width = 4)
struc.create_text(220,270,text = 'Io',fill = '#ffffff')

struc.create_text(380,270,text = 'I = Io*(cos(theta))^2',fill = '#ffffff')


if round(I,3) == 0 : #如果兩片偏振片夾角為90度，則光無法通過檢偏器。       
    Io_light = struc.create_line(25,250,148,250, fill = '#ff4433', width = 10)
    Ip_light = struc.create_line(152,250,298,250, fill = '#ff4433', width = 5)
    
else :#如果兩片偏振片夾角不為90度，則光可通過檢偏器。
    Io_light = struc.create_line(25,250,148,250, fill = '#ff4433', width = 10)
    Ip_light = struc.create_line(152,250,298,250, fill = '#ff4433', width = 5)
    I_light = struc.create_line(302,250,470,250, fill = '#ff4433', width = 5)
    
malus.mainloop()