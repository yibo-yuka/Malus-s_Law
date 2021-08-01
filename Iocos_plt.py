# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 17:40:41 2021

@author: 曲采妮

畫出過檢偏器後之光強度與角度的關係圖。
"""

import numpy as np #載入numpy，命名為np
import matplotlib.pyplot as plt #載入matplotlib套件的pyplot函式庫，命名為plt

Io = float(input('請問光強度多少?')) #可自己設定原光強度

theta = np.arange(-2*np.pi,2*np.pi,0.01)
# 取角度在-2pi~2pi之間，每0.01取一個點
I = Io * ((np.cos(theta))**2) 
# 代入馬呂思定律公式
plt.plot(theta,I,color = 'red',linewidth = 2.0, linestyle = '--')
#畫出theta為橫軸，I為垂直軸的關係圖，線要紅色，線寬要2，線的種類是 -- (虛線)

plt.xlim(-6.28,6.28) #圖中橫軸的範圍
plt.ylim(0,1) #圖中垂直軸的範圍
plt.xlabel("theta") #橫軸名字的標籤
plt.ylabel("I = 0.5 * Io * (cos(theta))^2") #垂直軸名字的標籤
plt.title("Malus's Law") #標題名稱
plt.savefig('D:\\matplotlib 圖片\\test.png') #自動存圖到電腦
plt.show() #輸出結果圖 

#補充區
#I2 = Io * ((np.sin(theta))**2)
#plt.plot(theta,I2,color = 'blue',linewidth = 2.0, linestyle = '-')