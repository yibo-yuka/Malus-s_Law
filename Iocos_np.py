# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 20:28:24 2021

@author: 曲采妮

代入馬呂思定律公式求過檢偏器後剩下光強度為原來的幾倍。
"""


#import tkinter as tk
import numpy as np
#import matplotlib.pyplot as plt


Io = 1 #假設入射第一片偏振片的光強度為1
Ip = 0.5*Io #自然光經過起偏器剩二分之一的原有光強度
polarizer_th = float(input("請輸入起偏器角度?")) #第一片偏振片(起偏器)與垂直軸的角度
analyzer_th = float(input("請輸入檢偏器角度?")) #第二片偏振片(檢偏器)與垂直軸的角度
theta = polarizer_th - analyzer_th #求兩片偏振片角度差

rand = theta*(np.pi/180) #將角度換徑度 : 角度乘以 pi/180
cos_sqrt = np.cos(rand) #將cos平方
I = Ip * ((cos_sqrt)**2) #代入malus's Law
#print(I)
I = round(I,3) #round(要取四捨五入的數字，要取到哪一位)
print(I,'*Io',sep='') # sep='' 會將字串黏在一起



#I = Ip * ((np.cos(theta*(np.pi/180)))**2) #將角度換徑度 : 角度乘以 pi/180
#print(round(I,3),'*Io',sep='') #round(要取四捨五入的數字，要取到哪一位)，sep=''會將字串黏在一起
#print(I)




#matplotlib補充 
#theta = np.arange(-2*np.pi,2*np.pi,0.01)
#plt.plot(theta,I,color = 'red',linewidth = 2.0, linestyle = '-')
#plt.xlim(-5,5)
#plt.ylim(-1,1)
#plt.xlabel("theta")
#plt.ylabel("I = IO * (cos(theta))^2")
#plt.title("Malus's Law")
#plt.show()

#tkinter補充
#


