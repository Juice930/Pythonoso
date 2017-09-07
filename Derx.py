# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 16:36:55 2016

@author: Guillermo1
"""


import matplotlib.pyplot as plt
import numpy as np
#from mpl_toolkits.mplot3d import axes3d


tex=file("C:\Users\Guillermo1\Downloads\derx.txt",'r')
l = [ map(float,line.split()) for line in tex]
z=np.linspace(0,10,len(l)*len(l[0]))

fig1=plt.figure()
ax=fig1.gca(projection='3d')
ax.plot_surface(l,z,rstride=1,cstride=1,linewidth=0.5,alpha=0.3)
plt.show()