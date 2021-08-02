# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 16:01:53 2021

@author: 曲采妮
"""


from numpy import pi ,cos

Io = 1
#Io = float(input('請問入射檢偏器的光強度是？：'))

polarizer_degree = float(input('請輸入起偏器角度:')) #起偏器角度
analyzer_degree = float(input('請輸入檢偏器角度:')) #檢偏器角度
theta = polarizer_degree - analyzer_degree #起偏器與檢偏器的角度差
#print(theta)
rand = theta * (pi/180) #將角度換徑度 : 角度乘以 pi/180
cos_sqrt = (cos(rand))**2 #將cos項平方
I = Io * (cos_sqrt) #代入馬呂思定律的公式


print(I,'*Io',sep ='') #印出 I 為幾倍的 Io,sep用來消除空格
print(I)

