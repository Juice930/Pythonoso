# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:06:51 2016

@author: Guillermo1
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation

def F(x,y,t):
    return np.sin(x+t)*np.cos(y+t)
pi=np.pi
t=np.linspace(0,10,101)
x=y=np.linspace(-2*pi,2*pi,31)
x,y=np.meshgrid(x,y)

fig=plt.figure()
ax=fig.gca(projection='3d')

def Update(t):
    z=F(x,y,t)
    ax.clear()
    ax.plot_surface(x,y,z,rstride=1,linewidth=.1,alpha=0.5)
    ax.set_zlim3d(-3,3)
    fig.suptitle('t='+str(t)+'s')
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    
anim=animation.FuncAnimation(fig,Update,t)
plt.show()