#%%
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:01:50 2023

@author: trfaa001
"""

import math

e = 2.718281 # definerer e

a = 0
b = 1


#Definerer funksjonen som skal løses
def f(x):
    return 5*math.log(e, x**3+2)-6+x

#Finner mitden av intervalet
mitden = (a+b)/2

while abs(f(mitden) >= 0.0001):
    if f(a)*f(mitden) < 0:
        b=mitden
    else:
        a=mitden
    mitden= (a+b)/2

print("Løsningen på likningen er lik", round(mitden, 4))    
# %%
