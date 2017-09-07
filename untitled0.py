# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:31:15 2016

@author: Juice
"""
def cuad(x):
    return x**2
def recta(x,m=1,b=0):   #Valores por default
    return m*x+b
def funcDicc(**Dicc):
    print Dicc
    
def superFunc(x,a=1,*tup,**Dicc):
    'SUPER Función'
    print 'x=',x
    print 'a=',a
    print 'tup\t',tup
    print 'Dicc\t',Dicc

A=[1,2,3,4]
B=[2,4,5,7]
print(map(cuad,A))

nuevoDicc={'m2': [2, 5], 'apple2': 5, 'banana2': 'Hola'}
funcDicc(x=1,y=2)
#superFunc(1,None,1,**nuevoDicc)
superFunc(1,5,10,25,'Equis',(1,2),True,apple=5,banana='Hola',m=[2,5],**nuevoDicc)
#print recta(x=2,m=5)
print superFunc.__doc__
"""print 'Qué hace? Mädchen'[-10:-2]
print complex(1,1)**3
print type(2)
print 2**(3/2)
print("{} Soy {}".format('Pablo','Pablo'))
print("{:.^30}".format('Hola'))
print ['h','o','l','a'].__str__()
print dir(set)"""