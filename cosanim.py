# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 19:07:24 2016

@author: Guillermo1
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
    
fig=plt.figure()
ax=plt.subplot(111)
ax.set_xlim(0,10)
ax.set_ylim(-2,2)
linea,=ax.plot([],[])
def init():
    linea.set_data([], [])
    return linea,
    
def animate(t):
    x=np.linspace(0,10,1000)
    y=np.cos(2*np.pi*(x-0.01*t))
    linea.set_data(x,y)
    fig.suptitle('t='+str(t)+' s')
    return linea,
anim=animation.FuncAnimation(fig,animate,t,init_func=init,repeat=True, interval=20,frames=200,blit=True)
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()