# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:19:33 2023

@author: trfaa001
"""

from pylab import *

def f(x): #selve funksjonen
    return x**2 + 2*x

x_verdier = linspace(-5, 5, 100) # 100 verdier mellom -5 og 5
y_verdier = f(x_verdier)

xlabel("x") #akse navn for x
ylabel("f(x)") #akse navn for y

axhline(y=0, color="black")
axvline(x=0, color="black")
grid()

plot(x_verdier, y_verdier)
show()