# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:23:41 2016

@author: Guillermo1
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig=plt.figure()
ax=plt.subplot(111)

def Updater(i):
    fil=open('Holi.txt','r')
    texto=fil.readlines()
    x=[]
    y=[]
    for line in texto:
        if line:
            data=line.split()
            x.append(data[0])
            y.append(data[1])
    ax.clear()
    ax.plot(x,y,'r')
    
ani=animation.FuncAnimation(fig,Updater,interval=1000)
plt.show()