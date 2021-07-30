# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 17:40:41 2021

@author: 曲采妮

畫出過檢偏器後之光強度與角度的關係圖。
"""

import numpy as np
import matplotlib.pyplot as plt
#matplotlib補充 
Io = float(input('請問光強度多少?')) #可自己設定原光強度
Ip = 0.5*Io #自然光經過起偏器剩二分之一的原有光強度

theta = np.arange(-2*np.pi,2*np.pi,0.5)
I = Ip * ((np.cos(theta))**2) 

plt.plot(theta,I,color = 'red',linewidth = 2.0, linestyle = '-')
plt.xlim(-10,10)
plt.ylim(0,1)
plt.xlabel("theta")
plt.ylabel("I = 0.5 * Io * (cos(theta))^2")
plt.title("Malus's Law")
plt.show()