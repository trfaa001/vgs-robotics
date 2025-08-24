# -*- coding: utf-8 -*-
"""
Created on Mon May 12 10:03:32 2025

@author: trfaa001
"""

U = 1.0
B = 1.5
R = 0.50
m = 0.010
L = 0.10

v = 0
s = 0
t = 0
dt = 0.00001

while v <= 1.0:
    a = (U*B*L-v*B**2*L**2)/(R*m)
    v += a*dt
    s += v*dt 
    t += dt
print(t, "s", s, "m", v, "m/s", a, "m/s**2") 
