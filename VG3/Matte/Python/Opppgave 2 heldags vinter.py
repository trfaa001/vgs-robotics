# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:38:22 2024

@author: trfaa001
"""
Areal = 0

a = float(input("Hvor skall integralet starte"))
b = float(input("Hvor skall integralet ende"))

delta_x = 1

x_i = a

def f(x):
    return 1/x

for i in range(10000):
    Areal += (f(x_i)+f(x_i+delta_x))/2
    x_i += delta_x
print("Trapes metoden", Areal)
