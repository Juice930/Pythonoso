# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 13:00:28 2016

@author: Guillermo1
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

def F(x,y,z):
    return np.array([np.sin(x)*np.cos(y)*np.cos(z),-np.cos(x)*np.sin(y)*np.cos(z),np.cos(x)*np.cos(y)*np.sin(z)])
    
x=np.linspace(-3,3,11)
y=np.linspace(-3,3,11)
z=np.linspace(-1,1,5)

x,y,z=np.meshgrid(x,y,z)

u,v,w=F(x,y,z)[0],F(x,y,z)[1],F(x,y,z)[2]

fig=plt.figure()
ax=fig.gca(projection='3d')

ax.quiver(x,y,z,u,v,w,length=0.2,alpha=0.5)
plt.show()