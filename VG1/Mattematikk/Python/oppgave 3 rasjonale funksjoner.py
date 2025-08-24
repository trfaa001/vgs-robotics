# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 11:51:29 2023

@author: trfaa001
"""

from pylab import *

def f(x):
    return(1-2 * x) / (x-2)

x = 8

while x >= -8 :
    if x != 2:
        print(x, f(x))
    x = x-1

x_verdier = linspace(-5, 5, 100)
y_verdier = f(x_verdier)

plot(x_verdier, y_verdier)
show()