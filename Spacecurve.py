# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:48:05 2016

@author: Guillermo1
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

def sigma(t):
    return np.array([np.sinh(t),np.cos(t),np.log(t)])
    
t=np.linspace(0,10,300)
x,y,z=sigma(t)[0],sigma(t)[1],sigma(t)[2]

fig=plt.figure()
ax=fig.gca(projection='3d')
ax.plot(x,y,z)
plt.show()