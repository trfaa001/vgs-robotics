# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:03:35 2023

@author: trfaa001
"""

from pylab import *

def f(x):
    return x**3 + x**2 + 2*x - 10

x_verdier = linspace(-5, 5, 100)
y_verdier = f(x_verdier)

plot(x_verdier, y_verdier)
show()