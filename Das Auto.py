# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 13:41:53 2016

@author: Guillermo1
"""

class Auto(object):
    def __init__(self,color):
        self.color=color
        
class VW(Auto):
    def __init__(self,color,modelo):
        super(VW,self).__init__(color)
        self.modelo=modelo
Jet=VW('Blanco','Jetta')
print Jet.modelo,Jet.color