# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:37:53 2016

@author: Guillermo1
"""

import matplotlib.pyplot as plt
import numpy as np

def F(x,y):
    return np.array([y*x,-x])

x=np.linspace(-1,1,20)
y=np.linspace(-1,1,20)

x,y=np.meshgrid(x,y)
u=F(x,y)[0]
v=F(x,y)[1]

fig=plt.figure()
ax=plt.subplot(111)
ax.quiver(x,y,u,v,width=0.003)
plt.plot()
plt.show()