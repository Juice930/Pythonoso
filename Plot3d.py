# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:23:49 2016

@author: Guillermo1
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

def f(x,y):
    return np.sin(np.sqrt(x**2+y**2))

x=np.linspace(-5,5,50)
y=np.linspace(-5,5,50)

x,y=np.meshgrid(x,y)

fig1=plt.figure()
ax=fig1.gca(projection='3d')
z=f(x,y)
ax.plot_surface(x,y,z,rstride=1,cstride=1,linewidth=0.5,alpha=0.3)
plt.show()