# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:15:49 2016

@author: Guillermo1
"""
import numpy as np
import matplotlib.pyplot as plt

scores=[3.,1.,0.2]

def softmax(x):
    summ=sum(np.exp(x))
    return np.array([np.exp(x[i])/summ for i in range(len(x))])

print softmax(scores)

x=np.arange(-2,6,0.1)*0.1
scores=np.stack([x,np.ones_like(x),0.2*np.ones_like(x)])
plt.plot(x,softmax(scores).T,linewidth=2)
plt.show()