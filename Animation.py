# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 13:39:18 2016

@author: Guillermo1
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as matan

def f(t):
    return t**2

t=np.linspace(0,10,100)
fig=plt.figure()
ax=plt.subplot(111)
ax.set_xlim(0,10)
ax.set_ylim(0,100)
linea,=ax.plot([],[])

x=[]
y=[]

def dataUpdater(t):
    x.append(t)
    y.append(f(t))
    linea.set_data(x,y)
    fig.suptitle('t='+str(t)+' s')
    return linea,

anim=matan.FuncAnimation(fig,dataUpdater,t,repeat=True,interval=10)
plt.show()