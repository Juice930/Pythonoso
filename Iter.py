# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 14:31:41 2016

@author: Guillermo1
"""

def foo():
     print "begin"
     for i in range(3):
         print "before yield", i
         yield i
         print "after yield", i
     print "end"
f=foo()
f.next()