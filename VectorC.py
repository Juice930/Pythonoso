# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:24:50 2016

@author: Guillermo1
"""

class Vector:
    def __init__(self,vec):
        self.vec=vec
        self.mod=self.modulo()
    def __add__(self,other):
        s=[]
        for i in range(len(self.vec)):
            s.append(self.vec[i]+other.vec[i])
        return Vector(s)
    def modulo(self):
        self.mod=0
        for i in self.vec:
            self.mod+=i**2
        self.mod=(self.mod)**(0.5)
        return self.mod
        
v1=Vector([1,0,1])
v2=Vector([2,0,2])
print v1.vec
print (v1+v2).modulo()