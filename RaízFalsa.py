# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:11:15 2016

@author: Guillermo1
"""

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(2*x+1)-3./5*x+1

def biseccionFalsa(f,a,b,tol=1e-3):
    c=a
    if f(a)==0: return a
    if f(b)==0: return b
    while f(b)-f(a)>tol:
        c=raizFalsa(f,a,b)
        if f(c)*f(b)<0:
            a=c
        elif f(c)*f(a)<0:
            b=c
        print c,f(a),f(b)
        
    return c

def raizFalsa(f,a,b):
    return b-f(b)*(a-b)/float(f(a)-f(b))

print biseccionFalsa(f,-5,6,1e-6),f(-5),f(6)