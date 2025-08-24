# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:14:51 2023

@author: trfaa001
"""

def f(x):
    return -x**2 + 5*x

x = 0

while f(x+0.1) > f(x):
    x+=0.1
print(x)