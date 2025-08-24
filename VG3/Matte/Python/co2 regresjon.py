# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 09:56:14 2025

@author: trfaa001
"""

from scipy.optimize import curve_fit
from pylab import plot, linspace, sin, loadtxt, exp
import matplotlib.pyplot as plt
import numpy as np

data_original = np.array(loadtxt("co2.txt", delimiter="\t", usecols = (3, 4))) #Gjøre om tekst fil til en array

x_original, y_original = zip(*data_original) #Gjøre om array til to lister

plt.scatter(x_original, y_original) #legg ut punktene fra listen

def f(t, a, b, c, d, e):
    return a*t+d*sin(c*t+e)+b

[a, b, c, d,e ] = curve_fit(f, x_original, y_original, maxfev=10000)[0] # Den nulte skal være variabelen

print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)
print("e = ", e)

plot(x_original, y_original, "o")
plt.xlabel("x-akse")
plt.ylabel("y-akse")
t = linspace(min(x_original), max(x_original), 1000)
plot(t, f(t, a, b, c, d, e), "r")
plt.show()

