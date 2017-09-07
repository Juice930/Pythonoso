# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:13:52 2016

@author: Guillermo1
"""

import numpy as np
import matplotlib.pyplot as plt


def S(t):
    return 2*t**3-t**2-3
def v(t):
    return 6*t**2-2*t
def a(t):
    return 12*t-2
t=np.arange(-2,6,0.1)
plt.plot(t,S(t),t,v(t),t,a(t),linewidth=2)
plt.show()